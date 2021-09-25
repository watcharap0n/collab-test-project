from flask import Flask, jsonify, request

# flask -> package from -> package
# import -> module

app = Flask(__name__) # ไม่มีเปลี่ยนแปลง


# methods GET, POST, PUT, DELETE

# GET คือการเรียกดูข้อมูล
# POST มันคือการสร้างข้อมูล
# PUT มันคือการแก้ไขข้อมูล
# DELETE มันคือลบข้อมูล

data = [
    { 
        'id': '001',
        'name': 'watcharapon',
        'age': '24',
    },
    {
        'id': '002',
        'name': 'nattawut',
        'age': '24'
    }
]



@app.route('/index') # default GET
def root_page():
    q = request.args.get('query') # func  -> 0 string
    key = request.args.get('key')
    search = request.args.get('search')
    if q or key:
        query = int(q) # string -> int
        if key:
            result = data[query][key] # data[0]
            return jsonify(result) # index 0
        elif q:
            result = data[query]
            return jsonify(result) # index 0
    elif search:
        new_data = {}
        for i in data:
            if i['name'] == search:
                new_data['data'] = i
                new_data['status'] = True
                new_data['message'] = 'found!'
        if not new_data:
            return jsonify({'message': 'not fount!', 'status': False, 'data': {}})
        return jsonify(new_data)
    else:
        return jsonify(data)



if __name__ == '__main__':
    app.run(port=8080, debug=True)
