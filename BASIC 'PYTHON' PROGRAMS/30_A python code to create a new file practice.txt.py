'''
=>By Adding the following data:
1.Hi everyone
2.We are learning File I/O.
3.Using Python.
4.I like programing in Python.
'''

class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("Hello",self.name, "\nYour Average Marks is: ",sum/3)

s1=student("Suraj katwal",[99,98,99])
s1.get_avg()