from flask import Flask
import gitworkcheck
import gitworkcheck2
app = Flask(__name__)
@app.route('/')
def index():
    return '<h1> Hello World! </h1>'
@app.route('/user/<name>')
def user(name):
    name2 = gitworkcheck.add_info(name) + ' ' + gitworkcheck2.add_info_firstbranch(name)
    return '<h1> Hi hi, %s </h1>' % name2
if __name__ == '__main__':
    app.run(debug=True)
