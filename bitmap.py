#!/usr/bin/env python
# coding:utf-8
#1620x786
#1340x1340
import sys
from PIL import Image
import numpy as np

import wx

class myFrame(wx.Frame):
	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, title=title)
		self.Bind(wx.EVT_PAINT, self.OnPaint)
		im = Image.open('data02053e.png').convert("RGBA")
		mt = np.asarray(im)
		self.bitmap = \
		wx.BitmapFromBufferRGBA(mt.shape[1], mt.shape[0], mt.tostring())

		self.SetSize((mt.shape[1], mt.shape[0]))

	def OnPaint(self, event=None):
		dc = wx.PaintDC(self)
		dc.DrawBitmap(self.bitmap, 0, 0, True)

app = wx.App(False)
frame = myFrame(None, "sdvx")
frame.Show()
app.MainLoop()

