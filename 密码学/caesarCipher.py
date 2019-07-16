# -*- coding: utf-8 -*-
'''
凯撒加密法
'''

def code(s,k):
	rt=[]
	for c in s.upper():
		if c in string.ascii_uppercase:
			n=ord(c)+k
			if n>90:
				n=n-26
			c=chr(n)
		rt.append(c)
	return ''.join(rt)

def decode(s,k):
	rt=[]
	for c in s.upper():
		if c in string.ascii_uppercase:
			n=ord(c)-k
			if n<65:
				n=n+26
			c=chr(n)
		rt.append(c)
	return ''.join(rt)
