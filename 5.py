# 11
import re

s = input("Введите строку: ")

longest_sequence = len(max(re.findall("н{1,}", s)))

print(f"Самая длинная полсдеовательность н: {longest_sequence}")
print(s.replace("!", "."))
