'''
    PROJECT EULER CODE CHALLENGE 2

        Each new term in the Fibonacci sequence is generated 
        by adding the previous two terms. By starting with 1
        and 2, the first 10 terms will be:

        1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

        By considering the terms in the Fibonacci sequence
        whose values do not exceed four million, find the sum
        of the even-valued terms.

'''

class EvenFibs:
    fibs = [1, 2]
    size_limit = 0

    def __init__(self, size_limit=4000000):
        self.size_limit = size_limit
        self.run_sequence()
        print self.sum_evens()

    def run_sequence(self):
        add = 3
        while add < self.size_limit:
            add = self.fibs[len(self.fibs) - 1] + self.fibs[len(self.fibs)-2]
            if add < self.size_limit:
                self.fibs.append(add)

    def sum_evens(self):
        tot = 0
        for val in self.fibs:
            if val % 2 == 0:
                tot = tot+val
        return tot

EvenFibs()