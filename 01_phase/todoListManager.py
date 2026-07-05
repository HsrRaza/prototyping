todos = []

def todo_manager():
    while True:
        user_input = input("Enter a todo item (or type 'ex' to quit): ")
        if user_input.lower() == 'ex':
            break
        todos.append(user_input)


todo_manager()

print("Your todo list:")
for index , todo in enumerate(todos, start=1):
    print(f"{index}, {todo}")
        
        
