#!/usr/bin/perl
#
# MergeWords.pl
# Usage: MergeSegWords.pl SourceFile
# 2008-09-29


#use utf8;
#use open IO => ':utf8';

# if(@ARGV!=0){
   # die "MergeSegWords.pl SourceFile\n";
# }

# my ($src, $tgt) = @ARGV;
#open(<STDIN>, $src) || die "Cannot open file: $src";

while($inline = <STDIN>){
    chomp $inline;
    $inline =~ s/^\s+//; $inline =~ s/\s+$//;
    next if ($inline eq '');
    @temp = split(/\s+/, $inline);
    for($i=0;$i<scalar(@temp); $i++ ){
      if($temp[$i] eq '<s>' || $temp[$i] eq '</s>'){ print " $temp[$i] 
";next; }
      if($temp[$i] =~ m/\d$/ && $temp[$i+1] =~ m/\./){ print 
"$temp[$i]"; next; }
      if($temp[$i] =~ m/\w$/){ print "$temp[$i] "; next; }
      print "$temp[$i]";
    }
#    print "$temp[$#temp]\n";
     print "\n";
}

close(IN);
