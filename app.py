
# from HostTor import VicksTor
# import VicksTor as vix
# vix.run_server('flask')

from flask import Flask, jsonify, request, render_template, send_from_directory
import random
import os

app = Flask(__name__)
names = os.listdir("static")
names = [int(i.split('.')[0]) for i in names]

@app.route('/static/<filename>')
def static_jpg(filename):
    return send_from_directory("static", filename)

@app.route('/', methods = ['GET', 'POST'])
def home():
	if(request.method == 'GET'):
		i = request.args.get('i')

		if i == None:
			num = random.choice(names)
		else:
			num = i
		return render_template('index.html', num=num, length=len(names))

@app.route('/random/', methods = ['GET'])
def static_json():
	num = random.choice(names)
	return jsonify({"image":f"static/{num}.jpg","link":f"/?i={num}"})

@app.errorhandler(404)
def page_not_found(e):
    e = 'Page not Found'
    return ( render_template('404.html', e=e), 404 )

if __name__ == '__main__':
	app.run(debug = False)
