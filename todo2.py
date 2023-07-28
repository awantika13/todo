from function import get_todos,write_todos
import time

now = time.strftime("%b %d %Y, %H : %M %S")
print("the time is below :")
print("it is", now)


while True:
     user_action= input(" type add,edit,complete or show ")
     user_action= user_action.strip()

     if user_action.startswith("add"):
         todo= user_action[4:]

         todos= get_todos()

         todos.append(todo+'\n')

         write_todos(todos,"todos.txt")

     elif user_action.startswith("show"):

         todos = get_todos()

         for index,item in enumerate(todos):

             item=item.strip("\n")

             row= f"{index +1}-{item}"

             print(row)

     elif user_action.startswith("edit"):

         try:
             imp = int(user_action[5:])
             print(imp)
             imp = imp-1

             todos = get_todos()

             todo_new = input(" enter the new todo")

             todos[imp]= todo_new  +'\n'

             write_todos(todos,"todos.txt")
         except ValueError:
             print("Your Command i not Valid")
             continue

     elif user_action.startswith("complete"):

         try:
             number = int(user_action[9:])

             todos = get_todos()
             index= number-1
             todo_to_remove= todos[index].strip("\n")
             todos.pop(index)

             write_todos(todos,"todos.txt")

             message=f"todo { todo_to_remove} was removed from the list"
             print(message)
         except IndexError:
             print("Index with that number is not present")
             continue

     elif user_action.startswith("exit"):
         break
     else:
         print(" command is invalid")