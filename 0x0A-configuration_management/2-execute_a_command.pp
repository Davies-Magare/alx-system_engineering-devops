#This script kills a process
exec { 'kill_process':
  command => 'pkill killmenow',
  path    => '/usr/bin'
}
