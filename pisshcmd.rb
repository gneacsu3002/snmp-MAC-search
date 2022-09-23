#!/usr/bin/env ruby
require 'net/ssh'

@hostname = "192.168.28.119"
@username = "pi"
@password = "raspberry"

@username = ARGV[0]
@hostname = ARGV[1]
@password = ARGV[2]
@cmd = ARGV[3]

begin
  ssh = Net::SSH.start(@hostname, @username, :password => @password)
  res = ssh.exec!(@cmd)
  ssh.close
  puts res
rescue
  puts "Unable to connect to #{@hostname} using #{@username}/#{@password}"
end 

