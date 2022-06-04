#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.
import pyperclip

text = pyperclip.paste()
print("Before Modification:")
print(text)

# stores different lines of text in a list named lines
lines = text.split("\n")

# adds * to every line stored in list
for i in range(len(lines)):
	lines[i] = "*" + lines[i]

# converts the new list of lines to a single text
text = "\n".join(lines)

# copies new modified text to the clipboard
pyperclip.copy(text)
print("\nAfter Modification:")
print(pyperclip.paste())
