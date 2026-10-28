#!/usr/bin/perl
use strict;
use warnings;
use FindBin;
use Digest::SHA;
use JSON::PP;

my $json = JSON::PP->new->canonical;
my $root = "$FindBin::Bin/../../../assets/collections";
my ($name, $file) = ($ENV{QUERY_STRING} // '') =~ /\Aname=([A-Za-z0-9_-]+)&file=([A-Za-z0-9_-][A-Za-z0-9_.-]*)\z/;

unless (defined $name && -f "$root/$name/$file") {
    print "Status: 404 Not Found\r\n";
    print "Content-Type: application/json; charset=utf-8\r\n\r\n";
    print $json->encode({ error => 'not found' });
    exit;
}

my $sha256 = Digest::SHA->new(256)->addfile("$root/$name/$file", 'b')->hexdigest;

print "Content-Type: application/json; charset=utf-8\r\n\r\n";
print $json->encode({ path => "/assets/collections/$name/$file", sha256 => $sha256 });
