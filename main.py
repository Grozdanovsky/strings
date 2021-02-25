def counthing_char(list1):
    dict = {}
    for item in list1:
        if item not in dict.keys():
            dict.update({item : list1.count(item)})
    return dict


# Main
string = "google.com"
list1 = [item for item in string]

print(counthing_char(list1))




