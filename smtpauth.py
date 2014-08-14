import smtplib
import sys, argparse

server = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]
port = sys.argv[4]

s = smtplib.SMTP(server, port)
s.starttls()

try:
	s.login(username, password)
	print "Authenticated"

except smtplib.SMTPAuthenticationError:
	print "Not Authenticated"


