# coding = UTF-8
# -*- coding: UTF-8 -*-
from selenium import webdriver
import os
os.system('clear')

print("""


         ██████╗ ██████╗ ███╗   ██╗ █████╗ ███╗   ██╗
        ██╔════╝██╔═══██╗████╗  ██║██╔══██╗████╗  ██║
        ██║     ██║   ██║██╔██╗ ██║███████║██╔██╗ ██║
        ██║     ██║   ██║██║╚██╗██║██╔══██║██║╚██╗██║
        ╚██████╗╚██████╔╝██║ ╚████║██║  ██║██║ ╚████║
         ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═══╝



""")
urlsfile=open('urls.txt','r')
demo=open("demo.txt","w+")
for url in urlsfile:
       try:
            if "https://" in url :
                url = url
            else :
                url = "https://"+url

            browser = webdriver.Firefox()
            browser.get(url)
            src = browser.page_source
            if (("Demo") or ("demo")) in src :
                print(' [!]Demo ==> ',url)
                demo= open("demo.txt","a")
                demo.write(url)
                demo.close()
            elif (("Register") or ("register")) in src :
                print(' [!]Sign up ==> ',url)
                signup= open("signup.txt","a")
                signup.write(url)
                signup.close()
            elif (("Sign Up") or ("Sign up")) in src :
                print(' [!]Sign up ==> ',url)
                signup= open("signup.txt","a")
                signup.write(url)
                signup.close()
            elif (("Regístrate") or ("regístrate")) in src :
                print(' [!]Sign up ==> ',url)
                signup= open("signup.txt","a")
                signup.write(url)
                signup.close()
            elif (("Start Free Trial") or ("start free trial")) in src :
                print(' [!]Sign up ==> ',url)
                signup= open("signup.txt","a")
                signup.write(url)
                signup.close()
            elif (("free trial") or ("Free Trial")) in src :
                print(' [!]Sign up ==> ',url)
                signup= open("signup.txt","a")
                signup.write(url)
                signup.close()
            elif (("freetrial") or ("free-trial")) in src :
                print(' [!]Sign up ==> ',url)
                signup= open("signup.txt","a")
                signup.write(url)
                signup.close()
            elif (("Try For Free") or ("try for free")) in src :
                print(' [!]Sign up ==> ',url)
                signup= open("signup.txt","a")
                signup.write(url)
                signup.close()
            elif (("SIGN UP") or ("SIGN-UP")) in src :
                print('\033[0;33m[!]Sign up ==> ',url)
                signup= open("signup.txt","a")
                signup.write(url)
                signup.close()
            elif (("cart") or ("Cart")) in src :
                print(' [!]Sign up ==> ',url)
                signup= open("signup.txt","a")
                signup.write(url)
                signup.close()
            elif (("signup") or ("sign-up")) in src :
                print(' [!]Sign up ==> ',url)
                signup= open("signup.txt","a")
                signup.write(url)
                signup.close()
            elif (("Become a Member") or ("become a member")) in src :
                print(' [!]Sign up ==> ',url)
                signup= open("signup.txt","a")
                signup.write(url)
                signup.close()
            elif (("Create account") or ("create account")) in src :
                print(' [!]Sign up ==> ',url)
                signup= open("signup.txt","a")
                signup.write(url)
                signup.close()
            elif (("Create") or ("create")) in src :
                print(' [!]Sign up ==> ',url)
                signup= open("signup.txt","a")
                signup.write(url)
                signup.close()
            elif (("Refer") or ("refer")) in src :
                print(' [!]Sign up ==> ',url)
                signup= open("signup.txt","a")
                signup.write(url)
                signup.close()
            elif (("Get $15") or ("get $15")) in src :
                print(' [!]Sign up ==> ',url)
                signup= open("signup.txt","a")
                signup.write(url)
                signup.close()
            elif (("Get Started") or ("get started")) in src :
                print(' [!]Sign up ==> ',url)
                signup= open("signup.txt","a")
                signup.write(url)
                signup.close()
            elif (("free trial") or ("Free Trial")) in src :
                print(' [!]Sign up ==> ',url)
                signup= open("signup.txt","a")
                signup.write(url)
                signup.close()
            elif (("freetrial") or ("FreeTrial")) in src :
                print(' [!]Sign up ==> ',url)
                signup= open("signup.txt","a")
                signup.write(url)
                signup.close()
            elif (("Accedi") or ("accedi")) in src :
                print('\033[0;33m[[!]Sign up ==> ',url)
                signup= open("signup.txt","a")
                signup.write(url)
                signup.close()
            elif (("get-started") or ("Get-Started")) in src :
                print(' [!]Sign up ==> ',url)
                signup= open("signup.txt","a")
                signup.write(url)
                signup.close()
            elif (("Start Saving") or ("start saving")) in src :
                print(' [[!]Sign up ==> ',url)
                signup= open("signup.txt","a")
                signup.write(url)
                signup.close()
            elif (("JOIN NOW") or ("join now")) in src :
                print(' [[!]Sign up ==> ',url)
                signup= open("signup.txt","a")
                signup.write(url)
                signup.close()
            elif (("Shop Now") or ("shop now")) in src :
                print(' [[!]Sign up ==> ',url)
                signup= open("signup.txt","a")
                signup.write(url)
                signup.close()
            elif (("Join now") or ("Join Now")) in src :
                print(' [!]Sign up ==> ',url)
                signup= open("signup.txt","a")
                signup.write(url)
                signup.close()
            elif (("START NOW") or ("start now")) in src :
                print(' [!]Sign up ==> ',url)
                signup= open("signup.txt","a")
                signup.write(url)
                signup.close()
            elif (("START-NOW") or ("start-now")) in src :
                print(' [!]Sign up ==> ',url)
                signup= open("signup.txt","a")
                signup.write(url)
                signup.close()
            elif (("/users/sign_up") or ("users/sign_up")) in src :
                print(' [!]Sign up ==> ',url)
                signup= open("signup.txt","a")
                signup.write(url)
                signup.close()
            elif (("sign_up") or ("Sign_Up")) in src :
                print(' [!]Sign up ==> ',url)
                signup= open("signup.txt","a")
                signup.write(url)
                signup.close()
            elif (("quickactivate") or ("quick-activate")) in src :
                print(' [!]Sign up ==> ',url)
                signup= open("signup.txt","a")
                signup.write(url)
                signup.close()
            elif (("Quick Activate") or ("QUICK-ACTIVATE")) in src :
                print(' [!]Sign up ==> ',url)
                signup= open("signup.txt","a")
                signup.write(url)
                signup.close()
            else:
                print(" [+] Demo ==> ",url)
                demo= open("demo.txt","a")
                demo.write(url)
                demo.close()
            browser.close()
       except:
             print('[!] this  url is not working !!  ==> ',url)
             browser.close()
