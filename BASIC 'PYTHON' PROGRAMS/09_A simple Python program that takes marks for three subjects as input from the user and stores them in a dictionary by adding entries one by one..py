"""A simple Python program that takes marks for three subjects as input
from the user and stores them in a dictionary(starting with empty Dictionary)
by adding entries one by one, using subject names as keys and marks as value."""

marks={}
mark1=int(input("Physics marks: "))
marks.update({"Physics:":mark1})
mark2=int(input("Chemistry marks: "))
marks.update({"Chemistry":mark2})
mark3=int(input("Maths marks: "))
marks.update({"Maths":mark3})
print(marks)