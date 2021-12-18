def comma_code(list):
    s = ""
    for ele in list:
        if list.index(ele) == 0:
            s = s + ele
        elif list.index(ele) == (len(list) -1):
            s = s + ", and " + ele
        else:
            s = s + ", " + ele
    return s
        

a = ["ab", "cd", "ef", "gh", "ij"]
print(comma_code(a))