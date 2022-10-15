from django.http import JsonResponse
from flask import *
from DBConnection import Db

app = Flask(__name__)
db=Db()

@app.route('/')
def hello_world():
    return 'Hello World!'



@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    qry=("SELECT * FROM`login` WHERE username='"+email+"' AND password='"+password+"'")
    s = db.selectOne(qry)
    if s is not None:
        return jsonify(status="ok",lid=s['id'],type=s['type'])
    else:
        return jsonify(status= "no")



@app.route('/user',methods=["post"])
def user():
    name=request.form['name']
    email=request.form['email']
    phone=request.form['phone']
    qry="INSERT INTO login (`username`,`password`,type) VALUES ('"+email+"','"+phone+"','user')"
    res=request.form['id']
    r=db.insert(qry)
    qry1="INSERT INTO USER(`name`,`email`,`phone`,`login_id`)VALUES('"+name+"','"+email+"','"+phone+"','"+str(r)+"')"
    res1=db.insert(qry1)
    return jsonify(status="ok")



    


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)
