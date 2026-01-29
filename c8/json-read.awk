BEGIN { p=0 }
/^# end-json-read$/ { p=0 }
p==1 { print $0}
/^# json-read$/ { p=1 }


