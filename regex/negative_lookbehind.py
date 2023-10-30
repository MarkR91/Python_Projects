import re

lines = ["Hello world", "This line has ifdf", "Another line without ifdf", "Last line"]

# Use negative lookahead for "ifdf"
pattern = re.compile(r"^(?!.*ifdf)")

# Match any characters after that
pattern = re.compile(r"^(?!.*ifdf).*")

# Match until the end of the line
pattern = re.compile(r"^((?!.*ifdf).)*$")

for line in lines:
    if pattern.match(line):
        print(line)
