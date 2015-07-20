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

import logging

from openerp import SUPERUSER_ID
from openerp import tools
from openerp.modules.module import get_module_resource
from openerp.osv import fields, osv
from openerp.tools.translate import _
from datetime import datetime, timedelta

_logger = logging.getLogger(__name__)

class hr_job(osv.Model):
    _inherit = "hr.job"
    _columns = {
        'no_of_recruitment': fields.integer('Expected New Employees','Number of recruitment', copy=False,
                                            help='Number of new employees you expect to recruit.'),
        'document_id': fields.many2one('compose.document','Document'),
        'release_date': fields.date('Update Date'),
        'end_date': fields.date('End Date')
    }

    def job_open(self, cr, uid, ids, context=None):
        self.write(cr, uid, ids, {'website_published': False}, context=context)
        return super(hr_job, self).job_open(cr, uid, ids, context)

    _defaults = {
        'release_date': fields.date.context_today,

    }

    def auto_cancel(self, cr, uid, context={}):
        today = datetime.now()
        job_ids = self.pool.get('hr.job').search(cr,uid,[('end_date','=',today.strftime('%Y-%m-%d %H:%M:%S')),('website_published','=',True)],context=context)
        if job_ids:
            for job in self.pool.get('hr.job').browse(cr,uid,job_ids,context=context):
                job.write({'website_published':False})
        else:
            raise
hr_job()

class compose_document(osv.Model):
    _name = "compose.document"
    _columns = {
        'name': fields.text('Name')
    }
compose_document()