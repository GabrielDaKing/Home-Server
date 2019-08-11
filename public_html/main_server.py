#Home Server

from flask import Flask, render_template,request, abort
from os import listdir
from os.path import isdir,isfile

app = Flask(__name__)

root = "static/Movies and Shows"

@app.route('/')
def home():

	try:
		user = request.args.get('user')
		if isdir(root+"/"+user):
			files = [filename.split('.')[0] for filename in listdir(root+"/"+user)]
			return render_template('home.html',files=files,root=user+"/")

		else:
			vfile = root+'/'+user+".mp4"
			print(vfile)
			return render_template('video.html',vfile=vfile)

	except:
		files = [filename.split('.')[0] for filename in listdir(root)]
		print(files)
		return render_template('home.html',files=files,root="")

# @app.route('/video')
# def video():


if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0',port=80)