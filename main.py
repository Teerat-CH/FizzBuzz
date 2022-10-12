rule = {"fizz": 3, "buzz": 5}


def fizzbuzz(number: int) -> str:
    result = ""
    for i, j in rule.items():
        if number % j == 0:
            result += i
    if result == "":
        result += str(number)
    return result
