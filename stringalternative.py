def string_alternative(str):
    result = ""
    for i in range(len(str)):
        if i % 2 == 0:
            result = result + str[i]
    return result

print(string_alternative('hello world'))