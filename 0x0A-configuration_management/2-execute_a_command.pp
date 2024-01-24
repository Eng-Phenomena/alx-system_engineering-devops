#kill proccess
exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
