# install a nginx server

exec { 'install_nginx':
  command => '/bin/bash -c "apt-get -y update && apt-get -y install nginx && ufw allow \'Nginx HTTP\' && echo \'Hello World!\' > /var/www/html/index.html && sed -i \'24i\    rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;\' /etc/nginx/sites-available/default && service nginx start"',
  path    => ['/bin', '/usr/bin'],
  creates => '/var/www/html/index.html',
  require => Package['nginx'],
}
