#1. Primes: Write a function to return all the prime numbers less than n, where n is a parameter (assume n > 2) 

def primes(n):
    """Returns all prime numbers from 2 to n (excluding n) """
    
    # YOUR CODE HERE
    prime_list = []
    
    for i in range(2, n): #for every number starting at 2 and up to n (excluding n)
        for j in range(2, int(i**0.5)+1): #for every divisor from 2 - n (n is not included)
            if i%j == 0:
                break
        else: 
            prime_list.append(i)

    return prime_list



#2. Factor: Write a function to return all the prime factors of n, where n is a parameter (Hint: you can call your primes function from the previous problem) 

def factor(n):
    """Return all the prime factors of n."""
    # YOUR CODE HERE
    #keep dividing the input number by the prime numbers less than it (using the previous function)
    #once you divide the input number by the prime number, you can add that to the prime factorization for the number 
    #and you can continue doing that, until you reach the last of the prime factorization
    
    #you first need to get the prime factors of the input and use those numbers to continue dividing the input integer 
    #while doing the division, you need to keep track of the numbers you're dividing by in another list cause they are the prime factors
    prime_numbers = primes(n) 
    prime_factors = []
    
    if n == 2: 
        prime_factors.append(2)
        n //= 2
    
    for i in prime_numbers: 
        if n%i == 0: #if the input is divisible by that prime numer
            prime_factors.append(i) #add that number to the prime factors list
            n //= i     #divide the input parameter by that prime number
            while n%i == 0: #we have to continue dividing the i by the prime factors until we cannot anymore, therefore we use the while loop to continue dividing
                prime_factors.append(i) #append 
                n //= i            
    
    return prime_factors


#3. Decreasing_digits: Write a function called decreasing_digits to count all integers from 1 to n (inclusive) that have all digits in decreasing order, where n is given as a parameter 

 def decreasing_digits(n):
    """ Returns the number of integers from 1 to $n$ (inclusive) 
    that have all digits in decreasing order, where $n$ is
    given as a parameter. 
    """
    # YOUR CODE HERE
    
    #in order to traverse the string, we have to individually check through each of the elements 
    #by converting an int to a string, you would be able to check each individual element in the int 
    
    """ the below code would only work for one digit, and we need to make it work for all the digits
    for i in range(size - 1): #because indexing starts at 0 so you have to subtract one from length 
        for j in range(i + 1, size): 
            if(string_num[i] > string_num[j]): 
                count += 1

    return count
    """
    
    #the above code would only work for one pair of adjacent digits
    #to check for other digits, we need to check ALL adjacent pairs so we can use a boolean variable and break out of the loop everytime its false  
    
    """
    count = 0
    string_num = str(n) 
    
    size = len(string_num)
    for i in range(size): 
        check = True
        for j in range(i + 1, size): 
            if(string_num[i] > string_num[j]): 
                continue 
            else: 
                check = False
        if check == True: 
            count+= 1
    
    return count"""
    
    count = 0
    for i in range(1, n + 1):
        check = True
        string_num = str(i) 
        size = len(string_num)
        for j in range(size - 1):
            if int(string_num[j]) > int(string_num[j + 1]):
                continue
            else:
                check = False
                break  # No need to continue checking if one comparison fails
        if check:
            count += 1
        
    return count


#4. Stats : Write a function called stats to return the mean and median of a list of integers given as a parameter 

def stats(ints):
    """ 
    Returns a dictionary containing 
    the "mean" and "median" of a 
    list of integers given as a parameter. 
    """
    # YOUR CODE HERE
    
    #for i in sorted_list: 
     # sum += i 
     #  count += 1
    
   # mean = sum / count
#you do not need to do it the above way because 

    sorted_list = sorted(ints) 
    list_size = len(sorted_list)
    
    sum1 = sum(sorted_list)
    mean = sum1 / list_size
    
    if list_size % 2 == 1: 
        median = float(sorted_list[list_size // 2])
    else:
        num1 = sorted_list[(list_size // 2) - 1] 
        num2 = sorted_list[list_size // 2]
        median = ((num1 + num2) / 2)
    
    stats_dict = {"mean" : mean, "median" : median}
    
    return stats_dict

#5. one_triples: Write a function called one_triples to return all triples in a list of integers that sum to one. You can assume the list won’t contain any duplicates, and a triple should not use the same number more than once. All triples should be returned in a list of tuples, where each tuple is in sorted order. 

def one_triples(ints):
    """ 
    Returns all triples in a list of integers that sum to zero. 
    The list of integers is given as a parameter. 
    Assumes the list will not contain any duplicates, and a triple 
    should not use the same number more than once.
    """
    # YOUR CODE HERE
    
    #use a triple nested for loop to traverse through every potential triple pair that adds up to 1
    
    size = len(ints)
    result = []
    
    for i in range(0, size - 2):
        for j in range(i + 1, size - 1): 
            for k in range(j + 1, size): 
                if ints[i] + ints[j] + ints[k] == 1:
                    result.append((ints[i], ints[j], ints[k]))
        
    sorted_tuple_list = []
    
    for sorted_tuple in result: 
        sorted_tuple_list.append(tuple(sorted(sorted_tuple)))
        
    return sorted_tuple_list


