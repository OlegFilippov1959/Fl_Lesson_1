from flask import Flask
import gitworkcheck
app = Flask(__name__)
@app.route('/')
def index():
    return '<h1> Hello World! </h1>'
@app.route('/user/<name>')
def user(name):
    #name = name + add_info
    name2 = gitworkcheck.add_info(name)
    return '<h1> Hi hi, %s </h1>' % name2
    #return '<h1> Hi hi, %s </h1>' % name
if __name__ == '__main__':
    app.run(debug=True)
