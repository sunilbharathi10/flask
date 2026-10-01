# from flask import Flask,render_template

# app=Flask(__name__)


# @app.route("/kumar")
# def sunil():
#     return "flask introduction completed"
# @app.route("/ethavathukudunga")
# def ashik():
#     return "<h1>hi i am ashik ali from kk.nagar</h1>"


# @app.route("/kokkikumar")
# def webpage():
#     age=27
#     a=[1,3,4,5,56,"sre",44.0,True]
#     return render_template("index.html",myage=age,a=a)

# @app.route("/para/<name>")

# def kusuka(name):
#     return f" hi hello {name}"


# if __name__=="__main__":
#     app.run(debug=True)



# from flask import Flask,render_template,request,redirect

# import sqlite3

# connection=sqlite3.connect("batch24.db",check_same_thread=False)
# cur=connection.cursor()

# cur.execute("create table if not exists employees(id int primary key,emp_name varchar(50),password varchar(50),role varchar(50),Email varchar(50),salary int) ")


# app=Flask(__name__)



# @app.route("/",methods=["POST","GET"])

# def register():
#     if request.method=="POST":
#         uid=request.form["id"]
#         uname=request.form["name"]
#         upass=request.form["password"]
#         designation=request.form["role"]
#         esalary=request.form["salary"]
#         uemail=request.form["email"]
    
#         cur.execute("insert into employees(id,emp_name,password,role,Email,salary) values(?,?,?,?,?,?)",(uid,uname,upass,designation,uemail,esalary))
#         connection.commit()
        
#         return "data added to the database"
#     else:
#         return render_template("create.html")

# @app.route("/read")
# def view_data():
#     data=cur.execute("select * from employees")
#     record=data.fetchall()
#     return render_template("view.html",result=record)


# @app.route("/update/<iid>", methods=["GET", "POST"])
# def update(iid):
#     iid = int(iid)
#     # Fetch the existing record
#     record = cur.execute("SELECT * FROM employees WHERE id=?", (iid,)).fetchone()

#     if not record:
#         return "Record not found", 404

#     if request.method == "POST":
#         # Keep ID the same; only update other fields
#         uname = request.form["name"]
#         upass = request.form["password"]
#         designation = request.form["role"]
#         esalary = int(request.form["salary"])
#         uemail = request.form["email"]

#         cur.execute("""
#             UPDATE employees
#             SET emp_name=?, password=?, role=?, Email=?, salary=?
#             WHERE id=?
#         """, (uname, upass, designation, uemail, esalary, iid))
#         connection.commit()
#         return redirect("/read")
    
#     else:
#         # Render the form with existing values
#         return render_template("update.html", record=record)
    


# @app.route("/delete/<id1>",methods=["POST","GET"])
# def delete(id1):

#     data=cur.execute("select * from employees where id=?",(id1,))
#     cvb=data.fetchone()
#     if request.method=="POST":
#         cur.execute("delete from employees where id=?",(id1,))
#         connection.commit()
#         return redirect("/read")
#     else:
#         return render_template("delete.html",recording=cvb)




# app.run(debug=True)


# from flask import Flask,render_template,redirect,request
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ghfriend.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     email = db.Column(db.String(100), unique=True, nullable=False)
#     password = db.Column(db.String(200), nullable=False)

# @app.route("/")
# def home():
#     return "Flask app is running!"

# with app.app_context():
#     db.create_all()


# @app.route("/create",methods=["GET","POST"])
# def create_users():
#     if request.method=="POST":
#         id=request.form["id"]
#         name=request.form["name"]
#         email=request.form["email"]
#         password=request.form["password"]
        
#         new_user=User(id=id,name=name,email=email,password=password)
#         db.session.add(new_user)
#         db.session.commit()
        
#         return redirect("/view")
#     return render_template("create.html")

# @app.route("/view") #view
# def index():
#     users=User.query.all()
#     return render_template("index.html",users=users)   



