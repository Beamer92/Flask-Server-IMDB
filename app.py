from flask import Flask, request, jsonify
app = Flask(__name__)
import controller.hello as hello
#note that __name__ is two underscores on each side

@app.route('/hello', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return hello.getFunc()
        pass  
    elif request.method == 'POST':
        data = request.form
        result = hello.postFunc('walk')
        return result
        pass



