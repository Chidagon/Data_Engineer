from flask import Flask

<<<<<<< HEAD
p = Flask(__name__, instance_relative_config=True)
app.config.from_object("config")
app.config.from_pyfile("config.py")

@app.route('/')
def index():
    return "<h1>Hello World!</h1>"

#app.add_url_rule("/","index",index)

@app.route("/user/<name>")
def user(name):
    return "<h1>Hello, {}!</h1>".format(name)

=======

app = Flask(__name__, instance_relative_config=True)
app.config.from_object("config")
app.config.from_pyfile("config.py")


@app.route('/')
def index():
    return "<h1>Hello World !</h1>"

# app.add_url_rule("/","index",index)

@app.route("/user/<name>")
def user(name: str):
    return "<h1>Hello , {}!</h1>".format(name)

@app.route("/user1/<name>")
def user1(name):
    return "<h1>Bye, {}!</h1>".format(name)
>>>>>>> upstream/main
if __name__ == "__main__":
    app.run(debug=True)