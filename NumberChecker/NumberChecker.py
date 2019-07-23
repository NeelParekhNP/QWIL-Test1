def myFunction(input):
    string_count = input
    count = int(string_count)
    # Checks if the input is a natural number
    # If input is not a natural number it returns -1
    if count <= 0:
        return str(-1)
    count_length = len(string_count)
    count_integer_list = [int(d) for d in str(count)]
    new_count_integer_list = []
    total = 0
    new_total = 0
    #Calculates the sum of all integers in the input
    for number in count_integer_list:
        total += number
    #Checks if input is between 0 to 15 (not inclusive)
    if count_length <= 0 or count_length >= 15:
        return str(-1)
    else:
        #Looks for the minimal next number with the same sum of digits 
        while total != new_total:
            new_total = 0
            count += 1
            new_count_integer_list = [int(d) for d in str(count)]
            for number in new_count_integer_list:
                new_total += number
        #Checks if the minimal number is longer than the input number
        #Returns -1 if true
        if count_length < len(str(count)):
            return str(-1)
        #Adds leading zeros to new nuumber if necessary
        elif len(str(count)) < count_length:
            return str(count).zfill(count_length)
        #Returns minmial number without any alterations
        else:
            return str(count);
    
