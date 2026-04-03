BEGIN { p=0 }
/^def generate_dataframe.*:$/ { p=1 }
p==1 { print $0 }

