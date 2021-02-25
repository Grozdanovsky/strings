string = "1000000"

final_string = ""
test_string = ""
for item in string[::-1]:
    test_string += item
    final_string += item
    if len(test_string) % 3 == 0:
        final_string += "."

print(final_string[::-1])