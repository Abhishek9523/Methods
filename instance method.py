class Student:
    def display(self):
        print("this is display method")
    def show(self):  
        self.display()  
        print("this from show method")
        
obj=Student()
obj.show()        