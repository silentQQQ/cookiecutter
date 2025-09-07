# Project Introduction
Using cookiecutter to create a Django project template

# Prerequisites
- Create a venv virtual environment
```
python -m venv venv_ck
pip install cookiecutter
pip install django
cd ./venv_ck/Scripts
activate
```

# Run Cookiecutter
```
cookiecutter git@github.com:silentQQQ/cookiecutter.git
```

## Create App
Enter the created project, such as myproject
```
python add_app.py app1_name app2_name ……

```

Perform the following operations:
- Add app_name to INSTALLED_APPS in settings.py
- Add URLs to the project's urls.py
- Create apps\app_name directory under the project directory and initialize it
- The project can be run directly, such as python manage.py runserver

# Project Address
https://github.com/silentQQQ/cookiecutter.git

# Hook Description
The files in the hooks directory will be automatically executed after project creation to initialize the project, such as creating databases, creating superusers, etc.
- pre_gen_project.py: Executed before project creation
- post_gen_project.py: Executed after project creation

# Cookiecutter Command Description
Usage: cookiecutter [OPTIONS] [TEMPLATE] [EXTRA_CONTEXT]...

  Create a project from a Cookiecutter project template (TEMPLATE).
  Cookiecutter is free and open source software, developed and managed by
  volunteers. If you would like to help out or fund the project, please get in      
  touch at https://github.com/cookiecutter/django_config

Options:
  -V, --version                Show the version and exit.
  --no-input                   Do not prompt for parameters and only use
                               django_configjson file content. Defaults to
                               deleting any cached resources and redownloading      
                               them. Cannot be combined with the --replay
                               flag.
  -c, --checkout TEXT          branch, tag or commit to checkout after git
                               clone
  --directory TEXT             Directory within repo that holds
                               django_configjson file for advanced
                               repositories with multi templates in it
  -v, --verbose                Print debug information
  --replay                     Do not prompt for parameters and only use
                               information entered previously. Cannot be
                               combined with the --no-input flag or with extra      
                               configuration passed.
  --replay-file PATH           Use this file for replay instead of the
                               default.
  -f, --overwrite-if-exists    Overwrite the contents of the output directory       
                               if it already exists
  -s, --skip-if-file-exists    Skip the files in the corresponding directories      
                               if they already exist
  -o, --output-dir PATH        Where to output the generated project dir into       
  --config-file PATH           User configuration file
  --default-config             Do not load a config file. Use the defaults
                               instead
  --debug-file PATH            File to be used as a stream for DEBUG logging        
  --accept-hooks [yes|ask|no]  Accept pre/post hooks
  -l, --list-installed         List currently installed templates.
  --keep-project-on-failure    Do not delete project folder on failure
  -h, --help                   Show this message and exit.