import subprocess
import paramiko

def i():
    with open('/home/d_leksin/mitv_lst_for_script.txt', 'r') as hosts_list_txt:
        hosts_list_arr = [i for i in hosts_list_txt]
    for host in hosts_list_arr:
        subprocess.Popen(['ssh', '-p', '8022', host], stdin=subprocess.PIPE, stdout=subprocess.PIPE).wait()
        subprocess.communicate(input='cat > start_sshd<<EOF')
        subprocess.communicate(input='#!/data/data/com.termux/files/usr/bin/sh')
        subprocess.communicate(input='termux-wake-lock')
        subprocess.communicate(input='sshd')
        subprocess.communicate(input='ls -d /sdcard/Download/.video/* > /sdcard/Download/playlist.m3u')
        subprocess.communicate(input='EOF')



client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('192.168.40.182', port=8022, username='u0_k45', password='vvgio9it')
stdin, stdout, stderr = client.exec_command('cd .termux/boot/;cat > start_sshd<<EOF;#!/data/data/com.termux/files/usr/bin/sh;termux-wake-lock;sshd;ls -d /sdcard/Download/.video/* > /sdcard/Download/playlist.m3u;EOF')
data = stdout.read() + stderr.read()
client.close()
