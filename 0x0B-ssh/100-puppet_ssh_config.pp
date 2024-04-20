# change SSH config file
exec {'echo':
path    => '/bin:/usr/bin',
command => 'echo "    IdentityFile ~/.ssh/school\n    PasswordAuthentication no\n" >> /etc/ssh/ssh_config',
}