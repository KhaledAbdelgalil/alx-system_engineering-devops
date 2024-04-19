# Define packages to be installed
$python_version = '3.8.10'
$pip_package = 'pip3'
$werkzeug_version = '2.1.1'
$flask_version = '2.1.0'

# Ensure Python 3.8.10 is installed
package { 'python3':
  ensure => $python_version,
}

# Ensure pip3 is installed
package { $pip_package:
  ensure => installed,
  require => Package['python3'],
}

# Ensure Werkzeug 2.1.1 is installed
package { 'werkzeug':
  ensure   => $werkzeug_version,
  provider => 'pip3',
  require  => Package[$pip_package],
}

# Ensure Flask 2.1.0 is installed
package { 'flask':
  ensure   => $flask_version,
  provider => 'pip3',
  require  => Package['werkzeug'],
}
