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
        'hobbies': []
    },
    {
        'id': '002',
        'name': 'nattawut',
        'age': '24',
        'hobbies': []
    }
]



@app.route('/index', methods=['GET', 'POST']) # default GET
def root_page():
    if request.method == 'GET':
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
    elif request.method == 'POST':
        search = request.args.get('q')
        hobbie = request.args.get('hobbie')
        item = request.get_json()
        if search:
            for obj in data:
                if obj['id'] == search:
                    hobbies = obj['hobbies']
                    hobbies.append(hobbie)
            return jsonify(data)
        elif item:
            data.append(item)
            return jsonify(data)
        else:
            name = request.form['name']
            age = request.form['age']
            id = request.form['id']
            hobbie = request.form['hobbie']
            val = {
                'name': name,
                'age': age,
                'id': id,
                'hobbies': [hobbie],
            }
            data.append(val)
            return jsonify(data)


@app.route('/post_data', methods=['POST'])
def post_data():
    pass



if __name__ == '__main__':
    app.run(port=8080, debug=True)