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
        })



class SessionReport(models.AbstractModel):
    _name = 'report.openacademy.report_session_document1'
    _inherit = 'report.abstract_report'
    _template = 'openacademy.report_session_document1'
    _wrapped_report_class = SessionReport_print

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
