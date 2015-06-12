#!/usr/bin/env/ python
#-*- coding: utf-8 -*-

'Write data to a excel file'

__author__ = 'hulatang'

import xlwt
import pytz
import datetime


def getTime():
	tz = pytz.taimezone('Asia/Shanghai')
	return datetime.datetime.now(tz)

def writeXLS(item):
	wb = xlwt.Workbook()
	ws = wb.add_sheet('Ju Mei Global')


def writeData(item):
	lens = len(item)

	style0 = xlwt.XFStyle()
	style1 = xlwt.XFStyle()

#creat font
    font = xlwt.Font()
	font.name = 'Times New Roman'

#alignment
    align = xlwt.Alignment()
	align.horz = xlwt.Alignment.HORZ_CENTER
	align.vert = xlwt.Alignment.VERT_CENTER

#background color
	pattern = xlwt.Pattern()
	pattern.pattern = xlwt.Pattern.SOLID_PATTERN
	pattern.pattern_fore_colour = 5

	style0.font = font
	style0.alignment = align
	style0.pattern = pattern

	style1.font = font
	style1.alignment = align

	wb = xlwt.Workbook()
	ws = wb.add_sheet('Ju Mei Global')
	ws 
