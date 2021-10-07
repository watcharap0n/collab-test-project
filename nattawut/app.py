from flask import Flask, jsonify, request

#flask -> package from -> package
# import -> module

app = Flask(__name__) 

# methods Get, Post, put, delete

# Get คือ การเรียกข้อมูล 
# post คือ การสร้างข้อมูล
# put คือ การแก้ไขข้อมูล
# Delete คือ ลบข้อมูล
#vim ฝึกพิมพ์

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
pets = [
    {
        'colors': 'brown',
        'sex' : 'male',
        'type' : 'pomeranian'
    },
    {
        'colors': 'red',
        'sex' : 'female',
        'type' : 'shiwawa'
    },
    {
        'colors': 'blue',
        'sex' : 'female',
        'type' : 'shiba'
    }
]
@app.route('/',methods=['GET','POST'])#get 
def index():
    if request.method == 'GET':   
        q = request.args.get('todo')
        key = request.args.get('key')
        searchs = request.args.get('se')
        if q or key:
            query = int(q)
            if key:
                result = data[query][key]
                return jsonify(result)
            elif q: 
                result = data[query]
                return jsonify(result)
        elif searchs:
            datas = {}
            for i in data:
                if i['name'] == searchs:
                    datas['data'] = i
                    datas['status'] = True
                    datas['message'] = 'found!'
                    datas['notifycation'] = 'found Information!'
            if not datas:
                return jsonify({'message': 'not found!', 'status': False, 'notify': 'no name!', 'data': {}})
            return jsonify(datas)    
        else:
            return jsonify(data)        
    elif request.method == 'POST':  
        search = request.args.get('q') # มีหน้าที่ในการเป็นตัวแปรที่เก็บ รีเควส
        hobbie = request.args.get('hobbies')
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
            name_form= request.form['name']
            age_from = request.form['age']
            id_from = request.form['id']
            hobbie_from = request.form['hobbies']    
            val = {
                'id': id_from,
                'name': name_form,
                'hobbies': [hobbie_from],
                'age': age_from
            }
            data.append(val)
            return jsonify(data)


@app.route('/haha')
def eiei():
    p = request.args.get('dog')
    pey = request.args.get('pey')
    print(p)
    if p or pey:
        shabu = int(p)
        if pey:
            result = pets[shabu][pey]
            return jsonify(result)
        elif p:
            result = pets[shabu]
            return jsonify(result)
    else:        
        return jsonify(pets) 


@app.route('/put_todo/<string:id>', methods=['PUT'])
def put_data():
    pass

if __name__ == '__main__':
    app.run(port=8080, debug=True)
