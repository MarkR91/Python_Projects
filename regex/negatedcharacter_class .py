"""import re

lines = ["Hello world", "island", "Another line", "important info"]

pattern = re.compile(r"^[^i]*$")

for line in lines:
    if pattern.match(line):
        print(line)
"""
import re

lines = ["Hello", "ifdf line", "Another line", "Start"]

pattern = re.compile(r"^[^i]*$")

for line in lines:
    if pattern.match(line):
        print(line)
