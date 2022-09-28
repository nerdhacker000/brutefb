import mechanize
br = mechanize.Browser()
br.open("http://mywebsite.com/messages.php?action=send")
br.select_form(nr = 0)
br.form['email'] = 'marccarthy3@gmail.com'
br.form['pass'] = '. 1234@ duah. com'
req = br.submit()
req.read()
