from flask import Flask, render_template

app = Flask(__name__, template_folder ='templates')

# menggunakan parameter garis miring
# di kode html juga demikian

@app.route('/login')
def login():
    return render_template("login.html") 

@app.route('/')
def signup():
    return render_template("signup.html")

@app.route('/home')
def home():
    return render_template("home.html")
    


if __name__ == "__main__":
    app.run(debug=True)
