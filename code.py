import random, string
alphabet = string.ascii_letters + " !'."

def get_letter():
    return random.choice(alphabet)

def create_chromosome(size):
    # TODO: Create a chromosome as a string of the right size
    chromosome = ''
    for i in range(size):
        new_letter = get_letter()
        chromosome += str(new_letter)
    return chromosome

def get_score(chrom, answer):
	score = 0
    # TODO: implement the scoring function
    #  * compare the chromosome with the solution (how many character are in the correct position?)
	for idLetter in range(len(chrom)):
		if chrom[idLetter] == answer[idLetter]:
			score += 1
	score = score/len(chrom)
	return score

def selection(chromosomes_list):
	GRADED_RETAIN_PERCENT = 0.3     # percentage of retained best fitting individuals
	NONGRADED_RETAIN_PERCENT = 0.2  # percentage of retained remaining individuals (randomly selected)
	# TODO: implement the selection function
	#  * Sort individuals by their fitting score
	#  * Select the best individuals
	#  * Randomly select other individuals
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
    # TODO: implement the crossover function
    #  * Select half of the parent genetic material
    #  * child = half_parent1 + half_parent2
    #  * Return the new chromosome
    #  * Genes should not be moved
	child = ''
	for i in range(len(parent1)):
		if i <= len(parent1)/2:
			child += str(parent1[i])
		else : child += str(parent2[i])
	return child

def mutation(chrom):
    # TODO: implement the mutation function
    #  * Random gene mutation : a character is replaced
	id_mut = random.randint(0, len(chrom) - 1)
	new_chrom = ''
	for id_letter in range(len(chrom)):
		if id_letter == id_mut :
			new_chrom += get_letter()
		else :
			new_chrom += chrom[id_letter]
	return new_chrom

def create_population(pop_size, chrom_size):
	# use the previously defined create_chromosome(size) function
	# TODO: create the base population
	return [create_chromosome(chrom_size) for i in range(pop_size)]

def generation(population):

	# selection
	# use the selection(population) function created on exercise 2
	select = selection(population)

	# reproduction
	# As long as we need individuals in the new population, fill it with children
	children = []
	# TODO: implement the reproduction
	while len(children) < 5:
		## crossover
		parent1 = population[random.randint(0, len(population) - 1)] # randomly selected
		parent2 = population[random.randint(0, len(population) - 1)] # randomly selected
		# use the crossover(parent1, parent2) function created on exercise 2
		child = crossover(parent1, parent2)

		## mutation
		# use the mutation(child) function created on exercise 2
		child = mutation(child)
		children.append(child)

	# return the new generation
	return select + children

def algorithm(answers, answer_size):
	chrom_size = answer_size
	population_size = 20

	# create the base population
	population = create_population(population_size, chrom_size)

	answers = []
	# while a solution has not been found :
	while len(answers) == 0 :
		## create the next generation
		# TODO: create the next generation using the generation(population) function
		population = generation(population)

		## display the average score of the population (watch it improve)
		# print(get_mean_score(population), file=sys.stderr)

		## check if a solution has been found
		for chrom in population:
			if chrom == answer:
				print(chrom)
				answers.append(chrom)


    # TODO: print the solution
	print("SOLUTION")

if __name__ == '__main__':
	answer = 'jNxbthOwkccnaiqpfooJmxfIBqZNuZJYMouIbHLbDRFAcaZhgExowygcfNonxmNUGYdITZJQXnqxgAEZHkaljGHGadgAxRIWArGV'
	print(answer)
	algorithm(answer, len(answer))
