def fizzbuzz(number: int) -> str:
    result = ""
    if number % 3 == 0:
        result += "fizz"
    if number % 5 == 0:
        result += "buzz"
    if result == "":
        result += str(number)
    return result
