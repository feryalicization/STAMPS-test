
result = []

for num in range(100, 0, -1):
    if num % 3 == 0 and num % 5 == 0:
        result.append("FooBar")
    elif num % 3 == 0:
        result.append("Foo")
    elif num % 5 == 0:
        result.append("Bar")
    elif num > 1:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if not is_prime:
            result.append(str(num))
    else:
        result.append(str(num))

result_str = ", ".join(result)

result_str += " %"

print(result_str)
