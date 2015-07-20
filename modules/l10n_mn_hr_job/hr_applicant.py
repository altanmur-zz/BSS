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

_logger = logging.getLogger(__name__)

class hr_applicant(osv.Model):
    _inherit = 'hr.applicant'

    _columns = {
        'state': fields.selection([('approved','Approved')],'State')
    }

    def approve(self, cr, uid, ids, context=None):
        for applicant in self.browse(cr, uid, ids):
            if applicant.job_id:
                job_num = applicant.job_id.no_of_recruitment
                print'===========job_num',job_num
                job_num -=1
                print'----------------------job_num',job_num
                applicant.job_id.write({'no_of_recruitment': job_num}, context=context)

                if applicant.job_id.no_of_recruitment == 0:
                    applicant.job_id.write({'website_published': False}, context=context)
        return self.write(cr, uid, ids, {'state': 'approved'}, context=context)

    # def job_open(self, cr, uid, ids, context=None):
    #     self.write(cr, uid, ids, {'website_published': False}, context=context)
    #     return super(hr_job, self).job_open(cr, uid, ids, context)

hr_applicant()
