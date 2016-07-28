#!/usr/bin/env python
# coding:utf-8
#1620x786
#1340x1340
import sys
from PIL import Image
import numpy as np
import cv2

import wx

class myFrame(wx.Frame):
	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, title=title)
		self.SetBackgroundColour('black')
		self.timer = wx.Timer(self)
		self.Bind(wx.EVT_TIMER, self.OnTimer)
#		self.Bind(wx.EVT_PAINT, self.OnPaint)
		image = Image.open('out.png').convert("RGBA")
		self.array = np.asarray(image)
		self.counter = -1
		self.SetSize((55, 200))
		self.timer.Start(6)
		self.psp = np.array([
			[  1.27272727e-01,  -1.20000000e-01,   2.40000000e+01],
			[ -1.22124533e-15,  -1.22727273e-01,   5.00000000e+01],
			[ -5.63785130e-18,  -4.36363636e-03,   1.00000000e+00]
		])

	def OnTimer(self, event):
		self.counter += 1
		i = self.counter
		part = self.array[-1-200-i:-1-i,:,:]
		part = cv2.warpPerspective(part,self.psp,part.shape[1::-1])
		if part.shape == (200, 55, 4):
			bitmap = wx.BitmapFromBufferRGBA(55, 200, part.tostring())
			dc = wx.PaintDC(self)
			dc.DrawBitmap(bitmap, 0, 0, True)
		else:
			self.timer.Stop()
#	def OnPaint(self, event=None):
#		dc = wx.PaintDC(self)
#		dc.DrawBitmap(self.bitmap, 0, 0, True)

app = wx.App(False)
frame = myFrame(None, "sdvx")
frame.Show()
app.MainLoop()