# @app.route("/update/<int:id>",methods=["GET","POST"])
# def update_user(id):
#     user=User.query.get_or_404(id) #one is gettted the details or throw 404 not found error
    
#     if request.method=="POST":
#         user.id=request.form['id']
#         user.name=request.form['name']
#         user.email=request.form['email']
#         user.password=request.form['password']
      
#         db.session.commit()
#         return redirect("/view")
#     return render_template("update.html",user=user)




# @app.route("/delete/<int:id>")
# def delete_user(id):
#     user=User.query.get_or_404(id)
#     db.session.delete(user)
#     db.session.commit()
#     return redirect("/view")





# if __name__=="__main__":

#     app.run(debug=True)








# from flask_mail import Mail,Message
# from flask import Flask

# app=Flask(__name__)

# app.config["MAIL_SERVER"]="smtp.gmail.com" #simplemailtransfer protocol
# app.config["MAIL_PORT"]=587
# app.config["MAIL_USERNAME"]="sunilbharathimss@gmail.com"
# app.config["MAIL_PASSWORD"]="lgst mafh dbqr eawo"
# app.config["MAIL_USE_TLS"]=True

# mail=Mail(app)

# @app.route("/")
# def send_mail():
#     msg=Message(subject="subject:this mail is generated from flask",sender="sunilbharathimss@gmail.com",recipients=["ashikali246810@gmail.com","madhavanselvaraj4@gmail.com","abinayasakthi2005ya@gmail.com","arunyamaha007@gmail.com","sunilbharathiuniqtechnologies@gmail.com"])

#     msg.body="hello user\n you have important mail"
    
#     # with app.open_resource("static/media/cm.jpg") as img:
#     #     msg.attach("cm.jpg","image/jpg",img.read())
        
#     # with app.open_resource("static/media/asdf.mp4") as vid:
#     #     msg.attach("asdf.mp4","video/mp4",vid.read())
    
#     with app.open_resource("static/media/audios.mp3") as aud:
#         msg.attach("audios.mp3","video/mp4",aud.read())
        
#     with app.open_resource("static/media/python.pdf") as pdfss:
#        msg.attach("python.pdf","application/pdf",pdfss.read())
    
        
        
#     mail.send(msg)
#     return "mail sented successfully"
# app.run(debug=True)



# from flask_mail import Mail,Message
# from flask import Flask, render_template, request, redirect
# import random

# app=Flask(__name__)

# app.config["MAIL_SERVER"]="smtp.gmail.com" #simplemailtransfer protocol
# app.config["MAIL_PORT"]=587
# app.config["MAIL_USERNAME"]="sunilbharathimss@gmail.com"
# app.config["MAIL_PASSWORD"]="lgst mafh dbqr eawo"
# app.config["MAIL_USE_TLS"]=True

# saro=Mail(app)

# otp=random.randint(000000,999999)

# @app.route("/go")
# def asd():
#     return render_template("cv.html")

# @app.route("/saro",methods=["POST","GET"])
# def zxcv():
#     if request.method=="POST":
#         useremail=request.form["Email"]
#         data=Message(subject="subject:otp email for verification",sender="sunilbharathimss@gmail.com",recipients=[useremail])
#         data.body=f"the otp is---{str(otp)}"
#         try:
#             saro.send(data)
#             return render_template("fgh.html")
#         except Exception as e:
#             return str(e)
        

# @app.route("/actual_verification",methods=["POST","GET"])       
# def verify():

#     if request.method=="POST":

#         userotp=request.form["generate_otp"]

#         if str(otp)==userotp:
#             return render_template("home.html")
#         else:
#             return "OTP NOT MATCHED ❌"

# app.run(debug=True)






# from flask import Flask, render_template, request, redirect, session
# from flask_sqlalchemy import SQLAlchemy
# from werkzeug.security import generate_password_hash, check_password_hash

