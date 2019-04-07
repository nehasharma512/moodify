import base64

from flask import Flask, render_template,request
from mood import main_func

app = Flask(__name__)

#default page (function home will get activated when going to home route "/")
# render template looks for template (html) in templates folder
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/player")
def player():
    return render_template("player.html")

@app.route('/music', methods=['POST', 'GET'])
def music():
   mood = main_func()
   return render_template("player.html",emotion=mood)

@app.route("/test", methods=['POST', 'GET'])
def test():
	if request.method == 'POST':
		req = request.json
		s = req["img64"]
		print(type(s))
		#print(s)
		# Take in base64 string and return byte arrary
		imgdata = base64.b64decode(s)

		f = open("snap.jpg", "wb")
		f.write(imgdata)
		f.close()
		print(type(imgdata)) #byte array
		return "True"


if __name__ == "__main__":
    app.run(debug=True)
