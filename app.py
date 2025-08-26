from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello Pumkin team this is Rahul Chauhan !"

if __name__ == '__main__':
    # Listen on all interfaces, port 5000
    app.run(host='0.0.0.0', port=5000)

