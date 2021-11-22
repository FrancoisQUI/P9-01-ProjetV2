# LitReview
9th project of OpenClassrooms Python Couses.

The Aim of the project : use Django a Python Framework based on MVT (Model Vue Template) structure.

## Requirement

- Git
- Python >3.2 with pip
- Venv

## The Stack

### [Django](https://www.djangoproject.com/download/) :
With Django, you can take web applications from concept to launch in a matter of hours. Django takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.
### [Tailwinds.css](https://tailwindcss.com/) :
A utility-first CSS framework packed with classes like flex, pt-4, text-center and rotate-90 that can be composed to build any design, directly in your markup.
### [Flake8](https://flake8.pycqa.org/en/latest/) + [Flake8-Html](https://pypi.org/project/flake8-html/) :
Flake8 is a wrapper around these tools:

  - PyFlakes
  - pycodestyle
  - Ned Batchelder’s McCabe script

Flake8 runs all the tools by launching the single flake8 command. It displays the warnings in a per-file, merged output.

Flak8-Html : A flake8 plugin to generate HTML reports of flake8 violations.

## Installation
- Download the files or clone the repo where you want 
```shell
cd {your-desired-path}
git clone git@github.com:FrancoisQUI/P9-01-ProjetV2.git
cd P9-01-ProjetV2
```
- Create and activate your virtual environnement
```shell
python -m venv {your-desired-env-path*}
source {your-desired-env-path*}/activate
```
*the best choice is 'env'
- Install necessary packages
```shell
pip install -r requirements.txt
```
## Start the APP
This app is in development : if you want to deploy it in production please follow [this guidiline](https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/) ie : don't forget to change and hide the APPKEY.

- Start the server (from the P9-01-ProjetV2 directory) 
```shell
python manage.py runserver 
```
- Start the Tailwind tools (With Browsersync for front developpement)
```shell
python manage.py tailwind start
```
- Acces to the application with your favorite Browser : 
[https://127.0.0.1:8000/](https://127.0.0.1:8000/)

### Database
#### Use current database :
the current database contain a base admin account and some exemples

Current admin :
    User : admin
    Password : admin

#### Create a new database :
Delete file _litreview/db.sqlite3_

Migrate with command: 
```shell
python manage.py migrate
```

Create the Admin Account :
```shell
python manage.py createsuperuser
```
and follow instructions

Don't forget to restart your server.

## More
### Make a flake8 report to check pep8:
from the project directory : 
```shell
flake8 --format=html --htmldir=flake-report --exclude=./env,migrations,.history   
```
You'll find the report on /flake-report directory
