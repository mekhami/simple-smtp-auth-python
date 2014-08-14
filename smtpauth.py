import smtplib
import sys

def is_authenticated(server, port, username, password):
	s = smtplib.SMTP(server, port)
	s.starttls()

	try:
		s.login(username, password)
		return "Authenticated"

	except smtplib.SMTPAuthenticationError:
		return "Not Authenticated"

if __name__ == '__main__':

	server = sys.argv[1]
	username = sys.argv[2]
	password = sys.argv[3]
	port = sys.argv[4]

	print is_authenticated(server, port, username, password)

