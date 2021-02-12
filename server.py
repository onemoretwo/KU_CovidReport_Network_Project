from socket import *
import requests
import json

HOST = '127.0.0.1'   # or 127.0.0.1 or localhost
PORT = 20300
ADDR = (HOST,PORT)
BUFFER = 4096

srv = socket(AF_INET,SOCK_STREAM)

#bind socket to address
srv.bind((ADDR))	#double parens create a tuple with one object
srv.listen(1) # maximum queued connections is 1
print("Server is ready")

def getCovidData(province = "all"):
    api = "https://covid19.th-stat.com/api/open/cases/sum"
    response = requests.get(api)
    print(response.status_code)
    jobj = json.loads(json.dumps(response.json(), sort_keys=True, indent=4))

    for key in jobj:
        if key == "Province":
            allprovince = jobj[key]
            break
    
    if province == "all":
        return json.dumps(allprovince, sort_keys=True, indent=4)
    else:
        check = False
        for key in allprovince:
            if key == province:
                search = allprovince[key]
                check = True
                break
        if check == False:
            return "No Province"
        else:
            return search

while True:
    conn,addr = srv.accept() #accepts the connection
    print('...connected by', addr)
     
    province = conn.recv(BUFFER).decode()
    print(province)
    data = getCovidData(province)
    conn.send(str(data).encode())
    
    # if(province == "end"):
    #     conn.close()
    conn.close()