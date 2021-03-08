from selenium import webdriver
import sys
import time
from tkinter import *
from functools import partial
import tkinter as tk
import tkinter.scrolledtext as st 
from tkinter import messagebox
from tkinter.ttk import *
from selenium.webdriver.firefox.webdriver import WebDriver
class Insta:
    
    def __init__(self,link):
        tkWindow = Tk()  
        tkWindow.geometry('210x80')  
        tkWindow.title('Python-Bot')
        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                tkWindow.destroy()
                quit()
        tkWindow.protocol("WM_DELETE_WINDOW", on_closing)
        usernameLabel = Label(tkWindow, text="Username").grid(row=0, column=0)
        username = StringVar()
        usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)  
        passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)  
        password = StringVar()
        passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)  
        loginButton = Button(tkWindow, text="Login", command=tkWindow.destroy).grid(row=5, column=1)
        tkWindow.mainloop()
         #Selenium Start from here
         # You should add your path here
        driver_path = "Enter Your path here"
        self.link = link
        self.browser = webdriver.Firefox(executable_path = driver_path)
        Insta.openInstagram(self,username,password)
    
    def openInstagram(self,username,password):
        self.browser.get(self.link)
        time.sleep(2)
        Insta.login(self,username,password)
        Insta.followers(self)
        Insta.following(self)
        Insta.chose(self)

 
    def login(self,username,password):
        usernamee = self.browser.find_element_by_name("username")
        passwordd = self.browser.find_element_by_name("password")
        usernamee.send_keys(username.get())
        passwordd.send_keys(password.get())
        login_button= self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button/div").click()
        time.sleep(3)
        self.browser.get("https://www.instagram.com"+"/"+username.get()+"/")
        time.sleep(3)
  

    def scrooldown(self):
        jscommand="""
        page=document.querySelector(".isgrP");
        page.scrollTo(0,page.scrollHeight);
        var endofpage = page.scrollHeight;
        return endofpage;
        """
        endofpage = self.browser.execute_script(jscommand)
        while True:
            end = endofpage
            time.sleep(1)
            endofpage=self.browser.execute_script(jscommand)
            if end == endofpage:
                break
    

    def followers(self):
        self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a").click()
        time.sleep(4)
        Insta.scrooldown(self)
        followersl=self.browser.find_elements_by_css_selector(".FPmhX.notranslate._0imsa ")
        file = open("Followers.txt","w",encoding="UTF-8")
        for fallower in followersl:
            file.write(fallower.text+"\n")
        file.close()
        self.browser.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/button").click()
    
    def following(self):
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a").click()
        time.sleep(4)
        Insta.scrooldown(self)
        followingl=self.browser.find_elements_by_css_selector(".Jv7Aj.mArmR.MqpiF")
        file = open("following.txt","w",encoding="UTF-8")
        for fallowing in followingl:
            file.write(fallowing.text+"\n")
        file.close() 


    def compare(self):
        following =  open("following.txt", "r").read().split('\n')  
        Followers = open("Followers.txt", "r").read().split('\n')
        non_followers = open("nonfollowers.txt", "w")
        for non_follower in following:
            if non_follower not in Followers:
                non_followers.write(non_follower + '\n')
        non_followers.close()


    def unfollow(self):
            following =  open("following.txt", "r").read().split('\n')
            non_followers = open("nonfollowers.txt", "r").read().split('\n')
            i=0
            try:
                while i < len(non_followers):
                    trick = following.index(non_followers[i]) + 1
                    i+=1
                    self.browser.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/ul/div/li[{}]/div/div[2]/button".format(trick)).click()
                    self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/button[1]").click()
            except:
                windows = Tk()
                windows.title("Python-Bot")
                sto = Style()
                sto.configure('TButton', font=
                ('calibri', 10, 'bold', 'underline'),
                foreground='Green')
                tk.Label(windows,  
                    text = "Unfollowing performed successfully.",  
                    font = ("Times New Roman", 20), 
                    background = 'SteelBlue3',
                    foreground = "black").grid(column =0, 
                                    row = 0) 
                
                def on_closing():
                    if messagebox.askokcancel("Quit", "Do you want to quit?"):
                        self.browser.quit()
                        sys.exit()
                buttons = Button(windows,text =  "ok" , style='TButton' ,width=20, command=on_closing)
                buttons.grid(padx=120, pady=15)
                windows.protocol("WM_DELETE_WINDOW", on_closing)
            

    def chose(self):
        Insta.compare(self)
        window = Tk()
        non_follow = open("nonfollowers.txt", "r").read().split('\n')
        window.title("         Python-Bot")
        window.geometry("275x100")
        app = Frame(window)
        app.grid()
        
        def who():
            Insta.compare(self)
            window.destroy()
            win = tk.Tk() 
            win.title("Python-BOT")
            tk.Label(win,  
                text = "Nonfollowers:",  
                font = ("Times New Roman", 15),  
                background = 'lime green',  
                foreground = "black").grid(column = 0, 
                                    row = 0) 
            text_area = st.ScrolledText(win, 
                            width = 30,  
                            height = 8,  
                            font = ("Times New Roman", 
                                    15)) 
            text_area.grid(column = 0, pady = 10, padx = 10) 
            for i in non_follow:
                text_area.insert(tk.INSERT,"{}\n".format(i))
            text_area.configure(state ='disabled') 
            
            button1 = Button (text =  "Unfollow" , width=20, command=unfo)
            button1.grid(padx=80, pady=15)
            
            def on_closing():
                if messagebox.askokcancel("Quit", "Do you want to quit?"):
                    self.browser.quit()
                    sys.exit()   
            win.protocol("WM_DELETE_WINDOW", on_closing)
            win.mainloop() 
        def unfo():        
            Insta.unfollow(self)
            
        button1 = Button(app, text =  "Unfollow" , width=20, command=unfo)
        button1.grid(padx=80, pady=15)
        button2 = Button(app, text = "Check who are they?" , width=20, command=who)
        button2.grid(padx=80, pady=15)
        
        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                self.browser.quit()
                sys.exit()
        window.protocol("WM_DELETE_WINDOW", on_closing)
        window.mainloop()
    
