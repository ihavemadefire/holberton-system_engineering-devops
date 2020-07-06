#!/usr/bin/env ruby
a = ARGV[0].scan(/((?<=from:))([a-zA-Z0-9\-+ :]*)/).join()
b = ARGV[0].scan(/((?<=to:))([a-zA-Z0-9\-+ :]*)/).join()
c = ARGV[0].scan(/((?<=flags:))([a-zA-Z0-9\-+ :]*)/).join()
puts a+","+b+","+c
