# FotoArtCMS

## Local getting up and running

Preparing local system for run locally

	git clone <github repo>
	cd fotoartcms
	virtualenv venv
	source venv/bin/activate
	pip install -r requeriments.txt
	python wsgi/openshift/manage.py createdb --noinput

Now you can run the project locally

	python wsgi/openshift/manage.py runserver

# mezzanine-openshift

This project is to provide the simplest way possible to run mezzanine on the
openshift stack with the best possible defaults for development and production.


## Getting up and running

**NOTE**: Taken directly from the django-example by OpenShift.

Create an account at http://openshift.redhat.com/

Install the RHC client tools if you have not already done so:
    
    sudo gem install rhc

Create a python-2.6 application

    rhc app create -a mezzanine -t python-2.6

Add this upstream repo

    cd mezzanine
    git remote add upstream -m master git://github.com/overshard/mezzanine-openshift.git
    git pull -s recursive -X theirs upstream master

Then push the repo upstream

    git push

You can then access your new mezzanine instance at
http://mezzanine-$yournamespace.rhcloud.com with the username and password
`admin` and `default` respectively.


## Final notes

In `wsgi/openshift/settings/production.py` `DEBUG` is set to `True` in order to
get a default username and password but also for testing your app. Once you
actually go into production be sure to set this to `False`.
