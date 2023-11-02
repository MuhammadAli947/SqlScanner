import requests
from colorama import Fore, Style
from colorama import init
from termcolor import colored

init()
VulnerableParams = []


                                             
burp0_url =  >
burp0_cookies =  >
burp0_headers = >            just copy the request from burp using the extention export to python request and paste it here.
burp0_data = >



print("**********************************************************************")
for param in burp0_data:
    OriginlValue = burp0_data[param]
    burp0_data[param] = burp0_data[param] + "'"
    payloadValue = burp0_data[param]
    Response = requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)
    burp0_data[param] = OriginlValue
    print(colored('[+] Testing', 'yellow', attrs=['bold']))
    #print(text,payloadValue)
    if(str(Response.status_code).__contains__("5")) or Response.status_code == 500 or Response.text.__contains__("Database"):
        print("**********************************************************************")
        print(burp0_url)
        VulnerableParams.append(str(param))
        print(colored('[+] ' + param + ' is SQL Injection Vulnerable', 'red', attrs=['bold']))
        print(Response.status_code)
        #print(Response.text)
        print("**********************************************************************")
    else:
        print(colored('[+] '+ param+' is not Vulnerable', 'green', attrs=['bold']))
        
print(colored('[+] SQL Injection Vulnerable Params are: ', 'yellow', attrs=['bold'])) 
print(burp0_url)       
for i in VulnerableParams:
    
    print(colored(i, 'red', attrs=['bold']))

    #print(param," is not Vulnerable")
