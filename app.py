from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template("homepage.html")

#TODO: include a 404 page
#TODO: add resume to homepage
#TODO: tab at the top referencing medium blog
#TODO: actually post on medium

if __name__ == '__main__':
    app.run()
