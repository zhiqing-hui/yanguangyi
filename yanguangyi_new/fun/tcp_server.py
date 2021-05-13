import socket
import sys
import threading
import subprocess
import numpy as np
import binascii
def socket_client():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 防止socket server重启后端口被占用（socket.error: [Errno 98] Address already in use）
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('169.254.158.70', 6666))
        s.listen(10)
    except socket.error as msg:
        print(msg)
        sys.exit(1)
    print('Waiting connection...')

    while 1:
        conn, addr = s.accept()
        # 开启多线程处理客户端连接
        t = threading.Thread(target=deal_data, args=(conn, addr))
        t.start()

    # while 1:
    #     # t = threading.Thread(target=deal_data, args=s)
    # #     # 开启多线程处理客户端连接
    #     deal_data(s)
    #     t.start()
def check_date(data):
    data_header = data[0:2]
    data_tail = data[-2:]
    if data_header != "55":
        return False
    if data_tail != "a5":
        return False
    return True


def deal_data(conn, addr):
    print('Accept new connection from {0}'.format(addr))

    while 1:
        data1 = conn.recv(1024).decode('UTF-8')
        data = sixteen_to_str(data1)
        print(data)
        # print(binascii.a2b_hex(data).decode())  ####打印收到的指令
        print(check_date(data))
        if not check_date(data):
            # 如果客户端发过来的数据帧不合法，发送数据00数据给客户端，表示数据格式错误
            conn.send(bytes(str_to_sixteen('5a010700a5'), "UTF-8"))
            print("server is unconneted")
            break
        command = data[2:4]

        if command == "01":
            # 根据收到的command参数，返回指定的数据给客户端，server自己封装数据帧
            # 下面表示返回给客户端的数据为Byte4，也就是01，转换十进制为1,表示未连接
            conn.send(bytes(str_to_sixteen('5a010702a5'), "UTF-8")) ####返回已链接信号
            print("已连接")
            break
            # print("状态查询")
        elif command == "02":
            pi_cpu_id = "123"
            conn.send(bytes(str_to_sixteen('5a0207123a5'), "UTF-8"))
            print("芯片id查询"+pi_cpu_id)
            break
        elif command == "03":
            conn.send(bytes(str_to_sixteen('5a0307a5'), "UTF-8"))
            print("时钟校验")
        elif command == "04":
            result = get_caculate_result()####测量数据
            result_send = "5a040701" + result + "a5"
            result_send_sixteen = str_to_sixteen(result_send)


            conn.send(bytes(result_send_sixteen, "UTF-8"))

            break
            # print("查询测量数据")
        elif command == "05":
            result_recieve = data[6:43]
            result_sended = get_caculate_result()####测量数据
            if result_recieve == result_sended:
                result_send_true = "5a050701a5"   ####数据准确
                conn.send(bytes(str_to_sixteen(result_send_true), "UTF-8"))
            else:
                result_send_false = "5a050702a5"
                conn.send(bytes(str_to_sixteen(result_send_false), "UTF-8"))
            break
            print("比对测量数据")

        elif command == "06":
            conn.send(bytes(str_to_sixteen('5a010701a5'), "UTF-8"))
            print("查询故障代码")
        elif command == "07":
            print("获取定位数据")
        elif command == "08":
            print("验光仪测量人数给定")
        elif command == "09":
            passwd = data[6:12]
            print("设置验光仪密码为："+passwd)

        else:
            print("unknow command")
    conn.close()

def get_cpu_load():


    cmd = "top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'"
    CPU = subprocess.check_output(cmd, shell=True)
    print(CPU.decode())

def get_caculate_result():
    result_quguangdu = np.loadtxt("/home/pi/PycharmProjects/yanguangyi_new/tempfile_txt/result_quguangdu.txt")
    result_tongkong = np.loadtxt("/home/pi/PycharmProjects/yanguangyi_new/tempfile_txt/result_tongkong.txt")
    sph = str("%.2f" %(result_quguangdu[0]))
    print(len(sph))
    cyl = str("%.2f" %(result_quguangdu[1]))
    A = str("%.2f" %(result_quguangdu[2]))
    R1 = str("%.2f" %(result_tongkong[0]))
    R2 = str("%.2f" %(result_tongkong[1]))
    Axis = str("%.2f" %(result_tongkong[2]))
    str_quguangdu = rebuilt_byte(sph) + rebuilt_byte(cyl) + rebuilt_byte(A)
    str_tongkong = rebuilt_byte(R1) + rebuilt_byte(R2) + rebuilt_byte(Axis)
    str_result = str_quguangdu + str_tongkong
    print(1)

    return str_result


def sixteen_to_str(sixteen_data):
    data_str = binascii.a2b_hex(sixteen_data).decode()
    return data_str
def str_to_sixteen(str_data):
    data_sixteen = str_data.encode().hex()
    return data_sixteen

def rebuilt_byte(str):
    if len(str) == 4:
        return "00"+str
    if len(str) == 5:
        return "0"+str
    if len(str) ==6:
        return str






if __name__ == '__main__':
    socket_client()
    pass

