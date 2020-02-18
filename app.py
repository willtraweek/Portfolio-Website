from flask import Flask, render_template, request

application = Flask(__name__)
app = application

@app.route('/')
@app.route('/home')
@app.route('/index')
def home_page():
    return render_template("homepage.html")

@app.route('/zirtue_forwarding_test')
def zirtue_forwarding_page():
    return render_template("zirtue_forwarding_test.html")

#TODO: include a 404 page
#TODO: add resume to homepage
#TODO: tab at the top referencing medium blog
#TODO: actually post on medium

if __name__ == '__main__':
    app.run()
