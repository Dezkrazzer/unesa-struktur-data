# Creating a stack
def create_stack():
    stack = []
    return stack

# Creating an empty stack
def check_empty(stack):
    return len(stack) == 0

# Checking the size of the stack
def check_full(stack):
    return len(stack) == 10

#Adding items into the stack
def push(stack, item):
    if check_full(stack):
        print("[WARNING] Stack is full. Can't push more items")
        return
    else:
        stack.append(item)
        print(f"{item} pushed to stack")

# Removing an element from the stack
def pop(stack):
    if check_empty(stack):
        return "Stack is empty"
    return stack.pop()

stack = create_stack()
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))
push(stack, str(5))
push(stack, str(6))
push(stack, str(7))
push(stack, str(8))
push(stack, str(9))
push(stack, str(10))
push(stack, str(11))
push(stack, str(12))
# stack.clear()
print(f"Popped item: {pop(stack)}")
print(f"Stack after popping an element: {str(stack)}")