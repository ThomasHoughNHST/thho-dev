from datetime import datetime
from pymongo import MongoClient
import flask


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/')
def home():
    return f'''<h3>Date: {datetime.now()}</h3>'''


if __name__ == "__main__":

    client = MongoClient(
        port=27017,
        username='root',
        password='example'
    )
    db = client.local
    collection = db['pedals']
    cursor = collection.find({})
    for document in cursor:
        print(document)

    app.run()
