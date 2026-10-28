#!/usr/bin/perl
use strict;
use warnings;

print "Content-Type: text/plain; charset=utf-8\r\n\r\n";
print $ENV{QUERY_STRING} // '', "\n";
