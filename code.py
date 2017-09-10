import random, string
alphabet = string.ascii_letters + " !'."

def get_letter():
	""" Get a letter in the alphabet """
	return random.choice(alphabet)

def create_chromosome(size):
    """
	input : size of a chromosome
	Create a chromosome as a string of the right size
	output : chromosome
	"""
    chromosome = ''
    for i in range(size):
        new_letter = get_letter()
        chromosome += str(new_letter)
    return chromosome

def get_score(chrom, answer):
	"""
	input : chromosome and the answer
	compare the chromosome to the answer
	output : score
	"""
	score = 0
    # implement the scoring function
    #  * compare the chromosome with the solution (how many character are in the correct position?)
	for idLetter in range(len(chrom)):
		if chrom[idLetter] == answer[idLetter]:
			score += 1
	score = score/len(chrom)
	return score

def selection(chromosomes_list):
	"""
	input : chromosome population
	select the best chromosomes and random chromosomes
	output : selection
	"""
	new_chromosomes_list = chromosomes_list
	score_list = []
	score_max, id_max = 0, 0
	for id_chrom in new_chromosomes_list:
		score_list.append(get_score(id_chrom, answer))

	for i in range(len(score_list)):
		for id_cur in range(len(score_list) - i):
			if score_max < score_list[id_cur]:
				score_max = score_list[id_cur]
				id_max = id_cur
		inter = new_chromosomes_list[len(new_chromosomes_list) - i - 1]
		new_chromosomes_list[len(new_chromosomes_list) - i - 1] = new_chromosomes_list[id_max]
		new_chromosomes_list[id_max] = inter

	nb_best_chrom = int(len(score_list) * 30 / 100)
	nb_random_chrom = int(len(score_list) * 20 / 100)
	selection = []

	for i in range(nb_best_chrom):
		selection.append(new_chromosomes_list[len(new_chromosomes_list) - 1 - i])
	for i in range(nb_random_chrom):
		selection.append(new_chromosomes_list[i])
	return selection

def crossover(parent1, parent2):
	"""
	input : 2 parents
	create a child from both parents
	output : child
	"""
	child = ''
	for i in range(len(parent1)):
		if i <= len(parent1)/2:
			child += str(parent1[i])
		else : child += str(parent2[i])
	return child

def mutation(chrom):
	""" implement the mutation function of a chromosome """
	id_mut = random.randint(0, len(chrom) - 1)
	new_chrom = ''
	for id_letter in range(len(chrom)):
		if id_letter == id_mut :
			new_chrom += get_letter()
		else :
			new_chrom += chrom[id_letter]
	return new_chrom

def create_population(pop_size, chrom_size):
	""" create a chromosome population """
	return [create_chromosome(chrom_size) for i in range(pop_size)]

def generation(population):
	"""
	input : list of chromosomes
	purpose : generate a new chromosome population
	output : new list of chromosomes
	"""

	# selection
	# use the selection(population) function created on exercise 2
	select = selection(population)

	# reproduction
	# As long as we need individuals in the new population, fill it with children
	children = []
	# TODO: implement the reproduction
	while len(children) < 5:
		## crossover
		parent1 = select[random.randint(0, len(select) - 1)] # randomly selected
		parent2 = select[random.randint(0, len(select) - 1)] # randomly selected
		# use the crossover(parent1, parent2) function created on exercise 2
		child = crossover(parent1, parent2)

		## mutation
		# use the mutation(child) function created on exercise 2
		mut = random.randint(0,9)
		if mut == 1: #10% that a chrom can mutate
			child = mutation(child)
		children.append(child)

	# return the new generation
	return select + children

def algorithm(answers, answer_size):
	""" Genetic algorithm """
	chrom_size = answer_size
	population_size = 20

	# create the base population
	population = create_population(population_size, chrom_size)

	answers = []
	# while a solution has not been found :
	while len(answers) == 0 :
		## create the next generation
		# create the next generation using the generation(population) function
		population = generation(population)

		## check if a solution has been found
		for chrom in population:
			if chrom == answer:
				answers.append(chrom)


    # print the solution
	print(answers[0])

if __name__ == '__main__':
	answer = 'jNxbthOwkccnaiqpfooJmxfIBqZNuZJYMouIbHLbDRFAcaZhgExowygcfNonxmNUGYdITZJQXnqxgAEZHkaljGHGadgAxRIWArGV'
	print(answer)
	algorithm(answer, len(answer))
