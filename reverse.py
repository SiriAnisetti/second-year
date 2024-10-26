def reverse_string(s):
    s=str(s)
    return s[::-1]
    reversed_str = ""
    for char in s:
        reversed_str = char+reversed_str
    return reversed_str
        reversed_str = char + reversed_str
    return reversed_str  # Fix the return statement

print(reverse_string("Hacktoberfest"))
print(reverse_string("12345"))  # This should be a string
print(reverse_string(""))  # This will test with an empty string
    return reversed_str 

print(reverse_string("Hacktoberfest"))  
print(reverse_string("12345"))         
print(reverse_string(""))             
print(reverse_string(""))            
