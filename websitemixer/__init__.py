from flask import Flask
from flask.ext.moment import Moment
from flask.ext.login import LoginManager
from flask_mail import Mail
import os
import json

app = Flask(__name__)
app.config.from_object('config')
mail = Mail(app)
moment = Moment(app)

basedir = os.path.abspath(os.path.dirname(__file__))

def get_all_plugin_info():
    pluginData = []
    basedir = os.path.abspath(os.path.dirname(__file__))
    dirs = os.walk(basedir+'/plugins/')
    for x in dirs:
        if os.path.isfile(x[0]+'/config.json'):
            with open(x[0]+'/config.json') as data_file:
                data = json.load(data_file)
            pluginData.append(data)
    return pluginData

pluginData = get_all_plugin_info()
for p in pluginData:
    for mod in p['import']:
        plugin = "websitemixer.plugins."+p['basics']['directory']
        name = str(mod)
        imported = getattr(__import__(plugin, fromlist=[name]), name)

