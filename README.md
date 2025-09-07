# Project Introduction
Using cookiecutter to create a Django project template
Inspired by [cookiecutter](https://github.com/cookiecutter/cookiecutter)

# Prerequisites
- Create a venv virtual environment
```
python -m venv venv_ck
cd ./venv_ck/Scripts
activate

pip install cookiecutter
pip install django
```

# Run Cookiecutter
## Create Project
```
cookiecutter git@github.com:silentQQQ/cookiecutter.git
```
- project name, defalut is myproject
- Author, default is moomboss
- Version, default is 1.0.0


## Create App
Enter the project directory, run the following command to create django apps
```
python add_app.py app1 app2 app3
```

## Test 
```
python manage.py runserver
```
access http://127.0.0.1:8000/app1/
> hello app1
 
# Hook Description
The files in the hooks directory will be automatically executed after project creation to initialize the project, such as creating databases, creating superusers, etc.
- pre_gen_project.py: Executed before project creation
- post_gen_project.py: Executed after project creation
 