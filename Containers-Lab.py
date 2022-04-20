#1
students = ['Katie', 'Wilson', 'Nia', 'Ryan']

print(students[0])
print(students[-1])

#2
foods = ('corn', 'steak', 'cheesecake', 'calamari')
for i in foods:
    print(i + " is a good food")


#3
for x in foods:
  if (x == foods[-2] or x == foods[-1]):
    print (x)

#4
home_town = {
  'city': 'Vallejo',
  'state': 'California',
  'population': 100999222
}
print(f"I was born in {home_town['city']}, {home_town['state']} - populatin of {home_town['population']}")


#5
for key in home_town:
   print(f"{key} : {home_town[key]}")
   

#6

cohort = []

for x in students:
  cohort.append(x)
  
print(cohort)

#7
awesome_students = []

for x in students:
  awesome_students.append(f"{x} is awesome!")
  
print(awesome_students)


#8
a_letters = []
for x in foods:
  if "a" in x:
    a_letters.append(x)

print(a_letters)
