import queue

"""
    Check if a word is a palindrome using queues and stacks. It is a traditional way of doing it. We avoid nesting 
    two loops.
    There is a small example of the power of Python doing all of this in one small method. 
    Big O notation --> O = N ^ 2
    
"""


class Palindrome:

    def __init__(self):
        self.queue = queue.Queue()
        self.stack = []

    def is_palindrome(self, chain):
        length = len(chain)

        for letter in range(length):
            self.stack.append(chain[letter])
            self.queue.put(chain[letter])

        for i in range(length // 2):
            if self.stack.pop() != self.queue.get():
                return False
                break

        return True

    def is_palindrome_space_and_upper(self, chain):
        return self.is_palindrome(str.lower(chain).replace(' ', ''))

    """   
        Compare the chain with itself, but going around with slicing
        Ex: chain = jamon
            chain[::-1] = nomaj
            return False
        Ex: chain = oso
            chain[::-1] = oso
            :return True
    """
    @staticmethod
    def simple_is_palindrome(chain):
        return chain == chain[::-1]
