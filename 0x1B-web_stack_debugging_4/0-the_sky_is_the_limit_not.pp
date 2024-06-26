# Fixes an nginx site that can't handle multiple concurrent requests
exec { 'fix--for-nginx':
  command => "bash -c \"sed -iE 's/^ULIMIT=.*/ULIMIT=\\\"-n 4000\\\"/' \
/etc/default/nginx; service nginx restart\"",
  path    => '/usr/bin:/usr/sbin:/bin'
}
