"""
Reverse the string
"""

# Approach 1 :  

def reverseString(text:str)-> str:
  start = 0 
  end = len(text)-1 
  n = len(text)//2 
  while start <= end :
    text[start], text[end] = text[end], text[start]
    start += 1 
    end -= 1 
  word = "".join(text)
  return word 
