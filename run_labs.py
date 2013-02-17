#!/usr/bin/env python
import os
# from subprocess import call

# set the location of your own config file
os.environ['LABS_SETTINGS'] = '/Users/mike/Sites/mwmlabs-com/labs.cfg'
# call(["mysql.server", "start"])

from flask_labs import app
app.run(debug=True)
