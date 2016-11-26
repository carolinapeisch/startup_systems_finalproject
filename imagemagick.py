import subprocess
from subprocess import check_output

out = check_output(['identify', '-format', '%k', 'capture.png'])

print out


