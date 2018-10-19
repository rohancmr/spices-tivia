from random import choice

spices = ['Fennel', 'Asafoetida', 'Barley', 'Basil', 'Bay Leaf', 'Black Pepper', 'Cardamom', 'Carom Seed', 'Cinnamon', 'Clove', 'Coriander', 'Coriander Leaves', 'Cumin', 'Curry Leaves', 'Dry Ginger', 'Fenugreek', 'Garlic', 'Ginger', 'Green Gram', 'Mango Powder', 'Mint', 'Mustard', 'Mustard Oil', 'Nigella', 'Nut', 'Nutmeg', 'Chilli', 'Pomegranate Seed', 'Poppy', 'Red Chilli', 'Saffron', 'Sago', 'Sesame', 'Turmeric', 'Vinegar', 'White Pepper', 'Linseed', 'Yeast', 'Popy seed', 'Swertia', 'Mace', 'Niger', 'Indian Madder', 'Gall-Nut', 'Liquorice']

for i in spices:
	print("{},{},{}".format(i, choice(spices), choice(spices)))