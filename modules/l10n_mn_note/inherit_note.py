from openerp import SUPERUSER_ID
from openerp.osv import osv, fields
from openerp.tools import html2plaintext

class note_note(osv.osv):
    """ Note """
    _inherit = 'note.note'

    _columns = {
    	'description': fields.text("Description")
    }