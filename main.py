def interleave(str1, str2):
    new_list = list(zip(str1, str2))
    return "".join(["".join(item) for item in new_list])


print(interleave('hi', 'ha'))
