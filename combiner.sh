#!/bin/bash
# It takes in one argument --- filename(with full path) of the objective spoken language # text.

segtext=`echo $1 | java -jar ./segmenter/ChiUtf8Segmenter.jar -mode5 consolemode ./segmenter/100k_wordprobmap `


result=`echo $segtext |  python ./transduce.py | perl ./mergeWord.pl `

echo $result

# result=`echo $segtext |  python ./transduce.py | sed 's/\s*//g'| tee "$1.rewriteByRule" `
