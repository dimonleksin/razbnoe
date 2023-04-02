#!/bin/bash
list=$(cat "/home/leksin/tmp/routerlist" | wc -l)
count=0
oldcount=0
for i in $(cat "/home/leksin/tmp/routerlist"); do
        a=$(nslookup $i | grep -v 10.250 | grep -oE '192\.168\.[[:digit:]]{1,3}\.254')
        for b in $(cat "/home/leksin/documents/local.txt" | grep -oE '192\.168\.[[:digit:]]{1,3}\.254'); do
                if test "$a" == "$b" 
		then 
                        let count++
			let oldcount=$count
			echo $count
			echo $oldcount
                        break 
                fi
        done

	let oldcount=$oldcount+1
	if [[ "$oldcout" != "$count" ]]
	then echo "$i"
	 fi
done
echo "$oldcount"
#echo "$list"
echo "$count"
