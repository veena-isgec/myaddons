from odoo import api,fields,models,_
from datetime import datetime
import xlwt 
import io
import base64
import shutil
from os import path

class gmc_details_wizard2(models.TransientModel):
    _name='gmc.details.wizard2'
    gmc_policy_id = fields.Many2one('gmcmodule.policytable',string='Policy Type')
    
    def button_excel(self, data, context=None):
        try:
            import xlwt
        except Exception(e):
        raise wizard.except_wizard(_('User Error'), _('Please Install xlwt Library.!'))
	src= path.realpath("testfile1.xls")
	head, tail = path.split(src)
	print("path:" + head)
	print("path:" + tail)
	dst = src + ".bak"
	shutil.copy(src,dst)
	print(SRC + "copied as " + dst)

        filename = 'GMC Details.xls'
        string = 'Employee Details'
        wb = xlwt.Workbook(encoding='utf-8')
        worksheet = wb.add_sheet(string)
        style_value = xlwt.easyxf('font: bold on ,colour_index 0x36;' "borders: top double , bottom double ,left double , right double;")
        style_header = xlwt.easyxf('font: bold on ,colour_index black;' "borders: top double , bottom double ,left double , right double;")
        style = xlwt.XFStyle()
        fnt = xlwt.Font()
        fnt.colour_index = 0x36
        fnt.bold = True
        fnt.width = 256 * 30
        style.font = fnt
        style1 = xlwt.XFStyle()
        fnt = xlwt.Font()
        fnt.colour_index = 0x86
        fnt.bold = True
        fnt.width = 256 * 30
        style1.font = fnt
       
        worksheet.write(0,0,'Sl.No',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,1,'EmpCode',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,2,'Employee Name',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,3,'Sum Insured(in Lac)',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))
        worksheet.write(0,4,'Prorata Premium in Rs.',xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'))

        if self.gmc_policy_id:
            b = 1
            cnt = 0
            employee_pool = self.env['gmcmodule.employeetable']
            searched_employees = employee_pool.search([('policytype_id','=',self.gmc_policy_id.name)])
            for thisemployee in searched_employees:
                b+=1
                cnt+=1
                worksheet.write(b, 0, cnt)
                worksheet.write(b, 1, thisemployee.cardno or '')
                worksheet.write(b, 2, thisemployee.name or '')
                worksheet.write(b, 3, thisemployee.suminsured or '')
                worksheet.write(b, 4, thisemployee.proratapremium or '')

        fp = io.BytesIO()
        wb.save(fp)
        out = base64.encodestring(fp.getvalue())
        view_gmcreport_id=self.env['view.gmcreport2'].create({'file_name':out,'datas_fname':filename})
        return {
        'res_id'   :view_gmcreport_id.id,
        'name'     :'GMC Details Report',
        'view_type':'form',
        'view_mode':'form',
        'res_model':'view.gmcreport2',
        'view_id'  : False ,
        'type'     :'ir.actions.act_window',
    }
      
class view_gmcreport2(models.TransientModel):
    _name = 'view.gmcreport2'
    _rec_name = 'datas_fname'
    datas_fname=fields.Char('File Name', size=256)
    file_name=fields.Binary('Report')
    
