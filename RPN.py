rpn = input("Enter your chain: ").split()
stack = []
result = 0
for i in range(len(rpn)):
    if rpn[0] == '+':
        result = float(stack[len(stack) - 2]) + float(stack[len(stack)- 1])
        stack.pop()
        stack.pop()
        stack.append(result)
        del rpn[0]
    elif rpn[0] == '-':
        result = float(stack[len(stack) - 2]) - float(stack[len(stack) - 1])
        stack.pop()
        stack.pop()
        stack.append(result)
        del rpn[0]
    elif rpn[0] == '*':
        result = float(stack[len(stack) - 2]) * float(stack[len(stack) - 1])
        stack.pop()
        stack.pop()
        stack.append(result)
        del rpn[0]
    elif rpn[0] == '/':
        result = float(stack[len(stack) - 2]) / float(stack[len(stack) - 1])
        stack.pop()
        stack.pop()
        stack.append(result)
        del rpn[0]
    elif rpn[0] == '^' or rpn[0] == '**':
        result = float(stack[len(stack) - 2]) ** float(stack[len(stack) - 1])
        stack.pop()
        stack.pop()
        stack.append(result)
        del rpn[0]
    else:
        stack.append(rpn[0])
        del rpn[0]
if len(stack) == 1 and len(rpn) == 0:
    print("Result = ", float(stack[0]))
else:
    print("Incorrect chain. Please restart program and start again.")
