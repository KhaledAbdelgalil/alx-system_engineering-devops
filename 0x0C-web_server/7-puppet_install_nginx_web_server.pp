# install a nginx server

package { 'nginx':
  ensure => 'installed',
}

file { '/var/www/html/index.html':
  ensure  => 'file',
  content => 'Hello World!',
}

file { '/etc/nginx/sites-available/default':
  ensure  => 'file',
  content => template('nginx/default.conf.erb'),
  require => Package['nginx'],
}

service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => File['/etc/nginx/sites-available/default'],
}

firewall { 'allow nginx http':
  port   => 80,
  proto  => 'tcp',
  action => 'accept',
}
