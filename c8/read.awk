BEGIN { p=0 }
/^# end-read$/ { p=0 }
p==1 { print $0}
/^# read$/ { p=1 }


