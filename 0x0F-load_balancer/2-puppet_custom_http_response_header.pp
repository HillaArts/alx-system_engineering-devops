#!/usr/bin/env bash
#Class nginx_custom_header {
  # Ensure Nginx is installed
  package { 'nginx':
    ensure => installed,
  }

  # Fetch the hostname of the server
  $hostname = $::hostname

  # Define the custom header configuration
  $custom_header = "add_header X-Served-By '${hostname}';\n"

  # File resource to configure Nginx
  file { '/etc/nginx/conf.d/custom_header.conf':
    ensure  => file,
    content => $custom_header,
    owner   => 'root',
    group   => 'root',
    mode    => '0644',
    require => Package['nginx'], # Ensure Nginx is installed before modifying its configuration
    notify  => Service['nginx'], # Reload Nginx to apply the configuration changes
  }

  # Ensure Nginx service is running and enabled to start at boot
  service { 'nginx':
    ensure    => running,
    enable    => true,
    subscribe => File['/etc/nginx/conf.d/custom_header.conf'], # Reload Nginx if the custom configuration changes
  }
}

include nginx_custom_header

