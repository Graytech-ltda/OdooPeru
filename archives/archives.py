# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#     Copyright (C) 2012 Cubic ERP - Teradata SAC (<http://cubicerp.com>).
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

from openerp import models, fields, api
from openerp.tools.translate import _

class archives_medium_type(models.Model):
    _name = "archives.medium.type"
    name = fields.Char('Code', required=True)

class archives_table_department(models.Model):
    _name = "archives.table.department"
    retention_table_id = fields.Many2one('archives.retention.table', 'Retention Table')
    department_id = fields.Many2one('hr.department', 'Department')
    work_time = fields.Float('Work Time', help="Time in days")
    
class archives_retention_table(models.Model):
    _name = "archives.retention.table"
    _description = "Archives Retention Table"
    
    name = fields.Char('Name', size=1024, required=True)
    code = fields.Char('Code', size=32, required=True)
    type =  fields.Selection([('view','View'),
                              ('normal','Normal')], 'Type', required=True)
    parent_id = fields.Many2one('archives.retention.table', 'Parent Table')
    retention_time_handling = fields.Integer('Retention Time Handling', help="Time in years")
    retention_time_archive = fields.Integer('Retention Time Archive', help="Time in years")
    final_disposition_preserve = fields.Boolean('Final Disposition Preserve')
    final_disposition_microfilm = fields.Boolean('Final Disposition Microfilm')
    final_disposition_removal = fields.Boolean('Final Disposition Removal')
    final_disposition_selection = fields.Boolean('Final Disposition Selection')
    medium_type_ids = fields.Many2many('archives.medium.type','archives_table_medium_rel', string="Medium Types")
    
    active = fields.Boolean('Acive', default=True)
    
class archives_process_template(models.Model):
    _name = "archives.process.template"
    _inherit = ['mail.thread', 'ir.needaction_mixin']
    
    name = fields.Char('Name', required=True)
    code = fields.Char('Code', size=32, required=True)
    type =  fields.Selection([('view','View'),
                              ('normal','Normal')], 'Type', required=True)
    parent_id = fields.Many2one('archives.process.template','Parent Template')
    retention_table_id = fields.Many2one('archives.retention.table', 'Retention Table', required=True)
    department_id = fields.Many2one('hr.department', 'Department')
    
    description = fields.Text('Description')
    state = fields.Selection([('draft','Draft'),
                              ('done','Done'),
                              ('cancel','Cancel')], 'State', readonly=True, default="draft")
    step_ids = fields.One2many('archives.process.template.step', 'process_template_id', string="Steps")
    
class archives_process_template_step(models.Model):
    _name = "archives.process.template.step"
    
    sequence = fields.Integer('Sequence', required=True)
    name = fields.Char('Name', required=True)
    process_template_id = fields.Many2one('archives.process.template','Process Template')
    retention_table_ids = fields.Many2many('archives.retention.table', 'archives_process_tmpl_table_rel', 'Retention Tables')
    work_time = fields.Float('Work Time', help="Time in days")
    
class archives_process(models.Model):
    _name = "archives.process"
    _inherit = ['mail.thread', 'ir.needaction_mixin']
    
    name = fields.Char('Code', size=32, required=True)
    template_id = fields.Many2one('archives.process.template','Process Template')
    retention_table_id = fields.Many2one('archives.retention.table', 'Retention Table', required=True)
    department_id = fields.Many2one('hr.department', 'Department')
    description = fields.Text('Description')
    date_start = fields.Datetime('Date Start')
    date_compute = fields.Datetime('Date Compute', readonly=True)
    date_end = fields.Datetime('Date End')
    state = fields.Selection([('run','Run'),
                              ('done','Done'),
                              ('cancel','Cancel')], 'State', readonly=True, default="run")
    step_ids = fields.One2many('archives.process.step', 'process_id', string="Steps")
    
class archives_process_step(models.Model):
    _name = "archives.process.step"
    
    sequence = fields.Integer('Sequence', required=True)
    name = fields.Char('Name', required=True)
    process_id = fields.Many2one('archives.process','Archives Process')
    document_ids = fields.Many2many('archives.document', 'archives_process_document_rel', 'Archives Documents')
    date_start = fields.Datetime('Date Start')
    date_compute = fields.Datetime('Date Compute', readonly=True)
    date_end = fields.Datetime('Date End')    
    state = fields.Selection([('wait','Wait'),
                              ('run','Run'),
                              ('done','Done'),
                              ('cancel','Cancel')], 'State', readonly=True, default="wait")    
    
