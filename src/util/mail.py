from onesecmail import OneSecMail
import re

def getEnlightenMailbox():
    return "enlighten@1secmail.net"

def getRandomMailbox():
    return OneSecMail.get_random_mailbox().address

#get last ,ail, access properties using assignement (.body, .subject...)
def getLastMail(mail):
    mailbox=OneSecMail.from_address(mail)
    return mailbox.get_messages()[0]


#get login link from you.com
def getLoginLink(mail): 
    with open("src/util/mails/last_mail.html",'w') as f:
        f.write(f"<h1>Mail title : {getLastMail(mail).subject}</h1>")
        f.write(f"Date : <i>{getLastMail(mail).date}</i>")
        f.write("<hr><br>")
        f.write(getLastMail(mail).body)
    try:
        return re.search('''href="(.*?)"''',getLastMail(mail).body).group(1)
    except:
        return "Not a verification mail"



