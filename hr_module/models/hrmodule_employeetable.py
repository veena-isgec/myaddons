from odoo import models, fields, api



class HrModuleEmployeeTable(models.Model):
	_name = 'hrmodule.employeetable'	
	cardno = fields.Char('Card No.', required=True)
	name = fields.Char('Employee Name', required=True)
	dateofjoining = fields.Date('Date of Joining', required=True)
	user_id = fields.Many2one('res.users', ondelete='set null', string='Login User')	
	login = fields.Char('Login ID', related='user_id.login',store=True)
