# Ensure Python 3.8.10 is installed
package { 'python3.8':
  ensure => '3.8.10',
}

# Install pip for Python 3.8
package { 'python3-pip':
  ensure => installed,
}

# Install Flask 2.1.0 using pip3
exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  creates => '/usr/local/lib/python3.8/dist-packages/Flask',
  require => Package['python3-pip'],
}

# Install Werkzeug 2.1.1 using pip3
exec { 'install_werkzeug':
  command => '/usr/bin/pip3 install Werkzeug==2.1.1',
  creates => '/usr/local/lib/python3.8/dist-packages/werkzeug',
  require => Package['python3-pip'],
}
