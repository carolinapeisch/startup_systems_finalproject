#inspired by @grutt

from flask import Flask, request, abort
import os
import subprocess
import urllib

app = Flask(__name__)

@app.route('/')
def index():
    return 'Visit /api/num_colors?src=SOMEURL.'

@app.route('/api/num_colors', methods=['GET'])
def numColors():
    img = request.args.get('src')
    if img is None or img == "":
        return "Image has no name!"
    else:
	filename = img.split('/')[-1]
        local = "/var/www/app/imgs/"+filename
        urllib.urlretrieve(img, local)
	colors = ""
	try:
            colors = subprocess.check_output(["/usr/bin/identify", "-format", "%k", local])
        except:
            return "Imagemagick failed"
        #if(colors.returncode == 0):
         #   return colors.stdout
        #else:
         #   return "Still not working"
        return colors


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
