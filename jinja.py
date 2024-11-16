from flask import Flask,render_template,request


#wsgi application
app = Flask(__name__)               #it creates the instance of the Flask class. it will be the wsgi

@app.route("/")
def welcome():
    return "<html><H1>welcome to the website</H1></html>"

# here when we go to the /index path, we will redirect to the index.html page.
# here render_template will search for the file in the template folder
@app.route("/index",methods=["GET"])
def index_page():
    return render_template("index.html")

@app.route("/about")
def about_page():
    return render_template("about.html")

#variable rule
@app.route("/success/<score>")
def success(score):
    return "The mark is "+ score

if __name__ == "__main__":
    app.run(debug=True)