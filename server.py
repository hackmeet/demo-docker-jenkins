from flask import Flask

app = Flask(__name__)

@app.route('/')
def root():
    return 'welcome to the server v1.2 hehe'

@app.route('/version')
def version():
    return "1.0"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
