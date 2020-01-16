# Rss-News-Feed

OS - Ubuntu 16.04 <br>
Python - 2.7 <br>
Database - sqlite3 <br>
Django - 1.11.27 <br>

<b>Installation Steps:</b>

1. Create Virtual Environment <br>
$ virtualenv environment-name

2. Activate Virtual Environment <br>
$ source environment-name/bin/activate

3. Clone Project <br>
$ git clone https://github.com/sabir-hakeem/Rss-News-Feed.git

4. Go to project path <br>
$ cd Rss-News-Feed/

4. Install requirements.txt file <br>
$ pip install -r requirements.txt

5. Make Migrations <br>
$ python manage.py makemigrations

6. Migrate <br>
$ python manage.py migrate

7. Check for <b>CRONJOBS</b> settings in settings.py file <br>

8. Run Cronjob command <br>
$ python manage.py crontab add

9. Runserver <br>
$ python manage.py runserver

10. Open URL <br>
http://localhost:8000

<b><i>Note:</i></b>
Set Proxy Credentials in 'Rss-News-Feed/Rss_Feed/views.py'
