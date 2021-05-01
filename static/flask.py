from flask import Flask #Imports Flask Module
app = Flask(__name__)

@app.route('/') #Defining Root Node
def hello_world():
    return 'This is the Main Page'


@app.route('/2') #Second Node
def hello_world1():
    return 'You are in 2nd Node'    

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True) #Port is Set to 8080 and Host is set to Global