# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

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
    course_id   = fields.Many2one('openacademy.course',string='course')
    attendee_ids = fields.One2many('openacademy.attendee', 'session_id', string="Attendees")
    instructor_id = fields.Many2one('res.partner',string='Instructor')

#cada voucher
class openacademy_attendee(models.Model):
    _name       = "openacademy.attendee"
    
    name        = fields.Char('Name',size=32)
    session_id  = fields.Many2one('openacademy.session',string='session')
    partner_id  = fields.Many2one('res.partner',string='Partner')

    