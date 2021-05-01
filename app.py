from flask import Flask,render_template,request,send_file,send_from_directory

app = Flask(__name__)

@app.route('/') 
def start():
    return render_template('index.html')

@app.route('/downloadflask')
def download_file():
	#path = "html2pdf.pdf"
	#path = "info.xlsx"
	path = "static/flask.py"
	#path = "sample.txt"
	return send_file(path, as_attachment=True)    

@app.route('/downloadhtml')
def download_file2():
	path = "static/html_template.html"
	return send_file(path, as_attachment=True)   



if __name__ == '__main__':
  app.run(port=8080, debug=True)



