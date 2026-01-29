BEGIN { p=0 }
/^# end-write$/ { p=0 }
p==1 { print $0}
/^# write$/ { p=1 }


