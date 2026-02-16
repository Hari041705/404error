# Team Name: 404error
def calculate(expression: str) -> float:
    tokens = expression.replace(" ", "")
    nums = []
    ops = []
    i = 0
    while i < len(tokens):
        if tokens[i] in "+-*/":
            ops.append(tokens[i])
            i += 1
        else:
            j = i
            while j < len(tokens) and tokens[j] not in "+-*/":
                j += 1
            nums.append(float(tokens[i:j]))
            i = j
    i = 0
    while i < len(ops):
        if ops[i] == '*':
            nums[i] = nums[i] * nums[i+1]
            nums.pop(i+1)
            ops.pop(i)
        elif ops[i] == '/':
            nums[i] = nums[i] / nums[i+1]
            nums.pop(i+1)
            ops.pop(i)
        else:
            i += 1
    result = nums[0]
    for i, op in enumerate(ops):
        if op == '+':
            result += nums[i+1]
        else:
            result -= nums[i+1]
    return round(result, 2)
