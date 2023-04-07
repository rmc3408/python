class Book:

    def __init__(self, title, pages):
        self.title = title
        self.author = "John Doe"
        self.pages = pages
        print('# BOOK #')

    def __str__(self):  # Override from Object class.
        return f'published book {self.title} '
    
    def __len__(self):
        return self.pages
   

class Magazine(Book):
    
    def __init__(self, title, author, pages):
        # Option 01 - using super, no self
        # super().__init__(title, pages)

        # Option 02 - Call superclass
        Book.__init__(self, title, pages)
        self.author = author
        print('@ MAGAZINE @')

    def __str__(self):
        return 'Graphical Magazine with ' + Book.__str__(self) + f'by {self.author}'


print()
print('------   Dunder Method    --------')
b = Book('Python', 200)
# If not override show <__main__.Book object at 0x049438>
print(str(b))
print(len(b))
print()

d = Magazine('MenHealth', "Raphael", 78)
print(str(d))
