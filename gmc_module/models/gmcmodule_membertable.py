from odoo import models, fields, api

class GmcModuleMemberTable(models.Model):
	_name = 'gmcmodule.membertable'
	
	employee_id = fields.Many2one('gmcmodule.employeetable',string='Member')
	name = fields.Char('Name', required=True)
	age = fields.Integer('Age', required=True)

