# -*- coding: utf-8 -*-
# Licence AGPL

from openerp import models, fields, api


class openacademy_enroll(models.TransientModel):
    _name = 'openacademy.enroll'
    
    @api.model #cuando no existe record set, api.multi: cuando multiples record set 
    def _default_session_id(self):
        return self.env.context.get('active_id', False) #cuando no existe la llave me retorna un valor alternativo, en este caso False
    
    @api.multi
    def action_enroll(self):
        
        #referencia sobre el objeto attendee sobre el cual invocamos a todos sus métodos
        attendee_model  = self.env['openacademy.attendee']
        
        res= self.env.context.get('active_ids',[])
        
        if len(res)<=1:
            res= [self.session_id.id]
        

        for attendee in self.attendee_ids:
            
            for s in res:
                attendee_model.create({
                'name'      : attendee.name,
                'partner_id': attendee.partner_id.id,
                'session_id': s,
                })

        #se confirma que se cierra la ventana del wizard si se seleccionan mas wizards (anidados)
        return {}
    
    session_id      = fields.Many2one('openacademy.session', string='Session', default=_default_session_id)
    attendee_ids    = fields.One2many('openacademy.enroll.attendee', 'enroll_id', string='Attendees')

    
class openacademy_enroll_attendee(models.TransientModel):
    _name = 'openacademy.enroll.attendee'
    
    name        = fields.Char(string="Name")
    partner_id  = fields.Many2one('res.partner', string='Partner')
    enroll_id   = fields.Many2one('openacademy.enroll', string="Enroll")
