# characters = ['i', 'a']
# res = list(enumerate(characters))
# print(res)

# for index, character in enumerate(characters):
# 	print(index, character)

characters = ["Krillin","Goku", "Goku", "Gohan", "Piccolo",
              "Krillin","Goku", "Vegeta", "Gohan", "Piccolo",
              "Piccolo","Goku", "Vegeta", "Goku", "Piccolo"]

character_map = { character:[] for character in set(characters) }
print(type(character_map))

for index, character in enumerate(characters):
	character_map[character].append(index)
print(character_map)
