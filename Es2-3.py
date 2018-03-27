from sys import argv
filename=argv[1]
file=open(filename)
L=[]

testo=file.read()
file.close()
Text=testo.split("\n")

for task in Text:
    L.append(task)

print(L)

stng = "Choose action \n 1 insert a new task \n 2 remove a task \n 3 show all existing tasks sorted in alphabetic order  \n 4 close the program \n 5 Delete by substring"


while 1 == 1:
  print(stng)
  action = int(input())

  if action == 1:
        print("Insert task to be added")
        task = input()
        L.append(task)

  if action == 2:
        print("Insert task to be removed")
        task = input()
        L.remove(task)

  if action == 3:
        print("That's the list: \n")
        print(sorted(L, key=lambda x: x.upper()))

  if action == 4:
        file=open(filename,"w")
        for task in L:
         file.write(task+"\n")

        file.close()
        exit()
  if action==5:
       print("Insert substring")
       count=0
       subs=input()
       for s in reversed(L):
           if subs in s:
               L.remove(s)






