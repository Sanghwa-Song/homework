from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    name_receive = request.form['name_give']
    orderCount_receive = request.form['orderCount_give']
    address_receive = request.form['address_give']
    phoneNumber_receive = request.form['phoneNumber_give']

    order = {
        'name': name_receive,
        'orderCount': orderCount_receive,
        'address': address_receive,
        'phoneNumber': phoneNumber_receive
    }

    db.orders.insert_one(order)

    return jsonify({'result': 'success'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    orders = list(db.orders.find({}, {'_id': False}))

    return jsonify({'result': 'success', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=4000, debug=True)