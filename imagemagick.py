import subprocess
from subprocess import check_output

# subprocess.call(['identify', '-format', '%k', 'test.png'])

out = check_output(['identify', '-format', '%k', 'test.png'])

print out

