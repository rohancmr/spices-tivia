from random import choice

spices = ['Saunf', 'Heeng', 'Jau', 'Tulsi', 'Tej Patta', 'Kali Mirch', 'Ilaichi', 'Ajwain', 'Dalchini', 'laung', 'Dhaniya', 'Hara Dhaniya', 'Jeera', 'Kari Patte', 'Sonth', 'Methi', 'Lahsun', 'Adrak', 'Moong', 'Amchoor', 'Pudina', 'Sarson', 'Sarson Ka Tel', 'Kalonji', 'Akhrot', 'Jaifal', 'Mirch', 'Anar Dana', 'Afeem', 'Lal Mirch', 'Kesar', 'Sabudana', 'Til', 'Haldi', 'Sirka', 'Safed Mirch', 'Asalee ka Beej', 'Khameer', 'Khaskhas', 'Chirayata', 'Jaavitree', 'Ramtil', 'Majeeth', 'Majoofal', 'Mulaithi']

for i in spices:
	print("{},{},{}".format(i, choice(spices), choice(spices)))