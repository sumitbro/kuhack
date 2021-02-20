# kuhack


# Setup
# The first thing to do is to clone the repository:

`$ git clone https://github.com/sumitbro/kuhack.git`
`$ cd kuhack`
# Create a virtual environment to install dependencies in and activate it:

`$ virtualenv2 --no-site-packages env`
`$ source env/bin/activate`
# Then install the dependencies:

`(env)$ pip install -r requirements.txt`
# Note the (env) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtualenv2.

# Once pip has finished downloading the dependencies:

`(env)$ cd project`
`(env)$ python manage.py runserver`
And navigate to `http://127.0.0.1:8000`

# In order to search for donor nearby location, Select the blood group and click search button.

# to connect to databases
`$ python3 -m pip install 'django-cockroachdb>=3.1.*'`

`DATABASES = {
    'default': {
        'ENGINE' : 'django_cockroachdb',
        'PORT' : <port>,
        'USER' : '<user>',
        'PASSWORD': '<password>',
        'HOST' : 'localhost',
        'NAME' : 'hack',
    }
}`

# Where,
 <user> is the username that you created earlier.
<password> is the password that you created for the <user>.
<port> is the port listed in the (sql/tcp) connection string in the SQL shell welcome text. For example, for the connection string (sql/tcp) -postgres://root:admin@127.0.0.1:61011?sslmode=require, the port is 61011.

