find . -name '*.pyc' |xargs rm -feit
../lib/openerp-server -c ./openerp-server.conf
