#!/usr/bin/python3


def yield1():
	for i in range(1, 10):
		yield i


def yield2():
	for i in range(10, 21):
		yield i


def func():
	print(list(yield from yield1()))
	

func()