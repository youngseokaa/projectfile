from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://youngseok:dhdudtjr11!@cluster0.jactwgi.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
   return render_template('index.html')

@app.route("/homework", methods=["POST"])
def homework_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {
        'name':name_receive,
        'comment':comment_receive
    }
    db.pan.insert_one(doc)

    return jsonify({'msg':'응원완료!'})

@app.route("/homework", methods=["GET"])
def homework_get():
    all_pan = list(db.pan.find({}, {'_id': False}))
    return jsonify({'pan':all_pan})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)