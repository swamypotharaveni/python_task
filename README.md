# python_task
i am using ajax

To setup a local development environment:

Create a virtual environment in which to install Python pip packages. With [virtualenv](https://pypi.python.org/pypi/virtualenv),
```bash
virtualenv venv            # create a virtualenv
source venv/bin/activate   # activate the Python virtualenv 
```

or with [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/),
```bash
mkvirtualenv -p python3 {{project_name}}   # create and activate environment
workon {{project_name}}   # reactivate existing environment
```

Clone GitHub Project
.............bash

 git clone https://github.com/swamypotharaveni/python_task.git
 
cd project123
Install development dependencies,
```bash


pip install -r requirements.txt
Migrate Databases
bash


python manage.py makemigrations



python manage.py migrate


Run the web application locally,
```bash


python manage.py runserver # 127.0.0.1:8000
Create Superuser,
```bash



python manage.py createsuperuser
