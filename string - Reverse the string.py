"""
Reverse the string
"""

# Approach 1 :  string to list & two pointers method

def reverseString(text:str)-> str:
  start = 0 
  end = len(text)-1 

  while start <= end :
    text[start], text[end] = text[end], text[start]
    start += 1 
    end -= 1 
  return "".join(text) 

"""
Time Complexity : O(n)
Space Complexity : O(n) -> new string reversed string creation
"""



# Approach 2 : 

def ReverseStr(text:str):
  new_list = list(text)
  text = new_list[::-1]
  return "".join(text)

text = "Data"
x = ReverseStr(text)
print(x)
