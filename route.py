
from flask import Flask, request
from subprocess import check_output, call
import urllib2, re
 
app = Flask(__name__)      
 
@app.route('/')
def home():
  return render_template('imagemagick.py')
 
if __name__ == '__main__':
  app.run(port=sys.argv[1])
