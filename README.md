# fill-in-forms-webs
You can fill in any web form that does not have captcha

#### REQUIREMENTS
```sh
$ pip install mechanize
```

#### HOW TO USE

You must add the data to the text file **data.txt** where the different fields must be separated by **:** or by the character that you indicate.

You must indicate the name of the form as shown here

```python
br.form['username']
```
Then it will indicate the position in which the data has been added

For example, if your data string is

```
test:test@gmail.com:test
 0        1          2
``` 

And it would be as follows

```python
br.form['username'] = aux[0]
br.form['email'] = aux[1]
br.form['password'] = aux[2]
```

If you want to add a file, you must do it in the following way

```python
br.form.add_file(open('route/imagen.jpg'), "image/jpeg", 'imagen.jpg')
```

| Item      | Descriptiom |
| --------- | -----|
| route/imagen.jpg  | path where the image is located |
| image/jpeg   |   MIME type of the file |
| imagen.jpg      | file output name |

#### START IT
```sh
$ py App.py
```