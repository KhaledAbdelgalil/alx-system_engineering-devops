# puppet file to fix the web debug3 problem

exec { 'Fix web debug3 problem':
  command  => 'sudo sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php'
}
