from carefullyLoadYaml import *
import smtplib
import sys

fingerFile = "fingersToNames.yml"
fingerToName = carefullyLoadYaml(fingerFile)

nameFile = "namesToContacts.yml"
nameToContact = carefullyLoadYaml(nameFile)

carrierFile = "emailTextCodes.yml"
carrierDB = carefullyLoadYaml(carrierFile)

emailUsername = "grannyCamera2017"
emailAddress = 'grannycamera2017@gmail.com'
emailPassword = 'idon\'tremember'
print(emailPassword)

def fingerToContact(f):
    '''finger to contact takes an id (presumably from the finger reader)
    and looks up the name an links that to the contacts for that name.
    Raises a keyError if data is missing from data bases.'''
    try:
        name = fingerToName[f]
    finally:
        print('There is no name associated with finger ', f, file=sys.stderr)
    try:
        contacts = nameToContact[name]
    finally:
        print('There are no contacts assoicated with name ', name,' from finger ', f, file=sys.stderr)
    return(name, contacts)

def phoneToEmail(r):
    number = r['phone']
    carrier = r['carrier']
    print(number)
    code = number+carrierDB[carrier].split('number')[1]
    return(code)

def sendTextMessage(where, msg):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(emailUsername, emailPassword)
    server.sendmail(emailAddress, where, msg)

def doFinger(f, url):
    '''DoFinger takes a finger id (presumably from fingerprint reader) and
    looks up the users name and contacts to send a text message to all of
    the contacts.
    Raises a keyError if there are no names or contacts assoicated wit the finger'''
    name, contacts = fingerToContact(f)
    for r in contacts:
        c = phoneToEmail(r)
        msg = '''\
From:grannycamera2017@gmail.com
Subject: Pacifica Senior Living

 '''
        msg = msg+'Hi '+r['name']+', '+"\n"+name+' wants to chat at '+url+"\n"
        print(c)
        print(msg)
        sendTextMessage(c, msg)
