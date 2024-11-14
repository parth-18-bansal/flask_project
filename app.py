from flask import Flask

#wsgi application
app = Flask(__name__)               #it creates the instance of the Flask class. it will be the wsgi

@app.route("/")
def welcome():
    return "<html><H1>welcome to the website</H1></html>"

if __name__ == "__main__":
    app.run(debug=True)