import queue

"""
    Check if a word is a palindrome using queues and stacks. Is traditional  
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

    """   
        In python it is very easy to check if a word is a palindrome. 
        Compare the chain with itself, but going around with slicing
        Ex: chain = jamon
            chain[::-1] = nomaj
    """
    @staticmethod
    def simple_is_palindrome(chain):
        return chain == chain[::-1]


# print("Enter a word: ")
#
# input_data = input()
#
# obj = Palindrome()
#
# if obj.is_palindrome(input_data):
#     print("The word, " + input_data + ", is a palindrome.")
# else:
#     print("The word, " + input_data + ", is not a palindrome.")
#
# print("simple_is_palindrome")
# print(obj.simple_is_palindrome(input_data))
#
#
# list1 = ['physics', 'chemistry', 1997, 2000]
# list2 = [1, 2, 3, 4, 5, 6, 7 ]
#
# print ("list1[0]: ", list1[0])
# print ("list2[1:5]: ", list2[::-1])