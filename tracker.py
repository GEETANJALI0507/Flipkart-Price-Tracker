import requests as requests
import bs4
import smtplib
import time

#async def main():
headers = {"user_agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36"}
url ='https://www.flipkart.com/samsung-galaxy-a12-white-128-gb/p/itmc983691e03a7d?pid=MOBGYCCGGPXZHSWB&lid=LSTMOBGYCCGGPXZHSWBTXDFJB&marketplace=FLIPKART&store=tyy%2F4io&srno=b_3_71&otracker=CLP_Filters&fm=organic&iid=0c787a8b-f9b3-44cb-bccb-fe41fa6eee1c.MOBGYCCGGPXZHSWB.SEARCH&ppt=sp&ppn=sp&ssid=jx5tk3brk00000001624087647058'

#user_Price = 14500

def priceCheck():
    response =  requests.get(url, headers = headers)
    soup = bs4.BeautifulSoup(response.content, 'lxml')

    title = soup.find("span",{"class":'B_NuCI'}).get_text()
    print(title)

    
    price = int(soup.find("div",{"class":'_30jeq3 _16Jk6d'}).get_text()[1:].replace(',',''))
    print(price)

    if(price <= 14500):
        sendMail()


def sendMail():
    smtp_object = smtplib.SMTP('smtp.gmail.com',587)
    smtp_object.ehlo()
    smtp_object.starttls()
    smtp_object.login('youremail@gmail.com', 'app_password')
    subject = 'Hey! Price fell down'
    body = 'Check the link\n' + url
    msg = f"Subject: {subject}\n\n{body}"
    smtp_object.sendmail('youremail@gmail.com', 'reciveremail@gmail.com', msg)
    print("email sent")
    smtp_object.quit()
    


while(True):
    priceCheck()
    time.sleep(60*60)
