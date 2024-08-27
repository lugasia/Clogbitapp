from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('clogbit.html', message="Welcome to My Web App")




if __name__ == '__main__':
    app.run(debug=True)
    
    