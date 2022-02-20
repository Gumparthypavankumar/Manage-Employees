# import statements
from flask import Flask, jsonify, request, render_template, redirect, url_for, flash

from flask_pymongo import PyMongo

import urllib

from bson.json_util import dumps

import datetime
# Global Declarations
app = Flask(__name__)
app.secret_key = "abc"

app.config['MONGO_URI'] = "mongodb+srv://PavanKumar:qupcRKIVnmMGGiOa@employee-manager.8ome6.mongodb.net/employees?retryWrites=true&w=majority"
mongo = PyMongo(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        desg = request.form['desg']
        phone = request.form['phone']
        mongo.db.employee.insert_one({
            'name': name,
            'email': email,
            'designation': desg,
            'phone': phone,
            'created_at': datetime.datetime.now()
        })
        return redirect(request.url)
    else:
        cursor = mongo.db.employee.find().sort('created_at', -1)
        employees = list(cursor)
    return render_template('index.html', employees=employees)


@app.route('/employee/update/<ObjectId:id>', methods=['GET', 'PUT'])
def updateEmployee(id):
    if request.method == 'PUT':
        name = request.form['name']
        email = request.form['email']
        desg = request.form['desg']
        phone = request.form['phone']
        mongo.db.employee.update_one({'_id': id}, {'$set': {
            'name': name,
            'email': email,
            'designation': desg,
            'phone': phone,
            'created_at': datetime.datetime.now()
        }})
        return ""
    else:
        employee = mongo.db.employee.find_one_or_404({'_id': id})
        return render_template('edit.html', employee=employee)


@app.route('/employee/delete/<ObjectId:id>', methods=['GET', 'DELETE'])
def deleteEmployee(id):
    if request.method == 'DELETE':
        mongo.db.employee.delete_one({'_id': id})
        return "Employee Deleted Successfully"
    else:
        return redirect(request.url)


if __name__ == "__main__":
    app.run(debug=True, port=8000)
