from datetime import datetime
from pymongo import MongoClient
import flask


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/')
def home():
    return f'''<h1>Date: {datetime.now()}</h1>'''


if __name__ == "__main__":

    client = MongoClient(
        port=27017,
        username='root',
        password='example'
    )
    db = client.local
    brand = ['Boss', 'MXR', 'Ibanez']
    model = ['BD-2', 'Distortion +', 'AD-9']
    pedal_type = ['Drive', 'Drive', 'Delay']

    for i in range(0, len(brand)):
        pedal = {
            'brand': brand[i],
            'model': model[i],
            'pedal_type': pedal_type[i]
        }
        result = db.pedals.insert_one(pedal)

    app.run()
