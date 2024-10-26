def reverse_string(s):
    s=str(s)
    return s[::-1]
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str 

# Test the function
print(reverse_string("Hacktoberfest"))  
print(reverse_string("12345"))         
print(reverse_string(""))            
