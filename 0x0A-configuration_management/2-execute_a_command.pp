# kill a process

exec { 'kill_killmenow_process':
  command     => 'pkill killmenow',
  refreshonly => true,
  onlyif      => 'pgrep killmenow',
  logoutput   => true,
}
