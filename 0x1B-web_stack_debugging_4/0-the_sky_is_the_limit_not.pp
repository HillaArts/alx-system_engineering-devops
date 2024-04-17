# Assuming you have ERB templates for your nginx
# config files, insert new requests limit and restart nginx
exec { '/usr/bin/env sed -i s/15/1000/ /etc/default/nginx': }
-> exec { '/usr/bin/env service nginx restart': }
