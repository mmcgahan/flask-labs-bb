# Installation

1. First, install virtualenv (and optionally virtualenvwrapper), and then use pip to load the packages in requirements.txt
```bash
pip install -r requirements.txt
```

2. Modify the provided run_labs file to point the LABS_SETTINGS environment variable to your configuration file. An example Flask-Labs config file is provided in flask_labs-example.cfg - put in your database details and *move it out of the repository*.

3. Create a database with the settings in LABS_SETTINGS

4. Setup the database with setup.py. This will create an admin user 'Admin' with the password chosen in LABS_SETTINGS
```bash
python flask_labs/setup.py
```

5. For styling, set up [SASS](http://sass-lang.com/)+[Compass](http://compass-style.org/install/)
6. Run it
```bash
./run_labs.py
```

# Technology Stack

1. Flask
    - SQLAlchemy
    - Flask-Login
    - bcrypt
    - WTForms
2. SASS+Compass
3. Backbone
4. MySQL
5. HTML5

# TODO

- Create manager script to make installation/operation easier.
    - Admin user creation
    - Categories
    - Other options?
- Pull out MWMLabs-specific code
- Better boilerplate style
- Document all the things - make modules more explicit, e.g. XML-RPC API
