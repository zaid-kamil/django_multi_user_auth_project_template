
BAREBONES template for django project development.
- Contain user authentication for django system
- CSS Framework: bootstrap 4
- uses django crispy forms for displaying forms

### home
<img src="static\images\demo\1.png">

### login
<img src="static\images\demo\2.png">

### register
<img src="static\images\demo\3.png">

### reset password
<img src="static\images\demo\4.png">

### dashboard
<img src="static\images\demo\5.png">

### change password
<img src="static\images\demo\6.png">


#### install all libraries
```
pip install -r requirements.txt
```

#### check migrations
```
python manage.py makemigrations
```
```
python manage.py migrate
```
#### create a web admin
```
python manage.py createsuperuser
```

#### (optional) create an new app
```
python manage.py startapp <app-name-here>
```
#### run the webserver
```
python manage.py runserver
```

#### local web server for testing mail 
```
python -m smtpd -n -c DebuggingServer localhost:1025
```

#### link to simple ajax lib
https://lucidar.me/en/javascript-modules/ajax/