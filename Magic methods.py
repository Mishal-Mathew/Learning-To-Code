
class Book:

    def __init__(self,name , author , num_pages):
        self.name =name
        self.author = author
        self.num_pages = num_pages
    
    def __str__(self):
        return f"{self.name} by {self.author}"

    def __eq__(self,other):
        if self.name == other.name and self.author == other.author:
            return f"{self.name} and {other.name} are the same"
        else:
            return f"{self.name} and {other.name} are not the same"

    def __lt__(self , other):
        if self.num_pages < other.num_pages:
            return f"{self.name} have less pages than {other.name}"
        else:
            return f"{self.name} do not have less pages than {other.name}"
    def __gt__(self,other):
        if self.num_pages > other.num_pages:
            return f"{self.name} have more pages than {other.name}"
        else:
            return f"{self.name} do not have more pages than {other.name}"

    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"
    
    def __contains__(self,keyword):
        return keyword in self.author or keyword in self.name

    def __getitem__(self,key):
        if key == "title":
            return self.name
        elif key == "author":
            return self.author
        elif key == "num of pages":
            return self.num_pages
        else:
            return f"The key '{key}' is invalid"

book1 = Book("The Hobbit" , "J.R.R Tolkien", 250)
book2 = Book("Harry Potter" , "J.K Rowling" , 332)

print(book1)
print(book1 == book2)
print(book1 < book2)
print(book1 + book2)
print("Hobbit" in book1)
print(book1['audio'])