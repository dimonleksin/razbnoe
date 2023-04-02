import subprocess

#хост тест
host = 'u0_k45@192.168.10.194:8022'
object_to_upload = '/home/d_leksin/video/outS.mp4'

#посылаем команду в консоль
def on_host(host, object_to_upload):
    parallel_rsync = ['parallel-rsync', '-v', '-p', '1', '-H', host, object_to_upload, '/storage/emulated/0/Download']
    adb_conn = ['adb', 'connect', host[7:-4] + '5555']
    adb_shell = ['adb', '-s', host[7:-5], 'shell']
    mv_video = 'mv storage/emulated/0/Download/outS.mp4 storage/emulated/0/Download/.video/'
    reb = 'reboot'
    subprocess.Popen(parallel_rsync, stdout=subprocess.PIPE).wait()
    subprocess.Popen(adb_conn, stdout=subprocess.PIPE).wait()
    process_shell = subprocess.Popen(adb_shell, stdout=subprocess.PIPE, stdin=subprocess.PIPE).wait()
    process_shell.communicate(input=mv_video.encode())[0]
    process_shell.communicate(input=reb.encode())[0]
    subprocess.Popen(['adb', 'disconnect'])

def all_hosts(object_to_upload):
    addr_hosts_list = '/home/leksin/mitv_lst_for_delete_video.txt'
    with open(addr_hosts_list, 'r') as hosts_list_txt:
        hosts_list_arr = [i for i in hosts_list_txt]
    #parallel_rsync = ['parallel-rsync', '-v', '-p', '5', '-h', addr_hosts_list, object_to_upload, '/storage/emulated/0/Download']
    #process = subprocess.Popen(parallel_rsync, stdout=subprocess.PIPE)
    #process.wait()

    #цикл для ребута всех теликов
    for host in hosts_list_arr:
        if not ' -' in host:      #если у адреса в списке хостов стоит -, его не брать
            adb_conn = ['adb', 'connect', host[7:-4] + '5555']
            adb_shell = ['adb', '-s', host[7:-5], 'shell']
            #mv_video = 'mv storage/emulated/0/Download/outS.mp4 storage/emulated/0/Download/.video/'
            reb = 'reboot'
            #subprocess.Popen(parallel_rsync, stdout=subprocess.PIPE).wait()
            subprocess.Popen(adb_conn, stdout=subprocess.PIPE).wait()
            process_shell = subprocess.Popen(adb_shell, stdout=subprocess.PIPE, stdin=subprocess.PIPE).wait()
            #process_shell.communicate(input=mv_video.encode())[0]
            process_shell.communicate(input=reb.encode())
            subprocess.Popen(['adb', 'disconnect'])

all_hosts(object_to_upload)