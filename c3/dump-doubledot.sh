echo "$ grep 'Above +' doubledot.py | python byteseq.py | head -1" > doubledot-hexdump.txt
grep 'Above +' doubledot.py | python byteseq.py | head -1 >> doubledot-hexdump.txt
echo '' >> doubledot-hexdump.txt
echo "$ grep 'Below +' doubledot.py | python byteseq.py | head -1" >> doubledot-hexdump.txt
grep 'Below +' doubledot.py | python byteseq.py | head -1 >> doubledot-hexdump.txt
python ../texify.py doubledot-hexdump.txt
