import time
import serial
import smtplib
import logging

TO = 'YOUR@EMAIL.COM'
MAIL_USER = 'YOUR@EMAIL.COM'
MAIL_PASS = 'YOURPASSWORD'

SUBJECT = 'Intrusion!!'
TEXT = 'Your PIR sensor detected movement'

# Include your serial path below
ser = serial.Serial('/dev/YOUR_SERIAL_PATH', 9600)

def send_email():
    print("Sending Email")
    smtpserver = smtplib.SMTP("YOUR.SMTP.COM",YOURPORT)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(MAIL_USER, MAIL_PASS)
    header = 'To:' + TO + '\n' + 'From: ' + MAIL_USER
    header = header + '\n' + 'Subject:' + SUBJECT + '\n'
    print header
    msg = header + '\n' + TEXT + ' \n\n'
    smtpserver.sendmail(MAIL_USER, TO, msg)
    smtpserver.close()
    
while True:
    message = ser.readline()
    print(message)
    if message[0] == 'M' :
        send_email()
        logging.basicConfig(filename='sec.log', format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logging.warning('Movement detected!')
    time.sleep(0.5)
