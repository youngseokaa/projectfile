from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://youngseok:dhdudtjr11!@cluster0.jactwgi.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/bucket", methods=["POST"])
def bucket_post():
    sample_receive = request.form["sample_give"]

    count = list(db.bucket.find({}, {'_id': False}))
    num = len(count) + 1
    # num값은 나온숫자 bucket은 입력값
    doc = {
        'num': num,
        'bucket': sample_receive,
        'done': 0
    }

    db.bucket.insert_one(doc)
    return jsonify({'msg': '등록 완료!'})

@app.route("/bucket/done", methods=["POST"])
def bucket_done():
    num_receive = request.form['num_give']
    db.bucket.update_one({'num': int(num_receive)}, {'$set': {'done': 1}})
    return jsonify({'msg': '버킷완료'})

@app.route("/bucket", methods=["GET"])
def bucket_get():
    buckets_list = list(db.bucket.find({},{'_id':False}))
    return jsonify({'buckets':buckets_list})

@app.route("/bucket/cancel", methods=["POST"])
def bucket_cancel():
    num_receive = request.form['num_give']
    db.bucket.update_one({'num': int(num_receive)}, {'$set': {'done': 0}})

    return jsonify({'msg':'취소 완료!'})
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)