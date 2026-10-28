#!/usr/bin/perl
use strict;
use warnings;
use JSON::PP;

my $json = JSON::PP->new;
my ($name, $file) = ($ENV{QUERY_STRING} // '') =~ /\Aname=([A-Za-z0-9_-]+)&file=([A-Za-z0-9_-][A-Za-z0-9_.-]*)\z/;

unless (defined $name) {
    print "Status: 404 Not Found\r\n";
    print "Content-Type: application/json; charset=utf-8\r\n\r\n";
    print $json->encode({ error => 'not found' });
    exit;
}

print "Content-Type: application/json; charset=utf-8\r\n\r\n";
print $json->encode({ path => "/assets/collections/$name/$file" });
