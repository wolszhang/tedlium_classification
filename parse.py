import codecs
import os
dic = {}
yr = [2015,2016,2017,2018]
with codecs.open("res.txt", "r",encoding='utf-8', errors='ignore') as inp:
	for line in inp:
		flag = 0
		title = line.split(":")[0]
		idx = title.rfind(" ")
		title=title[:idx]+"_"+title[idx+1:]
		title = title.replace(" ","")
		label = line.split(":")[1][:-1]
		dic[title] = label
		for y in yr:
			if str(y) in title:
				flag = 1
		if flag == 0:
			print(title+":"+label)
