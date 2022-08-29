'''
PART 1:
- Create a new class called Author 

- An author class has a name and
 a list of books the publisher nas written

-Author class should have a publish method 
Which adds the book titles to the class book list

-Create a main function to test class   

PART 2:
-Prevent books list from listing duplicate books 
'''


class Author:
    #What does the Author class include?
    def __init__(self, name):
        self.name = name
        #new author class objects have no books
        self.book_list = []
    
    #need a way to insert books into the book list
    def Publish(self, title):
        # if the book is not already in the Authors book list:
        if title not in self.book_list: 
            self.book_list.append(title)
        else: #but if the book is in the list already:
            print(f'{title} already in list')


        

    def __str__(self):
        titles = ', '.join(self.book_list) or 'No published books' #tested: does say no publuished books
        return f'Author name: {self.name}, books written : {titles}'

def Main():

    s_king = Author('Steven King')
    s_king.Publish('The Shining')
    s_king.Publish('Fairy Tale')
    s_king.Publish('It: A Novel')
    s_king.Publish('Fairy Tale')
    
    
    print(s_king)

Main()
