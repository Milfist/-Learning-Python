import queue

"""
    Check if a word is a palindrome using queues and stacks. It is a traditional way of doing it. We avoid nesting 
    two loops.
    There is a small example of the power of Python doing all of this in one small method. 
"""


class Palindrome:

    def __init__(self):
        self.queue = queue.Queue()
        self.stack = []

    def enqueue_character(self, character):
        self.queue.put(character)

    def push_character(self, character):
        self.stack.append(character)

    def pop_character(self):
        return self.stack.pop()

    def dequeue_character(self):
        return self.queue.get()

    def is_palindrome(self, chain):
        length = len(chain)

        for letter in range(length):
            self.push_character(chain[letter])
            self.enqueue_character(chain[letter])

        for i in range(length // 2):
            if self.pop_character() != self.dequeue_character():
                return False
                break

        return True

    def is_palindrome_space_and_upper(self, chain):
        return self.is_palindrome(str.lower(chain).replace(' ', ''))

    """   
        In python it is very easy to check if a word is a palindrome. 
        Compare the chain with itself, but going around with slicing
        Ex: chain = jamon
            chain[::-1] = nomaj
    """
    @staticmethod
    def simple_is_palindrome(chain):
        return chain == chain[::-1]
