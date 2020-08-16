import mechanize

f = open('data.txt', 'r')
data = f.readlines()
f.close()

br = mechanize.Browser()

br.set_handle_robots(False)
br.set_handle_equiv(False)
br.addheaders = [('User-agent', 'Mozilla/5.0')]

for dat in data:
    br.open("https://yourwebsite.com/form.php")
    br.select_form(nr=0)

    aux = dat.split(':')  # Separator character

    br.form['username'] = aux[0]

    br.submit()
    br.close
