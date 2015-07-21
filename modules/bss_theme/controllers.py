from openerp import http

class Bss(http.Controller):
    @http.route('/index', auth='public', website=True)
    def index(self, **kw):
        return http.request.render('bss_theme.bss_index')

