# -*- coding: utf-8 -*-
# Licence AGPL

from openerp import models, fields, api, exceptions
from datetime import timedelta
from datetime import datetime

#curso tecnico
class openacademy_course(models.Model):
    _name       ="openacademy.course"
    
    #Fields declaration
    name        =fields.Char('Name',size=32,required=True)
    description =fields.Text('Description')
    session_ids = fields.One2many('openacademy.session', 'course_id', string="Sessions")
    responsible_id = fields.Many2one('res.users',string='Responsible')
    
    
    #Constraint a nivel de sql
    _sql_constraints = [('check_name','check(name<>description)','The name must be different of description'),
                        ('check_name','unique(name)','The name must be unique')]
    
    @api.one
    def copy(self, defaults):
        defaults['name']= self.name + ' (copy)'
        return super(openacademy_course, self).copy(defaults)
    
    
#lima
class openacademy_session(models.Model):
    _name       = "openacademy.session"
    
    #Functions declaration
    @api.one #or multi
    @api.depends('attendee_ids','seats') #calcula la fnc cuando cambian los argumentos
    def _remaining_seats(self):
        #porcentaje de sillas restantes
        self.remaining_seats = (1.0 - (self.seats and float(len(self.attendee_ids))/self.seats or 0.0))*100
    
    @api.one #or multi
    @api.constrains('seats') #calcula la fnc cuando cambian los argumentos
    def _check_seats(self):
        if self.seats <= 0:
            raise exceptions.ValidationError("The seats doesn't be negative number")
    
    @api.onchange('seats')#1 guion bajo no se puede acceder via webservice, 0 guion bajo es publica, 2 guion bajo en python no se puede acceder desde otras clases 
    def onchange_seats(self):
        if self.seats <= 0:
            return {'warning':{'title':'Warning!','message':"Seats doesn't be negative number"}}
    
    @api.one #or multi
    @api.constrains('instructor_id','attendee_ids') #calcula la fnc cuando cambian los argumentos
    def _check_instructor(self):
        if self.instructor_id.id in [ a.partner_id.id for a in self.attendee_ids ]:
            raise exceptions.ValidationError("The instructor must not be into the attendees")
    
    @api.one
    @api.depends('start_date','duration') #calcula la fnc cuando cambian los argumentos
    def _date_end(self):
        self.date_end = (datetime.strptime(self.start_date,"%Y-%m-%d") + timedelta(days=self.duration)).strftime("%Y-%m-%d")
    
    @api.one
    def _date_end_inv(self):
        self.duration = (datetime.strptime(self.date_end,"%Y-%m-%d")-datetime.strptime(self.start_date,"%Y-%m-%d")).days
    
    @api.one
    @api.depends('attendee_ids','attendee_ids.session_id')
    def _attendee_count(self):
        self.attendee_count= len(self.attendee_ids)
        
    #Fields declaration
    name            = fields.Char('Name',size=32, required=True)#fields.Relate('attendee_ids.')
    start_date      = fields.Date('Start Date', default = fields.Date.today)
    seats           = fields.Integer('Seats', default=1)
    duration        = fields.Float('Duration')
    course_id       = fields.Many2one('openacademy.course',string='Course')
    attendee_ids    = fields.One2many('openacademy.attendee', 'session_id', string="Attendees")
    instructor_id   = fields.Many2one('res.partner',string='Instructor',domain=['|',('is_instructor','=',True),('category_id.name','in',['Nivel 1','Nivel 2'])])
    remaining_seats = fields.Float('Remaining seats', compute=_remaining_seats)
    active          = fields.Boolean('Active',default=True)
    date_end        = fields.Date('End Date', compute=_date_end, inverse=_date_end_inv)
    attendee_count  = fields.Integer('Attendee Count', compute=_attendee_count, store=True)
    
    
#cada voucher
class openacademy_attendee(models.Model):
    _name       = "openacademy.attendee"
    
    #Fields declaration
    name        = fields.Char('Name',size=32)
    session_id  = fields.Many2one('openacademy.session',string='session')
    partner_id  = fields.Many2one('res.partner',string='Partner')

    