class archives_collection_location(models.Model):
    _name = "archives.collection.location"
    
    name = fields.Char('Name', required=True)
    type =  fields.Selection([('view','View'),
                              ('temporal','Temporal'),
                              ('handling','Handling'),
                              ('archive','Archive'),
                              ('destruction','Destruction'),
                              ('conversion','Conversion')], 'Type', required=True)
    parent_id = fields.Many2one('archives.collection.location', 'Parent Location')
    medium_type_ids = fields.Many2many('archives.medium.type', 'archives_collection_location_medium_rel', string="Medium Types")
    partner_id = fields.Many2one('res.partner', string='Location Adress')

class archives_collection(models.Model):
    _name = "archives.collection"
    
    name = fields.Char('Code', required=True)
    description = fields.Text('Description')
    location_id = fields.Many2one('archives.collection.location', 'Current Location', readonly=True) #Función
    move_ids = fields.One2many('archives.collection.move', 'collection_id', string="Moves")
    
class archives_collection_move(models.Model):
    _name = "archives.collection.move"
    
    name = fields.Char('Name', required=True)
    date = fields.Datetime('Date')
    collection_id = fields.Many2one('archives.collection', string="Collection")
    employee_id = fields.Many2one('hr.employee', string="Responsible Employee")
    location_id = fields.Many2one('archives.collection.location', string="Source Location", required=True)
    location_dest_id = fields.Many2one('archives.collection.location', string="Destinity Location", required=True)
    
class archives_document(models.Model):
    _name = "archives.document"
    _inherit = ['mail.thread', 'ir.needaction_mixin']
    
    name = fields.Char('Name', size=32, required=True, readonly=True, states={'pending': [('readonly', False)]})
    parent_id = fields.Many2one('archives.document', string="Parent Document",
                                readonly=True, states={'pending': [('readonly', False)]})
    subject = fields.Text('Subject', readonly=True, states={'pending': [('readonly', False)]})
    retention_table_id = fields.Many2one('archives.retention.table', string='Retention Table', required=True,
                                         readonly=True, states={'pending': [('readonly', False)]})
    responsible_id = fields.Many2one('res.users', string="Responsible User", readonly=True) #Function from document.move
    process_step_id = fields.Many2one('archives.process.step', string='Process Step',
                                      readonly=True, states={'pending': [('readonly', False)]})
    collection_id = fields.Many2one('archives.collection', string='Collection',
                                    readonly=True, states={'pending': [('readonly', False)]})
    date_start = fields.Datetime('Date Start', readonly=True, states={'pending': [('readonly', False)]})
    date_compute = fields.Datetime('Date Compute', readonly=True)
    date_end = fields.Datetime('Date End', readonly=True)
    partner_id = fields.Many2one('res.partner', string='Reply To',
                                 readonly=True, states={'pending': [('readonly', False)]})
    state = fields.Selection([('pending','Pending'),
                              ('done','Done'),
                              ('cancel','Cancel')], 'State', readonly=True, default="pending")
    folios = fields.Integer('Folios', readonly=True, states={'pending': [('readonly', False)]})
    adjunct = fields.Integer('Adjunct', readonly=True, states={'pending': [('readonly', False)]})
    propagate = fields.Boolean('Parent Propagate',
                                 readonly=True, states={'pending': [('readonly', False)]})
    move_ids = fields.One2many('archives.document.move', 'document_id', string="Moves",
                                 readonly=True, states={'pending': [('readonly', False)]})
    version_ids = fields.One2many('archives.document.version', 'document_id', string="Versions",
                                 readonly=True, states={'pending': [('readonly', False)]})
    company_id = fields.Many2one('res.company', string="Company", required=True, 
                                 default=lambda self: self.env.user.company_id.id,
                                 readonly=True, states={'pending': [('readonly', False)]})
    

class achives_document_version(models.Model):
    _name = "archives.document.version"
    
    document_id = fields.Many2one('archives.document', string="Docuement", required=True)
    name = fields.Char('Name', required=True)
    date = fields.Date('Date', required=True)
    attachment_ids = fields.One2many('ir.attachment', 'archive_version_id', string="Attachments")

class achives_document_move_type(models.Model):
    _name = "archives.document.move.type"
    name = fields.Char('Name', required=True)

class achives_document_move(models.Model):
    _name = "archives.document.move"
    
    document_id = fields.Many2one('archives.document', string="Docuement", required=True)
    type = fields.Many2one('archives.document.move.type', string="Move Type", required=True)
    date_start = fields.Datetime('Date Start')
    date_end = fields.Datetime('Date End')
    source_department_id = fields.Many2one('hr.department', string="Source Department") # related to user
    dest_department_id = fields.Many2one('hr.department', string="Destinity Department") # related to user
    source_user_id = fields.Many2one('res.users', string="Source User", required=True)
    dest_user_id = fields.Many2one('res.users', string="Destinity User", required=True)
    state = fields.Selection([('pending','Pending'),
                              ('acept','Acept'),
                              ('reject','Reject')], 'State', readonly=False, default="pending")