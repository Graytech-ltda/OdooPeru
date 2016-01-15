# -*- coding: utf-8 -*-

from openerp import models, fields, api


class SessionReport(models.AbstractModel):
    _name = 'report.openacademy.report_session_document1'
    
    @api.multi
    def render_html(self, data=None):
        report_obj = self.env['report']
        report = report_obj._get_report_from_name('openacademy.report_session_document1')
        docargs = {
            'doc_ids': self._ids,
            'doc_model': report.model,
            'docs': self,
        }
        return report_obj.render('openacademy.report_session_document1', docargs)


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
