#!/bin/bash
#set -x 
hosts_list=$1
#new_video=$2
#p=$3 #количество потоков
lst=$(cat $hosts_list | awk -F@ {'print $2'}|awk -F: {'print $1'}) #список хостов только IP

#загрузка ролика по списку в указанное количество потоков

#paralle-rsync -p $p -h $hosts_list $new_video  /storage/emulated/0/Download/.video

#Удалене старого видоса

#parallel-ssh -h $hosts_list "cd /storage/emulated/0/Download/.video && ls | grep -v $new_video | xargs rm -r"

#ребут теликов по списку

for unit in $lst
do
    adb connect "$unit:5555"
    echo "reboot" | adb shell &
    sleep 1
    adb disconnect
done
