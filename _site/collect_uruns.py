from os import listdir as ls
from os.path import isfile
types = ls('images')
counter = 0
def f(type):
    global counter
    if isfile('images/' + type):
	return
    files = ls('images/' + type)
    counter2 = 0
    for name in files:
	counter += 1
	counter2 += 1
	f = open("_urunler/%.3d.md" % counter, 'w')
	f.write('---\n')
	f.write('tip: %s\n' % type)
	f.write('referans_ismi: %d\n' % counter2)
	f.write('dosya_ismi: %s\n' % name)
	f.write('---\n')
	f.close()
map(f, types)
