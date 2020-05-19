class Book:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        print('# BOOK #')

    def __str__(self): #Override from Object class.
        return f'String method from book {self.title} by {self.author}.'
    
    def __len__(self):
        return self.pages
   

class Magazine(Book):
    
    def __init__(self, title, pages):
        super().__init__(self, title, pages)
        print('@ MAGAZINE @')

    def __str__(self):
        return 'Graphical Magazine: ' + Book.__str__(self)

print()
print('------   Dunder Method    --------')
b = Book('Python', 'Raph', 200)
# If not override show <__main__.Book object at 0x049438>
print(str(b))
print(len(b))
print()

d = Magazine('MenHealth', 78)
print(str(d))