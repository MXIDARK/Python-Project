import requests
import smtplib
import json


from tkinter import *
import tkinter.messagebox
from tkinter import simpledialog

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "1cf868802b6545909bd990752e217368"

my_email = "python.news.project@gmail.com"
password = "iuhaexlvbvspffsl"

connection = smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login(user=my_email , password= password)

root = tkinter.Tk()
root.title("News App")

def onClick():

    input = news_input.get()
    if input == "":
        tkinter.messagebox.showinfo("Warning",  message="Please type something First")
    else:
        news_params = {
            "apiKey": NEWS_API_KEY,
            "q": input,
            
        }
        message =""
        news_response = requests.get(NEWS_ENDPOINT, params= news_params)    
        articles = news_response.json()["articles"]

        with open("data.json","w") as data_file:
            json.dump(news_response.json(),data_file, indent = 4)
        str1=""
        str2=""
        str3=""
        three_articles = articles[:3]
        for article in three_articles:
            str1 =article["title"]
            title_i = article["title"].encode("ascii", "ignore")
            title_f = title_i.decode()
            dec_i = article["description"].encode("ascii", "ignore")
            dec_f = dec_i.decode()
            url_i = article["url"].encode("ascii", "ignore")
            url_f = url_i.decode()
            str3 = str3+str2
            message = message + title_f+"\n" + dec_f +"\n"+ url_f+"\n\n"
        output.configure(state = 'normal')
        output.delete(1.0,END)
        output.insert(END,message)
        output.configure(state = 'disable')
        news_box = tkinter.messagebox.askyesno(title="NEWS", message=f"{message}\n\n Do you want it on mail")
        
        email_input =""
        if news_box:
            email_input = simpledialog.askstring("email input","please enter you email address")
            if not email_input:
                tkinter.messagebox.showinfo("Okay",  message="Looks like no email ID was provided")
            else:
                connection.sendmail(from_addr=my_email, to_addrs= email_input,msg=f"Subject:{input}\n\n {message}")
                print("mail sent")
                tkinter.messagebox.showinfo("Yayyyyy",  message="Mail Sent")

news_input = Entry(width = 50)
news_input.grid(column=1, row=2)
news_input.focus()

button = Button(root, text="SEARCH", command=onClick, height=2, width=10, bg="coral1", font="bold")
button.grid(column=1 , row = 3)



bg_color = "orange2"
title = Label(root, text="Type to get News", font=("times new roman", 30, "bold"),pady=2, bd=12, relief=GROOVE, bg="coral1", fg="black")
title.grid(column=1,row=0)

news_title = Label(root,text="News Area", font=("times new roman", 20, "bold"), bd=7, relief=GROOVE,width =40)
news_title.grid(column =1 ,row =4,columnspan=3)
output = Text(root, height = 20,width = 80,bg = "pink",padx =15,state = 'disable',wrap = 'word')
output.grid(column=1,row=5)

root.title('PythonGuides')
root.config(bg='misty rose')




root.mainloop()
