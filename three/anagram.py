'''
Question 1: Anagram Checker

Problem Statement:
Write a function `is_anagram(s1, s2)` that checks if two strings `s1` and `s2` are anagrams of each other.
An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
 typically using all the original letters exactly once.

Function Signature:
```python
def is_anagram(s1: str, s2: str) -> bool:
```

Example:
```python
assert is_anagram("listen", "silent") == True
assert is_anagram("triangle", "integral") == True
assert is_anagram("apple", "pale") == False '''
def anagram(str11, str2):
  if len(str1)==len(str2):
    if sorted(str1)==sorted(str2):
      print("true")
  else:
    print("false")
str1=input("Enter a string: ")
str2=input("Enter a string: ")
anagram(str1, str2)
