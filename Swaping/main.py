string = "32.054,23"

final = string.maketrans(".,",",.")

print(string.translate(final))