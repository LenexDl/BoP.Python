rpn =[]
rpn = input().split()
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
    else:
        stack.append(rpn[0])
        del rpn[0]
print(float(stack[0]))