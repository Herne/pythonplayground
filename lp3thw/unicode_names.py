import unicodedata

for i in range(0x10FFFF):
    character = chr(i)
    name = unicodedata.name(character, "")
    if len(name) > 0:
        print(f"{i:6} | 0x{i:04X} | {character} | {name}")
