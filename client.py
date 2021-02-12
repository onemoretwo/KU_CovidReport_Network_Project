import socket

Host = "127.0.0.1"
Port = 20300
addr = (Host, Port)

cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cli.connect((addr))

print("start client")

print("\nยินดีต้อนรับสู่โปรแกรมศูนย์ข้อมูล Covid-19 (อ้างอิงโดย กรมควบคุมโรค)")

while True:
    print("เมนูหลัก : กรุณาเลือกเมนู\n    ( 1 ) ดูจำนวนผู้ติดเชื้อระดับจังหวัด\n    ( 2 ) ออกจากโปรแกรม")
    menu1 = input("เลือกเมนูที่: ")
    if menu1 == "1":
        while True:
            print("เมนู : ดูจำนวนผู้ติดเชื้อระดับจังหวัด\n    ( 1 ) ดูจำนวนผู้ติดเชื้อทุกจังหวัด\n    ( 2 ) ดูจำนวนผู้ติดเชื้อตามจังหวัดที่ระบุ\n\n    ( 3 ) ย้อนกลับเมนูหลัก\n    ( 4 ) ออกจากโปรแกรม")
            menu2 = input("เลือกเมนูที่: ")
            if menu2 == "1":
                cli.send("all".encode())
                data = cli.recv(4096).decode()
                print(data)
            elif menu2 == "2":
                province = input("ระบุจังหวัด(ภาษาอังกฤษ): ")
                cli.send(province.encode())
                data = cli.recv(4096).decode()
                if data == "No Province":
                    print("ไม่มีจังหวัดนี้ โปรดระบุชื่อจังหวัดใหม่")
                else:
                    print("จำนวนผู้ป่วยในจังหวัด " , province , "มีจำนวน", data)
            else:
                print("ไม่มีเมนูนี้!")
                continue
    elif menu1 == "2":
        print("ออกจากโปรแกรม!")
        break
cli.close()