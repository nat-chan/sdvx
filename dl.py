#!/usr/bin/env python
# coding:utf-8
import sys
import os
import urllib2

def dl(url):
	img = urllib2.urlopen(url)
	localfile = open(os.path.basename(url),'wb')
	localfile.write(img.read())
	img.close()
	localfile.close()

if __name__ == '__main__':
	Id = sys.argv[1]
	Num = Id[:2]
	os.mkdir(Id)
	os.chdir(Id)
	url_dir = 'http://www.sdvx.in/' + Num + '/'
	bg = url_dir + Id + '/' + Id + 'bg.png'
	bar = url_dir + Id + '/' + Id + 'bar.png'
	obj = url_dir + 'obj/data' + Id + 'e.png'
	for url in bg, bar, obj:
		dl(url)


#http://www.sdvx.in/01/01039/01039bg.png
#http://www.sdvx.in/02/obj/data02053e.png
#http://www.sdvx.in//02/02053/02053bar.png
