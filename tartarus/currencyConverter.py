#!/usr/bin/python2.7
import subprocess,json,pdb,os,sys
import smtplib,datetime

from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart

currUrl = 'https://currency-api.appspot.com/api/USD/INR.json'

def _getUSDtoInr(fromEmail,toEmail,fromEmailPass=''):
	curCurl = subprocess.Popen(['curl',currUrl],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	curlstdout, curlstderr = curCurl.communicate()
	jsonConvert = json.loads(curlstdout)
	msg = MIMEMultipart()
	msg['From'] = 'self@gmail.com'
	msg['To'] = toEmail
	msg['Subject'] = "USD to INR"
	gmail_user = fromEmail
	gmail_pwd = fromEmailPass
	now = datetime.datetime.now()
	body =	"""
Today's (%s) conversion rate
\tUSD->INR is
\t\t%s
    		"""%(now,jsonConvert['rate'])
	msg.attach(MIMEText(body, 'plain'))
	try:
		server = smtplib.SMTP("smtp.gmail.com", 587)
		server.ehlo()
		pdb.set_trace()
		server.starttls()
		server.login(gmail_user, gmail_pwd)
		text = msg.as_string()
		server.sendmail('self@gmail.com', toEmail, text)
		server.quit()
		print 'successfully sent the mail'
	except:
		print "failed to send mail" 


if __name__ == "__main__":
	fromEmail = sys.argv[1]
	toEmail = sys.argv[2]
	try:
		fromEmailPass = sys.argv[3]
	except:
		fromEmailPass = ''
	_getUSDtoInr(fromEmail,toEmail,fromEmailPass)