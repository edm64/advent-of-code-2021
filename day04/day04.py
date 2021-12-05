#!/usr/bin/python3
from collections import defaultdict as ddict

# I liked the solution I wrote that counts diagonals, then reread the instructions. I don't have the heart to delete that part, so it's staying in with a toggle.
includeDiagonals = False

debug = True

def dprint(s):
	if debug:
		print(s)

def bingOrder(x):
	# override alphanumerical sort, for more readable __repr__
	return "12345BINGO/\\".index(x)


class Card:
	def __init__(self, numbers):
		# dict containing all number positions as lists
		self.squares = ddict(lambda:[])
		# track marks in each possible win line, keyed by row (01234), col (BINGO), and diagonals (/\)
		self.lanes = ddict(lambda:0)

		# expecting to read in exactly 5 rows
		for r in range(5):
			row = numbers[r].split()
			for c in range(5):
				q = int(row[c])
				# note which rows/cols/diags that number is in
				self.squares[q] += [str(r+1), "BINGO"[c]]
				if includeDiagonals and r==c:
					self.squares[q].append("\\")
				if includeDiagonals and r+c==4:
					self.squares[q].append('/')


	def call(self, number):
		# mark the number in any rows/cols/diagonals on this card
		q = self.squares.pop(number, None)
		if q is not None:
			dprint(q)
			for lane in q:
				self.lanes[lane] += 1
			for j in sorted(self.lanes, key=bingOrder):
				dprint(f"{j}, {self.lanes[j]}")

	def bingo(self):
		# returns True if this card has 5 in a row
		return any([lane>=5 for lane in self.lanes.values()])

	def score(self):
		# calculate sum of unmarked squares
		return sum(self.squares.keys())


cards=[]
with open("input04.txt",'r') as inputte:
	# first line is called numbers
	sequence = [int(n) for n in inputte.readline().strip().split(',')]

	# this loop condition eats the blank newline between each card
	while inputte.readline() != '':
		cards.append(Card([inputte.readline().strip() for c in "BINGO"]))

k=0
for number in sequence:
	k+=1
	dprint(f">>{number}<<  ({k})")
	for card in cards:
		card.call(number)
	winners = [c.score() for c in cards if c.bingo()]
	if winners:
		dprint(winners)
		break

# part 1 solution
print(max(winners)*number)
