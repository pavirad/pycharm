def get_min_list(list_val):
    list_output = []
    for x in list_val:
        if x < 5:
            list_output.append(x)
    return list_output


print(get_min_list([1, 3, 4, 5, 10, 4]))

