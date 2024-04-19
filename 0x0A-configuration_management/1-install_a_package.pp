#!/usr/bin/puppet

# Ensure python3-pip is installed
package { 'python3-pip':
  ensure => installed,
}

# Install Flask and its dependencies using pip3
exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  path    => ['/usr/bin'],
  unless  => '/usr/bin/pip3 show flask | grep -q "Version: 2.1.0"',
}
