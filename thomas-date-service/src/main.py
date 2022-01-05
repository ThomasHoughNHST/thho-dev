from datetime import datetime
import flask


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/')
def home():
    return f'''<h3>Date: {datetime.now()}</h3>'''


if __name__ == "__main__":

    app.run()
