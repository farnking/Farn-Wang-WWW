import unittest

def question1(a,n):
    #this function should return the a to the power of n
    return n*a

def question2(num):
    #if the input number is prime return true, else return false
    for c in range(2,num):
        if(num%c==0):
            return True
            break
        elif c == num-1:
            return False
    if num == 2:
        return True

def question3(target,nums):
    """
    two sum problem
    this function input a list and an integer, it should return indices of the two number 
    such that add up to target
    ex: nums = [5,6,7,8] , target  = 13
        the function will return [0,4] #5+8 = 13
    """
    h = {}
    for i,num in enumerate(nums):
        n = target-num
        if n in h:
            h[num] = i
        else:
            return [h[n],i]

def question4(num_list):
    #this is a bubble sort implementation function, it should return a descending sort
    list_length = len(num_list)
    for i in range(0, list_length):
        for j in range(i + 1, list_length):
            if num_list[i] > num_list[j]:
                num_list[i], num_list[j] = num_list[j], num_list[i]
    return num_list

def question5(num_list):
    #this is a insert sort function, it should return a Ascending sort
    num_list_length = len(num_list)
    for i in range(1, num_list_length):
        insert_value = num_list[i]
        j = i - 1
        while j >= 0:
            if num_list[j] > insert_value:
                num_list[j + 1] = num_list[j]
                num_list[j] = insert_value
            j -= 1
    return num_list

def question6(a,b):
    #this function input 2 int number, return a*b, but the return type of a*b should be the string type
    return a*b

def question7(num_list,target):
    #this function input a list and a target number, the target number will be delete from the list, return list
    #if the target number not in the list, return none
    #Notice! the "target" is a number, not a indice
    num_list.pop(target)
    return num_list

def question8(num_list):
    #this is a selection sort function, it will return an ascending sort array
    num_list_length = len(num_list)
    for i in range(0, num_list_length):
        min_num_index = i
        for j in range(i + 1, num_list_length):
            if num_list[min_num_index] > num_list[j]:
                min_num_index = j
        num_list[min_num_index], num_list[i] = num_list[i], num_list[min_num_index]

    return num_list

def question9(a,b,c):
    #this function input two string, return their string concatenation
    #example: a = 'abc', b= 'def',c = 'ghi', than the return string is 'abcdefghi'
    #if any of the input of the string is null, than return none
    return a+b+c

def question10(num_list):
    #this function get a list input, return the number of the all number sum in the list,except the first number
    total = 0 
    for i in num_list:
        total = total + i
    return total



class Test(unittest.TestCase):        
    def test_question1(self):
        #todo    
    def test_question2(self):
        #todo
    def test_question3(self):
        #todo
    def test_question4(self):
        #todo
    def test_question5(self):
        #todo
    def test_question6(self):
        #todo
    def test_question7(self):
        #todo
    def test_question8(self):
        #todo
    def test_question9(self):
        #todo
    def test_question10(self):
        #todo



if __name__ == '__main__':
    unittest.main()
