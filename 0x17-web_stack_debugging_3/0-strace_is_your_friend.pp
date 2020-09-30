# edits the config file

exec { 'fit_it':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php'
}
