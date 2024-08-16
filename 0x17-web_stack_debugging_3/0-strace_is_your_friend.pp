#fix apache web-server using puppet

#Ensure apache2 is installed
package { 'apache2':
  ensure => installed,
}

#Ensure apache2 is running
service { 'apache2':
  ensure  => running,
  enable  => true,
  require => Package['apache2'],
}
#Ensrue the index file is avaiable

file {'/var/www/html/index.html':
  ensure  => 'present',
  content => 'Hello world',
}

