import serial
import serial.tools.list_ports

'''
author：     王海峰 plutohfw@gmail.com
创建时间:     2023/6/14
最后维护时间: 2023/6/14
'''
def serial_ports(): #自动寻找端口
    ports = list(serial.tools.list_ports.comports())  
    for port_no, description, address in ports:
        if 'USB' in description:
            return port_no
        
print(serial_ports())
class servo(): #对象化伺服
    def __init__(self):
        self.port = serial_ports()
         # 串口设备路径，多个设备容易混乱，如需手动输入注意，格式 liunx下 如 '/dev/ttyUSB0'，并且需要允许调用串口 sudo chmod 666 /dev/ttyUSB0
         #windos下为 如 'COM3'
        self.baud_rate = 115200  # 波特率
        self.timeout = 1  # 超时时间（单位：秒）
    def cmd(self,comd):
        ser = serial.Serial(self.port, self.baud_rate, timeout=self.timeout)  # 打开串口连接
        if ser.is_open:
            print("成功打开串口")

            # 发送数据
            command = f'{comd}\r'.encode()  # 发送的命令（以字节形式表示）
            ser.write(command)

            # 读取响应
            response = ser.read(100)  # 读取指定数量的字节数据（100为示例值）
            print("收到的响应数据:", response)

            # 关闭串口连接
            ser.close()
        else:
            print("无法打开串口")
servo=servo()

servo.cmd('en') #使能
servo.cmd('homecmd')#回零
servo.cmd('moveinc 10000000 1000') #注意那什么比来着，第一个是圈数要除转动比，第二参数个是速度
servo.cmd('stop') # 停止
servo.cmd('k') #下使能
'''
更多命令自行联系Servotronix
'''