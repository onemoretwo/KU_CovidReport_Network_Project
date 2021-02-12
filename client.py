import socket
import matplotlib.pyplot as plt
import json
import numpy as np
import time

Host = "127.0.0.1"
Port = 20300
addr = (Host, Port)

run = True

cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cli.connect((addr))

print("start client")

print("\nยินดีต้อนรับสู่โปรแกรมศูนย์ข้อมูล Covid-19 (อ้างอิงโดย กรมควบคุมโรค)")
def plot1(data,name):
    x = range(len(data))
    xtick = name
    plt.barh(x,data)
    plt.yticks(x,xtick)
    plt.show()

def plot2(data,name):
    # x = range(len(data))
    # xtick = name
    plt.pie(data,labels=name)
    plt.axis("equal")
    # plt.yticks(x,xtick)
    plt.show()

while run:
    print("เมนูหลัก : กรุณาเลือกเมนู\n\n    ( 1 ) ดูจำนวนผู้ติดเชื้อระดับจังหวัด\n    ( 2 ) ออกจากโปรแกรม\n")
    menu1 = input("เลือกเมนูที่(กรอกตัวเลขหน้าเมนู): ")
    if menu1 == "1":
        while True:
            print("เมนู : ดูจำนวนผู้ติดเชื้อระดับจังหวัด\n\n    ( 1 ) ดูจำนวนผู้ติดเชื้อทุกจังหวัด\n    ( 2 ) ดูจำนวนผู้ติดเชื้อตามจังหวัดที่ระบุ\n\n    ( 3 ) ย้อนกลับเมนูหลัก\n    ( 4 ) ออกจากโปรแกรม\n")
            menu2 = input("เลือกเมนูที่(กรอกตัวเลขหน้าเมนู): ")
            if menu2 == "1":
                cli.send("all".encode())
                data = cli.recv(4096).decode()
                print(data)

                y1 = []
                y2 = []
                j = json.loads(data)
                for i in j:
                    y1.append(j[i])
                    y2.append(i)
                plot2(y1,y2)

            elif menu2 == "2":
                province = input("ระบุจังหวัด(ภาษาอังกฤษ): ")
                cli.send(province.encode())
                data = cli.recv(4096).decode()
                if data == "No Province":
                    print("ระบุชื่อจังหวัดไม่ถูกต้อง")
                    time.sleep(1.5)
                    continue
                else:
                    print("จำนวนผู้ป่วยในจังหวัด " , province , "มีจำนวน", data)
                    time.sleep(3)
                    continue
            elif menu2 == "3":
                break
            elif menu2 == "4":
                cli.send("Exit".encode())
                run = False
                print("ออกจากโปรแกรม!")
                break
            else:
                print("ไม่มีเมนูนี้! โปรดกรอกเมนูใหม่")
                time.sleep(1.5)
                continue
    elif menu1 == "2":
        cli.send("Exit".encode())
        run = False
        print("ออกจากโปรแกรม!")
    else:
        print("ไม่มีเมนูนี้! โปรดกรอกเมนูใหม่")
        time.sleep(1.5)
        continue
cli.close()