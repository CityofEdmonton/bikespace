# Toronto Bike Parking Project

Note: This is a debugging branch and should NOT be merged with the master until and unless the code is updated and stable.

## Local Development

To use this project, we will work though the following steps:

1. Install requirements
2. Clone this repo
3. Create a `virtualenv` in the project root folder
4. Have a local instance of `postgres` running
5. Install ngrok
6. Code away

We strongly suggest on using `virtualenv` for python development

#### Next we Install python3 on your computer

On mac osx

```shell
# On Mac OSX we suggest homebrew, also known as brew
# please visit https://brew.sh/
# follow the on-screen instructions of the website

# hopefully homebrew is installed
# let us now use brew to install python3
brew install python3
```

On windows

```shell
# On windows we suggest chocolatey, also known as choco
# please visit https://chocolatey.org/
# follow the on-screen instructions of the website

# hopefully homebrew is installed
# let us now use choco to install python3
choco install python --version 3.6.3
```

##### Next we get the projects code setup to run

We now will setup an environment to run the python code of
the [https://gitlab.com/bikespace/Bicycle-parking](https://gitlab.com/bikespace/Bicycle-parking) project setup on your computer

```shell
pip3 install virtualenv

# get the repository of code on your machine and change to the directory
git clone git@gitlab.com:bikespace/Bicycle-parking.git civictechto-bicycle-parking

# change to the directory
cd civictechto-bicycle-parking

# setup a virtualenv for python3
virtualenv -p python3 venv
# note "venv" is now the name of the directory containing the python virtualenv

# Use the "venv" you setup earlier for your python3 project buy running the activate script
source venv/bin/activate

# Install requirements
# Install the requirements from the supplied `requirements.txt`.
pip3 install -r requirements.txt
```

### Have a postgres instance running

For mac OSX the easiest method is to download the [Postgres app](http://postgresapp.com/)

For other OS specific postgres packages running on the default 5432 port
Please visit the [postgres download page](https://www.postgresql.org/download/)

Create a database on postgres with the name

```
bike_parking_toronto
```

Now we export the databse url, so django can just use that instead of the default sqlite

```shell
export DATABASE_URL=postgresql://localhost/bike_parking_toronto
```

### Install ngrok

ngrok is needed to serve the local django application over ssl.
To install ngrok, use [npm](https://www.npmjs.com/get-npm).

Install ngrok globally:

```shell
which npm
npm install ngrok -g
```

### Start the Django Application

Once all the above steps are complete test by running the django app.

**Run migrations to apply the models defined into the database**

Run this migrate whenever the models.py for the app has been changed so the
changes can be applied to the databases.

```shell
# First we run the migrations for the database
python manage.py migrate

# Let us first create a superuser for the admin web page
python manage.py createsuperuser

# Now we can run the django web app
python manage.py runserver

# Now run ngrok to serve over https
# ngrok http [please_insert_port_django_is_running_on]
# for example
ngrok http 3000
```

## Project Structure

This is the current project structure, please note:

- the `Bicycle_parking` is the main Django Project folder
- the `bicycleparking` dir is one of the apps for the project

```
├── bicycleparking
│   ├── admin.py
│   ├── apps.py
│   ├── geocode.py
│   ├── __init__.py
│   ├── migrations
│   ├── models.py
│   ├── node_modules
│   ├── package.json
│   ├── package-lock.json
│   ├── __pycache__
│   ├── rollup.config.js
│   ├── serializers.py
│   ├── static
│   ├── templates
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── Bicycle_parking
│   ├── __init__.py
│   ├── __pycache__
│   ├── settings
│   ├── static
│   ├── staticfiles
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── docker-compose.yml
├── LICENSE
├── manage.py
├── node_modules
│   ├── flatpickr
│   ├── leaflet
│   └── leaflet-search
├── package.json
├── package-lock.json
├── Procfile
├── README.md
├── requirements.txt
├── runtime.txt
├── test
│   └── geodata_001.xml
└── venv
    ├── bin
    ├── include
    ├── lib
    └── pip-selfcheck.json
```

## Client Side

```
npm install
```

## Pushing changes

Please checkout out a new branch when working on the project and submit merge requests
for the proposed changes to the master branch.

## License: MIT

please see the `LICENSE` file
generated using https://choosealicense.com/licenses/mit/
