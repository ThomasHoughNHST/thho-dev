from datetime import datetime
import flask


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/date-service')
def home():
    return f'''<h1>Date: {datetime.now()}</h1>'''


if __name__ == "__main__":
    app.run()