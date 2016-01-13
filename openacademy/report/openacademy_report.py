# -*- coding: utf-8 -*-

from openerp import models, fields
from openerp import tools


class report_openacademy(models.Model):
    """OpenAcademy Analysis"""
    _name = "report.openacademy"
    _auto = False

    course_id = fields.Many2one('openacademy.course', 'Course')
    responsible_id = fields.Many2one('res.users', 'Responsible')
    instructor_id = fields.Many2one('res.partner', 'Instructor')
    name_session = fields.Char('Name Session')
    start_date = fields.Datetime('Event Date', readonly=True)
    seats = fields.Integer('Seats')
    duration = fields.Float('Duration')
    partner_id = fields.Many2one('res.partner', 'Partner')
    attendee_id = fields.Many2one('openacademy.attendee', 'Attendee')
    
    def init(self, cr):
        """Initialize the sql view for the OpenAcademy """
        tools.drop_view_if_exists(cr, 'report_openacademy')

        # TOFIX this request won't select events that have no registration
        cr.execute(""" CREATE VIEW report_openacademy AS (
            SELECT
                s.id::varchar || '/' || coalesce(a.id::varchar,'') AS id,
                c.id AS course_id,
                c.responsible_id AS responsible_id,
                s.instructor_id AS instructor_id,
                s.name AS name_session,
                s.start_date AS start_date,
                s.seats AS seats,
                s.duration AS duration,
                a.partner_id AS partner_id
                a.id AS attendee_id
            FROM
                openacademy_session s
                JOIN openacademy_attendee a ON (a.session_id=s.id)
                LEFT JOIN openacademy_course c ON (s.course_id=c.id)
        )
        """)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
