class publication:
    total_publication = 0
    def __init__(self,name):
        self.name = name

    def print_information(self):
        print(self.name, end=" ")

class book(publication):
    def __init__(self,name,author,pages):
        super().__init__(name)
        self.author = author
        self.pages = pages

    def print_information(self):
        super().print_information()
        print(f" is writen by {self.author},{str(self.pages)} pages")

class magazine(publication):
    def __init__(self,name, editor):
        super().__init__(name)
        self.editor = editor

    def print_information(self):
        super().print_information()
        print(f" is the magazine edited by {self.editor}")

pub=[]
pub.append(magazine("VOLT","AKIE"))
pub.append(book("CONAN","HIGASAKI", 201))
for i in pub:
    i.print_information()

