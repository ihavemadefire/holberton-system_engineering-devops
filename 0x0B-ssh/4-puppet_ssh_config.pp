# Sets up config file

file_line { 'Turn off passwd auth':
  ensure => file,
  path   => '/home/vagrant/.ssh/config',
  line   => 'IdentityFile ~/.ssh/holberton',
  match  => '^IdentityFile',
}
file_line { 'Turn off passwd auth':
    ensure => file,
path   => '/home/vagrant/.ssh/config',
path   => '/home/vagrant/.ssh/config',
line   => 'PasswordAuthentication no',
match  => '^PasswordAuthentication',
}