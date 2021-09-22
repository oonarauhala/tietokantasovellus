from os import getenv
from flask import Flask, render_template
from os import getenv

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")

import routes