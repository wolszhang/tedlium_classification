import codecs
import os
dic = {}
with codecs.open("log.txt", "r",encoding='utf-8', errors='ignore') as inp:
	for line in inp:
		title = line.split(":")[0]
		label = line.split(":")[1]
		if title not in dic:
			dic[title] = [label]
		else:
			dic[title].append(label)

		if title[-1].isdigit():
			k = int(title[-1])
			title = title[:-1]+str(k+1)
			if title not in dic:
				dic[title] = [label]
			else:
				dic[title].append(label)
			title = title[:-1]+str(k-1)
			if title not in dic:
				dic[title] = [label]
			else:
				dic[title].append(label)



ct = 0
prob = 0

with open("files.txt","r") as inp:
	for line in inp:
		ct += 1
		c = 0
		temp = line.replace(".stm","")[:-1]
		if not temp[-1].isdigit():
			temp = temp[:-1]
		for key in dic:
			if temp in key:
				prob += 1
				c = 1
		if c==0:
			print(temp)
print(prob)
print(ct)