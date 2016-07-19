#!/usr/bin/env python
# coding:utf-8
import sys
from PIL import Image
import numpy as np

def cutout(arr):
	'''
	譜面の展開図をレーンの配列に切り分ける
	'''
	return [
		arr[:,i:i+55,:]
		for i in range(
			12, arr.shape[1]-55+1, 70
		)
	]

def grayline(lane):
	'''
	レーンから小節を表す灰線のy座標を返す
	ちなみに小節を区切っている線はbar lineといいます。
	'''
	gray = [204, 204, 204, 255]
	sample = lane[:,8,:]
	return [
		i for i, col in enumerate(sample)
		if all(col == gray)
	]

def cutlane(bg, data):
	bar = grayline(bg)
	tier = bg + data           #TODO 画像の重ねあわせ
	ran = zip(bar[:-1],bar[1:])
	return [tier[r[0]:r[1],:,:] for r in ran]

def measure(bg, data):
	'''
	譜面展開図から小節ごとの配列に直す
	'''
	return reduce(
		lambda a,b:a+b,
		[
			cutlane(*two)
			for two in zip(cutout(bg),cutout(data))
		][::-1]
	)
	#np.r_[tuple(k)]

if __name__ == '__main__':
	bg, data = [
		np.array(
			Image.open(f).convert("RGBA")
		)
		for f in sys.argv[1:]
	]
	arr = measure(bg, data)
	mt = np.r_[tuple(arr)]
	MT = Image.fromarray(mt)
	MT.save('out.png')
