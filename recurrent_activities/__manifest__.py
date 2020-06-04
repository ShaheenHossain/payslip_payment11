# -*- coding: utf-8 -*-
{
    "name": "Recurring Activities",
    "version": "11.0.1.0.1",
    "category": "Discuss",
    "author": "Odoo Tools",
    "website": "https://odootools.com/apps/11.0/recurring-activities-337",
    "license": "Other proprietary",
    "application": True,
    "installable": True,
    "auto_install": False,
    "depends": [
        "mail"
    ],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "data/data.xml",
        "views/recurrent_activity_template.xml",
        "views/view.xml"
    ],
    "qweb": [
        "static/src/xml/*.xml"
    ],
    "js": [
        
    ],
    "demo": [
        
    ],
    "external_dependencies": {},
    "summary": "The tool to plan and generate recurring activities according to the flexible timetable rules",
    "description": """
    This is the tool to schedule activity templates for regular and automatic generation of activities based on those templates. With the app you are sure that all recurring tasks will be planned and assigned for proper users. 

    Each activity recurring rule represents a template where you can define a target document (e.g. partner, opportunity, order, etc), a responsible user, summary, notes, regularity, deadline period
    The recurrence of activities is flexibly defined: each Tuesday and Friday, the first day or the second Saturday of the month, every 2 days, etc. Look at the section <a href='#activities_recurrence'>Activities Recurrence</a>
    Activity deadline is set as an activity creation date plus specified period in days (use the field 'Deadline in x Days')
    The rules to prepare repeated activities is available from the activities' systray in the header
    A recurring activity might be assigned for any Odoo internal user. You can grant responsibles a right to prepare rules for any user or grant a right for a specific user to access own recurring activities. Have a look at the section <a href='#recurrence_security'>Security Rules</a>
    # <a name='activities_recurrence'> Activities Recurrence</a>
    <div class="alert alert-warning">
<span style="font-size:18px">
    <i class="fa fa-book"></i> Be cautious with a month / year exact date: if it didn't exist, a last month day would be applied: 31/09 --> 30/09
</span>
</div>
It doesn't look fine to send a reminder on Sunday? No problem! Define regularity in a way you like.
<ul  style='font-size:18px;'>
<li>By days: generate an activity every day, each 5 days, each 181 days</li>
<li>By weeks: assign a task on definite week days (e.g. on Mondays and Thursdays) each week or each 2,3,7,... weeks </li>
<li>By months: 
<ul>
<li>For the first month day</li>
<li>For the last month day</li>
<li>For the exact date, e.g. the 16th</li>
<li>For a definite weekday, for instance, the first Monday, the last Friday, or the third Tuesday</li>
</ul>
</li>
<li>By years: on an exact year day, e.g. on the first of September each year</li>
</ul>
    # <a name='recurrence_security'> Security Rules </a>
    <ul style='font-size:18px;'>
<li>Any internal user has right to observe own recurring activities</li>
<li>Users with the right 'Only Own Recurrent Activities' may create, update and unlink recurring activities related to their users</li>
<li>Users with the right 'All Recurrent Activities' or with the right 'Administration > Access Rights' have full rights for all rules</li>
</ul>
    Plan a recurring activity for any task with any regularity
    Repeat an activity each month in a proper day
    Rules for scheduled activities is available from the Systray
    Have an unlimited number of rules for repeated activities
    Recurring activities planned by days
    Plan regular activities per years
    Security for scheduled activities' rules
""",
    "images": [
        "static/description/main.png"
    ],
    "price": "44.0",
    "currency": "EUR",
}