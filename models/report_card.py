from odoo import api, models, fields, _ 
from datetime import datetime, date
from odoo.exceptions import ValidationError


class Reporting(models.Model): 
    _name = 'report.card'
    _rec_name = 'report_date'

    employee_name = fields.Many2one('res.users', string='Employee', readonly=True, default=lambda self: self.env.user )
    report_date = fields.Date(string='Date', readonly = True, compute = '_compute_date', store= True)
    completed_tasks = fields.Text('Completed Tasks', required = True)
    company_visits = fields.Char('Company Visits')
    lines_test = fields.Char('Lines')
    plans_for_next_day = fields.Text('Next Day Plans')
    issues_challs = fields.Text('Issues or Challenges')
    remarks = fields.Text('Remarks')
    attachments  = fields.Binary()


    @api.depends('completed_tasks')
    def _compute_date(self):
        for rec in self:
            rec.report_date = date.today().strftime('%Y-%m-%d')


    @api.constrains('report_date','employee_name')
    def validate_report(self):
        for rec in self: 
            dates = self.env['report.card'].search([
                    ('report_date', '=' ,rec.report_date),
                    ('id', '!=' ,rec.id)
                    ,('employee_name', "=", rec.employee_name.id)
                    ])
            if dates:
                raise ValidationError(_("You have already created a report today, please comeback tomorrow."))