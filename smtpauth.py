import smtplib
import sys, argparse

def is_authenticated(server, port, username, password):
	s = smtplib.SMTP(server, port)
	s.starttls()

	try:
		s.login(username, password)
		return "Authenticated"

	except smtplib.SMTPAuthenticationError:
		return "Not Authenticated"

if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument("--server", action="store", dest='server', help="server address")
	parser.add_argument("--port", help="server port", dest='port', type=int)
	parser.add_argument("--username", action="store", dest='username', help="username")
	parser.add_argument("--password", action="store", dest='password', help="password")

	results = parser.parse_args()
	#print results
	print is_authenticated(results.server, results.port, results.username, results.password)

