import subprocess
passwrd = 'vvgio9it'
with open('/home/d_leksin/Документы/mitv_lst.txt', 'r') as hosts_list_txt:
    hosts_list_arr = [i for i in hosts_list_txt]
for host in hosts_list_arr:
    if not ' -' in host:
        print(host[7:-7] + '5555')
  #  host_new = host.replace('a', 'k')
        subprocess.run(['adb', 'connect', host[7:-7] + '5555'])