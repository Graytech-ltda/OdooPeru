# -*- coding: utf-8 -*-

from openerp import models, api
import time
from openerp.report import report_sxw

class SessionReport_print(report_sxw.rml_parse):

    def __init__(self, cr, uid, name, context=None):
        if context is None:
            context = {}
        super(SessionReport_print, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
            'time': time,
            'get_product': self._get_product
        })

    def _get_product(self,code):
        self.cr.execute("SELECT t.name FROM product_product p join product_template t on (p.product_tmpl_id=t.id) where p.default_code = %s",(code,))
        res = self.cr.fetchall()
        return res and res[0][0] or ''


class SessionReport(models.AbstractModel):
    _name = 'report.openacademy.report_session_document1'
    _inherit = 'report.abstract_report'
    _template = 'openacademy.report_session_document1'
    _wrapped_report_class = SessionReport_print

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
