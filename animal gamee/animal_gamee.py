print("Pick either Ostrich, Lion or Whale") 
print("I will attempt to guess your choice") 
print("Does the animal live in the water? Y/N") 
answer = input().lower() 
if answer == "n": 
   print("Does the animal have wings? Y/N") 
   answer = input().lower() 
   if answer == "y": 
       print("It must be an Ostrich!")
   else:
       print("It must be a Lion!") 
else: 
   print("It must be a Whale!") 
print("Pick either Carrot, Broccoli, Peas or Sweetcorn")
print("I will attempt to guess your choice of vegetables ") 
print("Is the vegetable a ball? Y/N") 
answer2= input().lower() 
if answer2== "n": 
   print("Is the vegetable orange? Y/N ") 
   answer2= input().lower() 
   if answer2== "y": 
       print("Does the vegetable look like a tree? Y/N !")
   else:
       print("It must be a Peas! ") 
else: 
   print("It must be a Carrot!") 


