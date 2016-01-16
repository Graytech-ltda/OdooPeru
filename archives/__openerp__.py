# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2012 Cubic ERP - Teradata SAC (<http://cubicerp.com>).
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
{
    "name": "Arhives",
    "version": "1.0",
    "description": """
Manage all archives of an organization
======================================

The management of archives, enables you to track your all documents in easy and secure way.

Key Features
------------
* Manage documentes related to quality systems
* Manage your documentary process
* Optimize the comunication inside the organization

Dashboard / Reports for archives will include:
----------------------------------------------
* Archives Report
    """,
    "author": "Cubic ERP",
    "website": "http://cubicERP.com",
    "category": "Tools",
    "depends": [
        "hr",
        "document",
        "mail",
        "stock",
        ],
    "data":[
        "archives_view.xml",
	    ],
    "demo_xml": [],
    "active": False,
    "installable": True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
