from flask import Flask, jsonify, request, abort
from uuid import uuid4
from threading import Thread

app=Flask(__name__)

@app.route('/api/multiagent', methods=['POST'])
def run_multiagent():
    age = request.args.get('age')
    print(f'Age: {age}')
    return jsonify({'age': age})
    
if __name__ =='__main__':
    app.run(debug=True, port=3001)
