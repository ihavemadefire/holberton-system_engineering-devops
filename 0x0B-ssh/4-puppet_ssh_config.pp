# Sets up config file


file_line { 'Turn off passwd auth':
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/holberton',
}
file_line { 'Turn off passwd auth':
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
}