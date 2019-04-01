# Edmonton Bike Parking Project

This is a fork of Civic Tech TO's awesome [BikeSpace](https://gitlab.com/bikespace/Bicycle-parking) project. A huge thanks to everyone on the team!

The PoC is currently hosted [here](https://bikespace.edmonton.ca/), with the dashboard [here](https://bikespace.edmonton.ca/dashboard/).

Currently, this repo has backwards incompatible changes that have been done, so it can't be merged directly into BikeSpace's upstream repository.

## Building Docker images

We have a docker-compose file that is mostly used for building the Django and Postgres images needed for deployment. Assuming you have access to Edmonton's Docker repo, run the following to update the images:
``` shell
docker-compose build
docker-compose push
```

It may also be a good idea to tag the images semantically, then push those.

## Local Development

To use this project, we will work through the following steps:

1. Install requirements
1. Clone this repo
1. Add the Google service-account.json
1. Create a `virtualenv` in the project root folder
1. Have a local instance of `postgres` running
1. Build client side js
1. Run Django
1. Code away

We strongly suggest using `virtualenv` for python development.

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

# let us now use choco to install python3
choco install python --version 3.6.3
```

##### Next we get the projects code setup to run

We now will setup an environment to run the python code of
the [BikeSpace](https://github.com/CityofEdmonton/bikespace) project setup on your computer

On Mac/Linux:
```shell
pip3 install virtualenv

# get the repository of code on your machine and change to the directory
git clone https://github.com/CityofEdmonton/bikespace

# change to the directory
cd bikespace

# setup a virtualenv for python3
virtualenv -p python3 venv
# note "venv" is now the name of the directory containing the python virtualenv

# Use the "venv" you setup earlier for your python3 project buy running the activate script
source venv/bin/activate

# Install the requirements from the supplied `requirements.txt`.
pip3 install -r requirements.txt
```

On Windows:
```shell
pip3 install virtualenv

# get the repository of code on your machine and change to the directory
git clone https://github.com/CityofEdmonton/bikespace --config core.autocrlf=input

# change to the directory
cd bikespace

# setup a virtualenv for python3
virtualenv -p python3 venv
# note "venv" is now the name of the directory containing the python virtualenv

# Use the "venv" you setup earlier for your python3 project buy running the activate script
"venv/Scripts/activate"

# Install the requirements from the supplied `requirements.txt`.
pip3 install -r requirements.txt
```

### Google credentials

One of the changes made by Edmonton when doing our PoC was switching from AWS to Google Cloud for a blob store. We now require a service-account.json to be part of the app, even when working locally. Contact jared.rewerts@edmonton.ca if you're interested in setting this up.

### Database

Supplied with the repo is a `Dockerfile` to get a postgres instance up and running with the
postgis extension. The postgis extension is needed for the spatial data we use in the application.

For first time setup it requires a little bit of time in the terminal, so hang in there but once setup
it will be smooth for the rest of the development process.

[Install](https://docs.docker.com/install/) docker and docker-compose for your OS.

For Mac and Windows if you install docker, docker-compose is already installed
so don't have to worry about that.

Supplied is a `Dockerfile` for spinning up a containerized postgres with the necessary spatial 
files loaded already. Feel free to look around in the `db` folder for all the container startup files.

```shell
# Build and run our database
docker build -t bikespace-db ./db && docker run -p5432:5432 bikespace-db
```

Once all the spatial tables are loaded then the container db instance is ready to go.

#### For Linux:
Open your `5432` port it might be closed by default because of the firewall

```shell
sudo ufw allow from 127.0.0.1/24 to any port 5432
```

### Build client side js

To compile, `cd` into `bicycleparking` and run :
``` script
yarn run local
```

This builds files in the `bicycleparking/static/src/js` directory and places them into the `bicycleparking/static/dist` directory. Note that this must be run after every change to the js files.

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
```

## Project Structure

This is the current project structure, please note:

- the `Bicycle_parking` is the main Django Project folder
- the `bicycleparking` dir is one of the apps for the project
- the `db` dir is for creating our database easily
- the `test` dir is for running integration tests

## License: MIT

please see the `LICENSE` file
generated using https://choosealicense.com/licenses/mit/
