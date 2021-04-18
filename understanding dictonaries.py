##This program is to better explain dict()
#********************************Uncomment code to see changes*********************************

#Dictonaries allow us to work with key value pairs (hash maps, or associate of arrays

student={'name': 'David','age': 24, 'courses':['Database Management Systems','Analysis, Modeling and Design', 'Introduction to Computer Science']}

#print(student['name'])

#If we want to append a new entry into a dict() we use the method below

#student['phone']='555-5555'

#If we wanted to update multiple values at once we would use the .update() method

#student.update({'name':'Jane', 'age':26,'phone':'555-5555'})

#Let's say we want to delete some info from a dict() we would use the del function

#del student['age']

#pop method will remove and return value

#age=student.pop('age')

#print(student)

#print(age)

#print(student.get('phone'))

#We use the get method so we do not get a traceback error

#If we input a value the DNE  then the result would be none

#We can change what the result says by inputting a string in the second value spot

#print(student.get('studentID','Not Found'))

#*****************************How we can loop through key and values in our dict()
#print(len(student))
      
#print(len(student.keys()))
      
#print(len(student.values()))

#print(student.items())

for key,value in student.items():
    print(key,value)
    
