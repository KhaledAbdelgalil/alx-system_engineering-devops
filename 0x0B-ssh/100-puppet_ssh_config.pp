# change SSH config file
exec {'change_ssh_config':
path    => '/bin:/usr/bin',
command => 'echo "    IdentityFile ~/.ssh/school\n    PasswordAuthentication no\n" >> /etc/ssh/ssh_config',
}