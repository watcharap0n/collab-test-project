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
        'name': 'nattawut',
        'age': '24',
    },
    {
        'id': '002',
        'name': 'watcharapon',
        'age': '24',
    }
],
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
@app.route('/')#get 
def index():
    q = request.args.get('todo')
    key = request.args.get('key')
    if q or key:
        query = int(q)
        if key:
            result = data[query][key]
            return jsonify(result)
        elif q: 
            result = data[query]
            return jsonify(result)
    else:
        return jsonify(data)


if __name__ == '__main__':
    app.run(port=8080, debug=True)
