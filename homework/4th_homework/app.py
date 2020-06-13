from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient 

client = MongoClient('localhost', 27017)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/shop', methods=['POST'])
def shop_post():
    guest_receive = request.form['guest_give']
    item_receive = request.form['item_give']
    amount_receive = request.form['amount_give']
    address_receive = request.form['address_give']
    num_receive = request.form['num_give']
    
    shopping = {
        'guest' : guest_receive,
        'item' : item_receive,
        'amount' : amount_receive,
        'address' : address_receive,
        'num' : num_receive
    }

    db.shop.insert_one(shopping)
    return jsonify({'result':'success', 'msg': ' 성공적으로 저장되었습니다! '})

@app.route('/shop', methods=['GET'])
def shop_reviews():
    shop = list(db.shop.find({},{'_id':0}))
    return jsonify({'result': 'success', 'shop': shop})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
