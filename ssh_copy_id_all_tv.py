import subprocess
passwrd = 'vvgio9it'
with open('/home/leksin/Документы/mitv_lst_for_script.txt', 'r') as host_list:
    host_list_arr = ['u0_k45' + i[6:] for i in host_list]
for host in host_list_arr:
    subprocess.Popen(['sshpass', '-p', passwrd, 'ssh-copy-id', '-f', '-p', '8022', host])
