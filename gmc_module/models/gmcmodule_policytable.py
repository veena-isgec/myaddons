from odoo import models, fields



class GmcModulePolicyTable(models.Model):
	_name = 'gmcmodule.policytable'	
	name = fields.Char('Title', required=True)
	startdate = fields.Date('Start Date', required=True)	
	enddate = fields.Date('End Date', required=True)	
	premium = fields.Float('Premium per Lac', required=True)
	
