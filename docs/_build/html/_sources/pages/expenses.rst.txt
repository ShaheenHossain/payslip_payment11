Expenses
========

Expenses being done can be broadly classified into two categories:

#. **Expenses being incurred and managed by the Company (Company Expenses)**
#. **Expenses being incurred by the employee and managed by the Company (Employee Expenses)**

Depending on the type, the workflow will be different


Company Expenses can be further categorized into

#. **Recurring - GST Expenses - Recurring on a timely basis and whose input GST has to be claimed by the company. Eg. Mobile/Telephone Bills**
#. **Recurring - Non-GST Expenses - Recurring on a timely basis and whose input GST cannot be claimed by the company. Eg. Local Broadband expenses, Office Rent, Electricity Bills**
#. **Non-Recurring - GST Expenses - One Time Expenses such as buying IT assets such as computers, Electrical Equipment**
#. **Non-recurring - Non-GST Expenses - One time expenses such as Stationary, Fooding etc**




How to set expense types
########################

The first step to track expenses is to configure the expense types (managed as products in Odoo) that your company allows, from the Configuration menu. When a specific expense is reimbursed at a fixed price, set a cost on the product. Otherwise keep the cost at 0.0 and employees will report the real cost per expense.

.. image:: expenses/expense_product.png
   :align: center


Here are some examples to configure:

#. Restaurant: Cost: 0.00 (the cost of the ticket will be recorded on every expense)
#. Travel with Personal Car: Cost: 0.30 (the price per mile reimbursed by the company is fixed)
#. Hotel: Cost: 0.00 (the cost of the ticket will be recorded on every expense)
#. Others: Cost: 0.0

Don’t forget to set an expense tax on each expense type (and an account if you use Odoo Accounting). It’s usually a good practice to use a tax that is configured with Tax Included in Price. That way, employees report expenses with prices including taxes, which is usually the expected behaviour.


.. tip:: The Sales app allows you to specify unit of measures for your expense types (units, miles, nights, etc.). Go to Sales ‣ Configuration ‣ Settings and check Some products may be sold/purchased in different units of measure (advanced).

.. toctree::
   :maxdepth: 2
   :caption: How to Record Expenses:

   /pages/expenses/expense_by_employee.rst