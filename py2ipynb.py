import glob

def convert(file):
	from IPython.nbformat import v3, v4
	with open(file + ".py") as fpin:
		text = fpin.read()
	nbook = v3.reads_py(text)
	nbook = v4.upgrade(nbook)  # Upgrade v3 to v4
	jsonform = v4.writes(nbook) + "\n"
	with open(file + ".ipynb", "w") as fpout:
		fpout.write(jsonform)

#	import nbformat as nbf
#	nb = nbf.read(open(file + '.py', 'r'), 'py')
#	nbf.write(nb, open(file + '.ipynb', 'w'), 'ipynb')

files = glob.glob('./*.py')

import os.path
[convert(os.path.splitext(f)[0]) for f in files]