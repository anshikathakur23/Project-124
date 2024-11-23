from flask import Flask, jsonify, request

app = Flask (__name__)

contacts = []

@app.route ("/add-data", methods = ["POST"])

def tasks ():
    if not request.json:
        return jsonify ({
            "status":"error",
            "message":"Please provide the data"
        }, 400)
    
    contact = {
        'id': tasks[-1]['id'] + 1,
        'name': request.json['name'],
        'contact': request.json['contact'],
        'done': False
    }

    contacts.append (contact)

    return jsonify ({
        'status': 'success',
        'message': 'Task added successfully',
        'data': 'contact'
    }, 201)

if __name__ == '__main__':
    app.run (debug = True)