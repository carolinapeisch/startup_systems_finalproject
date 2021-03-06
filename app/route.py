
# from flask import Flask, request
# from subprocess import check_output, call
# import urllib2, re
 
# app = Flask(__name__)      
 
# @app.route('/')
# def home():
#   return render_template('imagemagick.py')
 
# if __name__ == '__main__':
#   app.run(port=sys.argv[1])
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
        abort(500)
    else:
        try:
            filename = img.split('/')[-1]
            local = "imgs/"+filename
            urllib.request.urlretrieve(img, local)
            colors = subprocess.run(["identify", "-format", "%k", local],
                                    stdout=subprocess.PIPE)
#            os.remove(local)
            if(colors.returncode == 0):
                return colors.stdout
            else:
                abort(500)
        except:
            abort(500)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
