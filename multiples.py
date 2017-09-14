'''
MULTIPLES OF THREE AND FIVE
	From ProjectEuler.com Code Challenge 1
	If we list all the natural numbers below 10
	that are multiples of 3 or 5, we get 3, 5,
	6 and 9. The sum of these multiples is 23.

	Find the sum of all the multiples of 3 or 5 below 1000.

'''

class NumberWang():
	index = 0
	num_ary = []
	limit = ""


	def __init__( self, limit = 100 ):
		self.limit = limit
		self.number_iterator()
		print(self.summer())

	#check if number is the multiple we are looking for
	def multiple_discovery( self, number ):
		if ((number % 5 == 0) or (number % 3 == 0)):
			self.num_ary.append(number)
	
	def number_iterator( self ):
		for i in range( 0 , self.limit):
			self.multiple_discovery(i)
	
	def summer(self):
		sums = 0
		for i in self.num_ary:
			sums = sums + i
		return sums

#if __name__ == "__main__":
NumberWang(100)
