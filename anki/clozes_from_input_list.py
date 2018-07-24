#!/usr/bin/env python

"""
Generate text for Anki 'cloze' notes based on a list of inputs

1. Take in a list of input.
2. Generate the text for a 'cloze' note for each item with
   the item blanked out.
"""

print("Header displayed before the list of items:")
header = input()

items = []
while True:
    print("Input an item; type 'done' when you are done:")
    new_item = input()
    if new_item == 'done':
        break
    items.append(new_item)

out_file = open('./out.md', 'w')
for i, ans in enumerate(items):
    out_file.write(f'\n\n## Note {i}\n\n')
    out_file.write(f'{header}\n')
    for it in items:
        if it == ans:
            cloze = '{{c1::' + ans + '}}\n'
            out_file.write(cloze)
        else:
            out_file.write(f'{it}\n')
out_file.close()
