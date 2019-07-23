def myFunction(input):
    string_count = input
    count = int(string_count)
    if count <= 0:
        return str(-1)
    count_length = len(string_count)
    count_integer_list = [int(d) for d in str(count)]
    new_count_integer_list = []
    total = 0
    new_total = 0
    for number in count_integer_list:
        total += number
    if count_length <= 0 or count_length >= 15:
        return str(-1)
    else:
        while total != new_total:
            new_total = 0
            count += 1
            new_count_integer_list = [int(d) for d in str(count)]
            for number in new_count_integer_list:
                new_total += number
        if count_length < len(str(count)):
            return str(-1)
        elif len(str(count)) < count_length:
            return str(count).zfill(count_length)
        else:
            return str(count);
    
