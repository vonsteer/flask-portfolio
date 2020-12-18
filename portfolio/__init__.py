from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cf6d07ca9c59cb68235264af53c04a38'


from portfolio import routes
