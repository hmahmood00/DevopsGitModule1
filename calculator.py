
total = 0

with open('step_3.txt', 'r') as f:
    lines = f.read().splitlines()
    lineNumber = 1
    while lineNumber < len(lines):
        line = lines[lineNumber - 1]
        args = line.split(' ')

        print (f'Line {lineNumber}: {line}')

        command = args[0]

        if (command == 'calc'):
            operator = args[1]
            num1 = int(args[2])
            num2 = int(args[3])
            if (operator == '+'):
                result = num1 + num2
                print(result)
                total += result
            elif (operator == '-'):
                result = num1 - num2
                print(result)
                total += result
            elif (operator == 'x' or operator == '*'):
                result = num1 * num2
                print(result)
                total += result
            elif (operator == '/'):
                result = num1 / num2
                print(result)
                total += result
            lineNumber = lineNumber + 1 
        elif (command == 'goto'):
            if (args[1] == 'calc'):
                operator = args[2]
                num1 = int(args[3])
                num2 = int(args[4])
                if (operator == '+'):
                    lineNumber = num1 + num2
                elif (operator == '-'):
                    lineNumber = num1 - num2
                elif (operator == 'x' or operator == '*'):
                    lineNumber = num1 * num2
                elif (operator == '//'):
                    lineNumber = num1 / num2
            else:
                lineNumber = int(args[1])



print(f'Total: {total}')
