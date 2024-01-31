#!/usr/bin/env ruby
# A regular expression that mathing must be capital letters
puts ARGV[0].scan([A-Z]).join
