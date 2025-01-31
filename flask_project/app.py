from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Flask!"

@app.route('/hello/<san>')
def hello(san):
    return f"Hello, {san}!"

@app.route('/data', methods=['GET', 'POST'])
def handle_data():
    if request.method == 'POST':
      data = request.json
      return {"message": "Data received", "data": data}
    return {"message": "Send a POST request with JSON data"}

@app.route('/update/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    return {"message": f"Item {item_id} updated"}


if __name__ == '__main__':
    app.run(debug=True)




