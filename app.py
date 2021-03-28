from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/medow")
def medow():
    return render_template('medow.html')


@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/FAQ")
def FAQ():
    return render_template('FAQ.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
app.run(debug='true')