# app = Flask(__name__)

# app.config["SECRET_KEY"] = "secret123"
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///kumar.db"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# db = SQLAlchemy(app)



# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(50), unique=True)
#     password = db.Column(db.String(200))
    
    
# with app.app_context():
#     db.create_all()


# @app.route("/")
# def home():
#     return render_template("login.html")


# @app.route("/register")
# def register_page():
#     return render_template("register.html")


# @app.route("/register_user",methods=["POST"])
# def register_user():
#     username=request.form['username']
#     password=request.form['password']
    
#     # check existing user
#     user=User.query.filter_by(username=username).first()
    
#     if user:
#         return "username already exists"
    
#     hashed_password=generate_password_hash(password)
    
#     new_user=User(username=username,password=hashed_password)
#     db.session.add(new_user)
#     db.session.commit()
    
#     return redirect("/")

# #login authencation
# @app.route("/login",methods=["POST"])

# def login():
#     username=request.form['username']
#     password=request.form['password']
    
#     user=User.query.filter_by(username=username).first()
    
#     if user and check_password_hash(user.password,password):
#         session['user']=username
#         return redirect("/dashboard")
#     else:
#         return "Invalid username or password 🔐"
    
# #dashboard
# @app.route("/dashboard")
# def dashbord():
#     if 'user' in session:
#         return render_template("home.html",user=session['user'])
#     return redirect("/")

# #logout
# @app.route("/logout")
# def logout():
#     session.pop('user',None)
#     return redirect("/")

# app.run(debug=True)















from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy

from flask_jwt_extended import jwt_manager,create_access_token,jwt_required,JWTManager
from werkzeug.security import generate_password_hash,check_password_hash

app=Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mask.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


#jwt secret key
app.config["JWT_SECRET_KEY"]="secret123"

db=SQLAlchemy(app)
jwt=JWTManager(app)


class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    email=db.Column(db.String(100),unique=True)
    password=db.Column(db.String(100))
    
with app.app_context():
    db.create_all()
    
    
#register API

@app.route("/register",methods=["POST"])
def register():
    data=request.json
    
    name=data["name"]
    email=data["email"]
    password=generate_password_hash(data["password"])
    
    user=User(name=name,email=email,password=password)
    
    db.session.add(user)
    db.session.commit()
     
    return jsonify({"message":"user registered successfully"})

#login API
@app.route("/login",methods=["post"])
def login():
    data=request.json
    email=data["email"]
    password=data["password"]
    
    user=User.query.filter_by(email=email).first()
    
    if not user:
        return jsonify({"message":"user not found"}),401
    if not check_password_hash(user.password,password):
         return jsonify({"message":"incorrect password"}),401
     
    token=create_access_token(identity=email)
    return jsonify({"message":"login successful",
                    "token":token})
    
#read api--->
@app.route("/users",methods=["GET"])
@jwt_required()
def get_users():
    users=User.query.all()
    output=[]
    for user in users:
        output.append({
            "id":user.id,
            "name":user.name,
            "email":user.email
        })
    return jsonify (output)
        
    
    
#update api--->

@app.route("/update/<int:id>",methods=["PUT"])
@jwt_required()
def update_user(id):
    user=User.query.get(id)
    if not user:
        return jsonify({"message":"user not found"})
    data=request.json
    user.name=data.get("name",user.name)
    user.email=data.get("email",user.email)
    
    db.session.commit()
    
    return jsonify({"message":"user updated successfully"})

#delete API---->

@app.route("/delete/<int:id>",methods=["DELETE"])
@jwt_required()
def delete_user(id):
    user=User.query.get(id)
    if not user:
        return jsonify({"message":"user not found"})
   
    db.session.delete(user)
    db.session.commit()
    
    return jsonify({"message":"user deleted successfully"})


#runserver

if __name__=="__main__":
    app.run(debug=True)










