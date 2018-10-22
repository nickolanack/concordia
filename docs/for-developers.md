# For Developers 


## Prerequisites

This application can run on a single Docker host using docker-compose. 
(recommended for development environments). For production, see the 
[cloudformation](cloudformation/) directory for AWS Elastic Container Service stack templates.

## Running Concordia

    $ git clone https://github.com/LibraryOfCongress/concordia.git
    $ cd concordia
    $ make devup

Browse to [localhost](http://localhost)

### Development Environment

You may wish to run the Django development server on your localhost
instead of within a Docker container. It is easy to set up a Python
virtual environment to work in.

#### Serve

Instead of doing `make devup` as above, instead do the following:

    $ docker-compose up -d db
    $ docker-compose up -d rabbit
    $ docker-compose up -d importer

This will keep the database in its container for convenience.

Next, set up a Python virtual environment, 
install [pipenv](https://docs.pipenv.org/), and other Python prerequisites:

    $ python3 -m venv .venv
    $ source .venv/bin/activate
    $ pip3 install pipenv
    $ pipenv install --dev

Finally, configure the Django settings, run migrations, and launch the
development server:

    $ export DJANGO_SETTINGS_MODULE="concordia.settings_dev"
    $ ./manage.py migrate
    $ ./manage.py runserver

#### Import Data

Once the database, rabbitMQ service, importer and the application 
are running, you're ready to import data. 
First, [create a Django admin user](https://docs.djangoproject.com/en/2.1/intro/tutorial02/#creating-an-admin-user) 
and log in as that user.
Then, Click on Campaigns and then Add Campaign. Enter a name for the campaign 
and project and a loc.gov item URL such as 
[https://www.loc.gov/item/mss859430011](https://www.loc.gov/item/mss859430011) and click Create.


#### Data Model Graph

To generate a model graph, do:

    $ docker-compose up -d app
    $ docker-compose exec app bash
    # cd concordia/static/img
    # python3 ./manage.py graph_models concordia > tx.dot
    # dot -Tsvg tx.dot -o tx.svg

#### Python Dependencies

Python dependencies are managed using [pipenv](https://docs.pipenv.org/).

If you want to add a new Python package requirement to the application
environment, it must be added to the Pipfile and the Pipfile.lock file.
This can be done with the command:

    $ pipenv install <package>

If you manually add package names to Pipfile, then you need to update
the Pipfile.lock file:

    $ pipenv lock

Both the Pipfile and the Pipfile.lock file must be committed to the
source code repository.