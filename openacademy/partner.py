# -*- coding: utf-8 -*-
# Licence AGPL
from openerp.osv import  osv, fields

#partner se hereda con la version 7 debido a que el padre esta en v7
class res_partner(osv.Model):
    _name = "res.partner"
    _inherit="res.partner"
    
    _columns = {
        'is_instructor': fields.boolean('Is Instructor'),
        'session_ids': fields.one2many('openacademy.session','instructor_id',string='Sessions'),
    }