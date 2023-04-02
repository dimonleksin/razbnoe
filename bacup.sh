#!/bin/bash
#set -x
#Список каталогов для бэкапа
srclst=$(ls -d /home/leksin/*|grep .txt && echo "/home/leksin/documents" && echo "/home/leksin/.ssh" && echo "/home/leksin/.android" && echo "/home/leksin/openwrt/backups")
scrbac="/home/leksin/tmp/backups" 
#echo $srclst
#копируем все файлы в один каталог
for i in $srclst
do
	cp -r "$i" "$scrbac/"
done
#создаем список установленных пакетов
dpkg --get-selections | awk {'print$1'} >> "$scrbac/dpkg_lst"
#переименуем скрытые каталоги
mv "$scrbac/.android" "$scrbac/android"
mv "$scrbac/.ssh" "$scrbac/ssh" 			#.$(echo $i|awk -F/ {'print $3'}) $scrbac/ssh
tar -cvzf backup.tar.gz $scrbac #запаковываем в архив то, что будем шифровать
lst=$(ls -d $scrbac/*)
#удаляем то, что уже запаковали в архив
for n in $lst
do
	rm -r "$n"
done
#шифруем с парольной фразой
gpg -c backup.tar.gz 
rm -r backup.tar.gz #удаляем архив, т.к. уже есть его шированная версия
sshpass -p dileefxu rsync -av --progress -e "ssh" backup.tar.gz.gpg root@pasiphae.vpn:/srv/ftpuser/tmp/leksin/backup/ #отправляем архив на сервер
rm -r backup.tar.gz.gpg #удаляем шифрованный архив
#set +x
