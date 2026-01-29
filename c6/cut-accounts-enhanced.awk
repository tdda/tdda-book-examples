BEGIN { p=1 }
/"creation_metadata"/ { p=-1 }
/"account_number"/ { p=0 }
/"no_tel"/ { p=1 }
/"fields":/ { p=1 }
p>0 { print $0 }
p==-1 && (/"}"/) { p=1 }


