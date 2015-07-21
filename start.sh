find . -name '*.pyc' |xargs rm -f
../lib/openerp-server -c ./openerp-server.conf
