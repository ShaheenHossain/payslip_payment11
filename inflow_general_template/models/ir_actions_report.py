# -*- coding: utf-8 -*-


import os
import base64
import tempfile
import logging
import subprocess
from contextlib import closing
from odoo.exceptions import UserError
from PyPDF2 import PdfFileWriter, PdfFileReader
from odoo.tools.misc import find_in_path
from odoo import api, models, tools, _

_logger = logging.getLogger(__name__)

def _get_wkhtmltopdf_bin():
    return find_in_path('wkhtmltopdf')


class IrActionsReport(models.Model):
    _inherit = 'ir.actions.report'

    @api.model
    def _run_wkhtmltopdf(self,
            bodies, header=None, footer=None, landscape=False,
            specific_paperformat_args=None, set_viewport_size=False):
        '''Execute wkhtmltopdf as a subprocess in order to convert html given in input into a pdf
        document.

        :param bodies: The html bodies of the report, one per page.
        :param header: The html header of the report containing all headers.
        :param footer: The html footer of the report containing all footers.
        :param landscape: Force the pdf to be rendered under a landscape format.
        :param specific_paperformat_args: dict of prioritized paperformat arguments.
        :param set_viewport_size: Enable a viewport sized '1024x1280' or '1280x1024' depending of landscape arg.
        :return: Content of the pdf as a string
        '''
        paperformat_id = self.paperformat_id or self.env.user.company_id.paperformat_id

        # Build the base command args for wkhtmltopdf bin
        command_args = self._build_wkhtmltopdf_args(
            paperformat_id,
            landscape,
            specific_paperformat_args=specific_paperformat_args,
            set_viewport_size=set_viewport_size)

        files_command_args = []
        temporary_files = []
        if header:
            head_file_fd, head_file_path = tempfile.mkstemp(suffix='.html', prefix='report.header.tmp.')
            with closing(os.fdopen(head_file_fd, 'wb')) as head_file:
                head_file.write(header)
            temporary_files.append(head_file_path)
            files_command_args.extend(['--header-html', head_file_path])
        if footer:
            foot_file_fd, foot_file_path = tempfile.mkstemp(suffix='.html', prefix='report.footer.tmp.')
            with closing(os.fdopen(foot_file_fd, 'wb')) as foot_file:
                foot_file.write(footer)
            temporary_files.append(foot_file_path)
            files_command_args.extend(['--footer-html', foot_file_path])

        paths = []
        for i, body in enumerate(bodies):
            prefix = '%s%d.' % ('report.body.tmp.', i)
            body_file_fd, body_file_path = tempfile.mkstemp(suffix='.html', prefix=prefix)
            with closing(os.fdopen(body_file_fd, 'wb')) as body_file:
                body_file.write(body)
            paths.append(body_file_path)
            temporary_files.append(body_file_path)

        pdf_report_fd, pdf_report_path = tempfile.mkstemp(suffix='.pdf', prefix='report.tmp.')
        os.close(pdf_report_fd)
        temporary_files.append(pdf_report_path)

        try:
            wkhtmltopdf = [_get_wkhtmltopdf_bin()] + command_args + files_command_args + paths + [pdf_report_path]
            process = subprocess.Popen(wkhtmltopdf, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = process.communicate()

            if process.returncode not in [0, 1]:
                if process.returncode == -11:
                    message = _(
                        'Wkhtmltopdf failed (error code: %s). Memory limit too low or maximum file number of subprocess reached. Message : %s')
                else:
                    message = _('Wkhtmltopdf failed (error code: %s). Message: %s')
                raise UserError(message % (str(process.returncode), err[-1000:]))
        except:
            raise

        # Merged two pdfs in single
        company_id = self.env.user.company_id
        model_id = self.env['ir.model'].sudo().search([('model', '=', self.model)])
        report_extra_content_id = self.env['report.extra.content'].search([('model_id', '=', model_id.id), ('company_id', '=', company_id.id)])
        if report_extra_content_id and report_extra_content_id.append_extra_content:
        # if company_id and company_id.append_extra_content and self.model in ['sale.order']:
        # if model_id.append_extra_content:
            pdf_custom_fd, pdf_custom_path = tempfile.mkstemp(suffix='.pdf', prefix='report.tmp.custom.')
            with open(pdf_custom_fd, 'wb') as pcd:
                pcd.write(base64.decodestring(report_extra_content_id.append_extra_content))

            custom_documents = [pdf_report_path, pdf_custom_path]
            writer = PdfFileWriter()
            streams = []  # We have to close the streams *after* PdfFilWriter's call to write()
            merged_file_fd, merged_file_path = tempfile.mkstemp(suffix='.pdf', prefix='report.merged.tmp.')
            try:
                for document in custom_documents:
                    pdfreport = open(document, 'rb')
                    streams.append(pdfreport)
                    reader = PdfFileReader(pdfreport)
                    for page in range(0, reader.getNumPages()):
                        writer.addPage(reader.getPage(page))

                with closing(os.fdopen(merged_file_fd, 'wb')) as merged_file:
                    writer.write(merged_file)
            finally:
                for stream in streams:
                    try:
                        stream.close()
                    except Exception:
                        pass

            temporary_files.extend([pdf_custom_path, merged_file_path])

            with open(merged_file_path, 'rb') as pdf_document:
                pdf_content = pdf_document.read()
        else:
            with open(pdf_report_path, 'rb') as pdf_document:
                pdf_content = pdf_document.read()

        # Manual cleanup of the temporary files
        for temporary_file in temporary_files:
            try:
                os.unlink(temporary_file)
            except (OSError, IOError):
                _logger.error('Error when trying to remove file %s' % temporary_file)

        return pdf_content