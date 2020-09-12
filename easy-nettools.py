import sys
import socket
import requests
import platform
import urllib.request
import json
import webbrowser
import speedtest
from pythonping import ping
ip=requests.get("https://ramziv.com/ip").text
url="https://ipinfo.io/"+ip+"/json"
getinfo=urllib.request.urlopen(url)
ipinfo=json.load(getinfo)
openports={}
ports={21:"ftp",22:"ssh",23:"telnet",25:"smtp",43:"whois",53:"dns",68:"dhcp",
       80:"http",110:"pop3",115:"sftp",119:"nntp",123:"ntp",139:"netbios",
       143:"imap",161:"snmp",179:"bgp",220:"imap3",389:"ldap",443:"https",
       993:"imaps",1723:"pptp",2049:"nfs",3306:"mysql",3389:"rdp",5060:"sip",8080:"http-alt"}
def getlip(): #Returns the ip device in the local network
    return socket.gethostbyname(socket.getfqdn())
def getgip(): #Returns the device ip in The Internet
    return ip
def osname(): #Returns the OS of device
    return platform.platform()
def city():
    #Returns the city name of device
    return ipinfo['city']
def region():#Returns the city of device
    return ipinfo['region']
def country():#Returns the country abbreviation of device
    return ipinfo['country']
def timezone(): #Return the timezone of device
    return ipinfo['timezone']
class location():
    def map(): #Opens the Google Maps page by coordinates
        webbrowser.open('https://www.google.com/maps/@'+ipinfo['loc'], new=2)

    def cds(): #Returns the coordinates of location
        print( ipinfo['loc'])
class speed():
    def download(): #Returns the download speed
        test = speedtest.Speedtest()
        return (test.download()/1024/1024)
    def upload(): #Returns the upload speed
        test = speedtest.Speedtest()
        return (test.upload()/1024/1024)
def get(ip): #Connects to the site by the link and returns the status of the request
    response=requests.get(ip).status_code
    if response==200:
        return "OK"
    elif response==403:
        return "Forbidden"
    elif response==404:
        return "Not Found"
    elif response==408:
        return "Request Timeout"
    elif response==500:
        return "Internal Server Error"
    elif reponse==504:
        return "Gateway Timeout"
    elif response==522:
        return "Connection Timed Out"
def scanport(ip,port): #Scans the port that you typed
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.01)
    try:
        sock.connect((ip,port))
    except:
        return False #If port is open
    else:
        return True  #If port is closed  
def scanports(ip): #Scans the most popular ports
    openports={}
    for port,name in ports.items():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.01)
        try:
            sock.connect((ip,port))
        except:
            pass
        else:
            openports.update({port:name}) #openports contains opened ports and their names
    return openports
    
