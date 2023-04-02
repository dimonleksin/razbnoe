

IFS='\n'
for i in $(cat ml.txt)
do
	m = $(echo $i|awk {'print$1'})
	p = $(echo $i|awk {'print$2'})
	/usr/local/bin/gmvault sync $m@saratovcafe.ru --type quick -c no -d /srv/gmail/$m -p >> /var/log/gmvault.log 2>&1
	gmvault export -t offlineimap -d /srv/gmail/$m/ /tmp/$m
	mv /tmp/Inbox/ /tmp/INBOX/
	cat "# Sample minimal config file.  Copy this to ~/.offlineimaprc and edit to\\n# get started fast.\\n\\n[general]\\naccounts = $m\\n\\n[Account $m]\\nlocalrepository = Gmvault\\nremoterepository = iRedMail\\n\\n[Repository Gmvault]\\ntype = Maildir\\nlocalfolders = /tmp/$m\\n\\n[Repository iRedMail]\\ntype = IMAP\\nremotehost = 192.168.10.115\\nremoteuser = $m@saratovcafe.ru\\nremotepass = $p\\nssl = no\\nsslcacertfile = /etc/ssl/certs/ca-certificates.crt" > .$m	
	offlineimap -c .$m
	rm -rf /tmp/$m
done
