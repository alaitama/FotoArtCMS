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


## Initial database creation

To create the initial database login via SSH and run:

    ~/python-2.6/virtenv/bin/python ~/app-root/repo/wsgi/openshift syncdb --noinput

