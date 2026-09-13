#!/usr/bin/perl
use strict;
use warnings;
use FindBin;
use JSON::PP;

my $json = JSON::PP->new;
my $root = "$FindBin::Bin/../../assets/collections";
my ($name) = ($ENV{QUERY_STRING} // '') =~ /\Aname=([A-Za-z0-9_-]+)\z/;

unless (defined $name && -d "$root/$name") {
    print "Status: 404 Not Found\r\n";
    print "Content-Type: application/json; charset=utf-8\r\n\r\n";
    print $json->encode({ error => 'not found' });
    exit;
}

my $dir = "$root/$name";
opendir my $dh, $dir or die "cannot open $dir: $!";
my @files = sort grep { !/\A\./ && -f "$dir/$_" } readdir $dh;
closedir $dh;

print "Content-Type: application/json; charset=utf-8\r\n\r\n";
print $json->encode([ map { { path => "/assets/collections/$name/$_" } } @files ]);
