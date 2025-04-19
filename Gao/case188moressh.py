#! /bin/python3
import paramiko,time,csv,threading,os
filepath="/home/user.csv"
h3c_Command="/home/h3c.txt"
hw_Command="/home/hw.txt"
cisco_Command="/home/cisco.txt"
sem=threading.Semaphore(4) #线程并发
date=time.strftime("%Y年%m月%d日")
txt=[ h3c_Command,hw_Command,cisco_Command ]
os.system(" touch /home/hw.txt & touch /home/h3c.txt & touch /home/cisco.txt")
filename="/home/"+date
f = open(filepath)
reader = csv.reader(f)
try:
    os.mkdir(filename)
except:
    print(filename,"文件夹已被创建!")

def user():
    f = open(filepath)
    next(f)
    print("登录以下设备:")
    for i in f:
        i=i[:-1]
        ip,type = i.split(',')[0],i.split(',')[4]
        print("Device_IP:%s Device_Type:%s" %(ip,type,))
    else:
        f.close()
        time.sleep(3) 
        ssh()

def sshlogin(host_ip, host_port, user, password,savepath,type):
    with sem:        
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(host_ip, host_port, user, password)
            shell = ssh.invoke_shell()         
            if type == "h3c":
                h3c = open(h3c_Command)
                for line in h3c:
                    time.sleep(1)
                    shell.send(line[:-1]+"\n")
                    print("Command_type:h3c 主机:h3c",host_ip,"开始执行:",line[:-1],time.asctime( time.localtime(time.time()) ))
                else:
                    h3c.close()
            elif type == "hw":
                hw=open(hw_Command)
                for line in hw:
                    time.sleep(1)
                    shell.send(line[:-1]+"\n")
                    print("Command_type:hw 主机:hw",host_ip,"开始执行:",line[:-1],time.asctime( time.localtime(time.time()) ))
                else:
                    hw.close()
            elif type == "cisco":
                cisco=open(cisco_Command)
                for line in cisco:
                    time.sleep(1)
                    shell.send(line[:-1]+"\n")
                    print("Command_type:Cisco 主机:Cisco",host_ip,"开始执行:",line[:-1],time.asctime( time.localtime(time.time()) ))
                else:
                    cisco.close() 
            print("开始回收操作日志: %s Wait...." %(host_ip))
            time.sleep(7)
            data = shell.recv(655350)
            conf = open(savepath,"wb")
            conf.write(data)
            conf.close
            ssh.close
            print("主机",host_ip,"执行完毕！","Time:",time.asctime( time.localtime(time.time()) ))
        except:
            print("主机:%s 登录失败" %(host_ip))

def ssh():
    for i,row in enumerate(reader):
        if i == 0:
            pass
        else:
            host_ip,host_port,user,password,type = row[0],row[1],row[2],row[3],row[4]
            savepath=filename+"/"+date+host_ip+".txt"
            print("开始登录:%s" %(host_ip),time.asctime( time.localtime(time.time()) ))
            t1 = threading.Thread(target=sshlogin,args=(host_ip,host_port,user,password,savepath,type,)) 
            t1.start()
for txt1 in txt:
    if "h3c" in txt1:    
        print('\nH3C-Command如下:')
    elif "cisco" in txt1:
        print('\nCisco-Command如下:')
    elif 'hw' in txt1 :
        print('\nHuaWei-Command如下:')
    for command in open(txt1):
        if 'h3c' in txt1:
            if len(command) != 0:
                if command[:-2] not in "reboot":
                    print("h3c_Command:%s" %(command[:-1]))
                else:
                    key = "Key"
            else:
                print("h3c_Command为空")
        elif 'hw' in txt1:
            if len(command) != 0:
                if command[:-2] not in  "reboot":
                    print("hw_Command:%s" %(command[:-1]))
                else:
                    key = "Key"
            else:
                print("hw_Command为空")
        elif 'cisco' in txt1:
            if len(command) != 0:
                if command[:-2] not in "reload":
                    print("cisco_Command:%s" %(command[:-1]))
                else:
                    key = "Key"
            else:
                print("hw_Command为空")
        else:
            print("None")
    else:
        open(txt1).close()
if key == "Key":
    keyword = input('可能存在重启设备命令，是否执行![Y/N]')
    if keyword == "Y" or keyword == "y":
        print('Start!!')
        user()
    else:
        pass
else:
    print('Start!!')

