BEGIN { p=0 }
/^    }$/ { p=0 }
p==1 { print $0 }
p==0 && (/"fields"/) { p=1 }
