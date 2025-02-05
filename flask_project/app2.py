from flask import Flask, request,jsonify

app = Flask(__name__)

menu = [
    {"name": "chicken biriyani", "price": 120},
    {"name": "mutton biriyani", "price":130},
    {"name": "chicken 65", "price":100}
]

@app.route('/data',methods=['GET','POST'])
def handled_data():
    if request.method =='POST':
        data = request.get_json()
        menu.append(data)
        return jsonify(data)
    return jsonify(menu)

if __name__ == '__main__':
    app.run(debug=True)
