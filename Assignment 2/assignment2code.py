#Problem 1 

def reverse_sorted_words(filename):

    # YOUR CODE HERE
    words = []
    with open (filename) as f:
        lines = f.readlines()
        for line in lines:
            w = line.split(",")
            for word in w:
                words.append(word.strip("\n"))
                
    return sorted(words, reverse = True, key=lambda s: s.lower())

    #raise NotImplementedError()


#Problem 2
def reformat_student_info(filename):
    #clear the file 
    f = open('studentInfoReformatted.txt', 'w') 
    f.close()
    
    # Read the input file
    with open(filename, 'r') as input_file:
        lines = input_file.readlines()

        # Process each line
    edited_lines = []
    for line in lines:
            # Remove spaces and commas
        edited_line = line.replace(" ", "").replace(",", "")
        edited_lines.append(edited_line)
    
    for line in edited_lines: 
        netid = ''
        first_name = ''
        last_name = ''
        major = ''
        gpa = ''
        
        if_capital = False
        capital_count = 0
        major_count = 0
           
        for char in line:
            if char.isupper():
                capital_count += 1
                if_capital = True

            if not if_capital:
                netid += char
            elif capital_count == 1:
                first_name += char
            elif capital_count == 2 and not char.isdigit():
                last_name += char
           
            #
            if char.isdigit() and capital_count >= 2 and major_count < 3:
                capital_count = 3
                major += char
                major_count += 1
           
            #gets the values for the GPA using either '.' to filter / major count variable to get where we are in the string
            elif (char.isdigit() or char == ".") and capital_count >= 2 and major_count >= 3:
                gpa += char
               
        # gets rid of any whitespace before and after the variables
        netid = netid.strip()
        first_name = first_name.strip()
        last_name = last_name.strip()
        major = major.strip()
        gpa = gpa.strip()
        
        if "." not in gpa:
            gpa += ".0"

        with open('studentInfoReformatted.txt', 'a') as output_file:
            #output_file.write(netid + ", " + first_name + " " + last_name + ", " + (str)major + ", " + (str)gpa + '\n')
            output_line = "{}, {}, {}, {}\n".format(netid, first_name + " " + last_name, major, gpa)
            output_file.write(output_line)

#Problem 3
def count_word_lengths(filename):
    # YOUR CODE HERE
    d = {}
    with open (filename) as f:
        lines = f.readlines()
        for line in lines:
            w = line.split(" ")
            for word in w:
                l = len(word.strip())
                if l in d:
                    d[l] += 1
                else:
                    d[l] = 1
    
    result_list = []
    for key, value in d.items():
        result_list.append((key, value))
        
    return sorted(result_list, reverse = True, key = lambda x: x[0])

    #raise NotImplementedError()

#Problem 4
def count_last_letter(words):

    # YOUR CODE HERE
    d = {}
    w = words.split(" ")
    for word in w:
        l = word[-1:]
        if l in d:
            d[l] += 1
        else:
            d[l] = 1

    return d

   # raise NotImplementedError()

#Problem 5
def is_interesting(number, awesome_numbers):
    
    # YOUR CODE HERE
    # YOUR CODE HERE
        
    num_string = str(number) #cast to a number 
    awesome_string = [str(i) for i in awesome_numbers] #convert each element in awesome_numbers to a str
    
    #can only have three digit numbers 
    if len(num_string) < 3: 
        return 0 
    
    #check if the number is in awesome phrases
    if number in awesome_numbers: 
        return 2
    
    #check if the number is a palindrome: 
    if num_string == num_string[::-1]: 
        return 2 

    #check if the digits are sequential & decrementing 
    if num_string[::-1] in '1234567890':
        return 2
    
    #check if the digits are sequential and increasing 
    if num_string in '1234567890':
        return 2 
    
    #check if all the digits are the same
    if num_string == num_string[0] * len(num_string):
        return 2
    
    #check if all the digits following the first one are 0s
    if num_string[1:] == '0' * (len(num_string) - 1):
        return 2
    
    #we have to check the next two upcoming miles to see as well 
    for i in range(1, 3): 
        newNum_string = str(number + i) 
        if (number + i) > 99: #if any of the following conditions are true for the next two numbers, it should return 1 cause its close to being an interesting number
            if (number + i in awesome_numbers) or (newNum_string == newNum_string[::-1]) or (newNum_string[::-1] in '1234567890') or (newNum_string in '1234567890') or (newNum_string == newNum_string[0] * len(newNum_string)) or (newNum_string[1:] == '0' * (len(num_string) - 1)): 
                return 1 
    
    return 0

  #  raise NotImplementedError()
