import csv




def load_data(fileP):

	reader = csv.reader(open(fileP))

	result = {}
	for row in reader:
		key = row[0]
		if key in result:

			pass
		result[key] = row[1:]

	return result

man_dict = load_data('inputs.csv')
woman_dict = load_data('outputs.csv')
potential_couple = []
free_M = [m for m in man_dict]



def matching_routine():

	while len(free_M)>0:
		for m in free_M:
			GS_match(m)


def GS_match(m):
	

	for w in man_dict[m]:

		woman_chosen = [couple for couple in potential_couple if w in couple]

		if len(woman_chosen) == 0 : 
			potential_couple.append([m,w])
			free_M.remove(m)
			print('%s is no longer a free man and is now potentialy linked to %s'%(m,w))
			break 

		elif len(woman_chosen) > 0 :
			print('%s is not available anymore'%(w))
			actual_m = woman_dict[w].index(woman_chosen[0][0])
			potential_m = woman_dict[w].index(m)

			if actual_m < potential_m:

				print('She\'s ok with %s..'%(woman_chosen[0][0]))
			else:

				print('%s index-rank is greater than %s'%(m, woman_chosen[0][0]))
				print('Making %s free . potentialy linking %s and %s'%(woman_chosen[0][0], m, w))

				free_M.remove(m)
				free_M.append(woman_chosen[0][0])
				woman_chosen[0][0] = m

				break


matching_routine()
print(potential_couple)
