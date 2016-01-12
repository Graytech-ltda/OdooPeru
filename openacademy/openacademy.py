# -*- coding: utf-8 -*-
# Licence AGPL

from openerp import models, fields

#curso tecnico
class openacademy_course(models.Model):
    _name       ="openacademy.course"
    
    name        =fields.Char('Name',size=32,required=True)
    description =fields.Text('Description')
    session_ids = fields.One2many('openacademy.session', 'course_id', string="Sessions")
    responsible_id = fields.Many2one('res.users',string='Responsible')
    
#lima
class openacademy_session(models.Model):
    _name       = "openacademy.session"
    
    name        = fields.Char('Name',size=32,required=True)
    start_date  = fields.Date('Date Start')
    seats       = fields.Integer('Seats')
    duration    = fields.Float('Duration')
    course_id   = fields.Many2one('openacademy.course',string='Course')
    attendee_ids = fields.One2many('openacademy.attendee', 'session_id', string="Attendees")
    instructor_id = fields.Many2one('res.partner',string='Instructor')

#cada voucher
class openacademy_attendee(models.Model):
    _name       = "openacademy.attendee"
    
    name        = fields.Char('Name',size=32)
    session_id  = fields.Many2one('openacademy.session',string='session')
    partner_id  = fields.Many2one('res.partner',string='Partner')

    