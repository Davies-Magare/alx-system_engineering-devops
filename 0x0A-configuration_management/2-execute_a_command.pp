#Kill a process with puppet
exec {'Kill a process':
  command  => 'pkill killmenow',
  path     => '/usr/bin',
}
