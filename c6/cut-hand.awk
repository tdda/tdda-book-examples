BEGIN { p=1}
/"min"/ { p=0}
/"max": -/ { p=0 }
p == 1 {print $0}
{p = 1}