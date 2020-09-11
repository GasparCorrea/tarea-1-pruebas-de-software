from datetime import datetime

# Function to be tested
# Compares the lenght of two strings and returns the largest
def compareStringLength(str1,str2):
    try:
        # If any of arguments is not string, raise exception
        if not type(str1) is str:
            raise TypeError(str1)
        if not type(str2) is str:
            raise TypeError(str2)
        # Compare length of strings, if they are equal in length, returns str2
        if len(str1) > len(str2): return str1
        else: return str2
    except TypeError as e:
        now = datetime.now()
        print(now," - Error: Only strings allowed ",e," is not a string.")

# Testing procedure
with open("test_cases.txt","r",encoding="utf-8") as file:
    now = datetime.now()
    print(now," - Testing: Reading test_cases.txt")
    tests = file.read().split("\n")
    total_correct = 0
    total = len(tests)
    for test in tests:
        str1,str2,expected = test.split(",")
        now = datetime.now()
        result = compareStringLength(str1,str2)
        correct = expected == result
        if correct:
            total_correct = total_correct + 1 
        print(now," - Testing: str1: ", str1,", str2:",str2,", expected:",expected,", result:", result, ", correct:", correct)
    now = datetime.now()
    print(now," - Finished: ", total_correct," of ",total," cases were correct.")
    

