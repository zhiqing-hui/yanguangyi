import socket
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# tcp_socket = socket.socket()
server_addr = ("192.168.1.113", 22)
tcp_socket.connect(server_addr)
while True:
   try:
     send_data = input("请输入：")
     tcp_socket.send(send_data.encode("utf-8"))
     data_r = tcp_socket.recv(1024).decode('utf-8')
     print("返回值是：", data_r)
   except:
     tcp_socket.close()