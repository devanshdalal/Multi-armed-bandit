import random
def weighted_choice(weights):
   r = random.uniform(0, sum(weights))
   upto = 0
   for c,w in enumerate(weights):
      if upto + w >= r:
         return c
      upto += w
   assert False, "Shouldn't get here"


M=1000 # no of simulations
N=100 # games in a simulation
machines = 3
t=0
total_score=0;

while t<M:

	wheels = [random.random() for x in range(machines)]
	mygames = 2

	i=0
	
	prediction = [1.0/3.0 for x in range(machines)]
	score = 0.0
	while i<N:
		choice = weighted_choice(prediction)
		
		inc=1.0 if random.random()<wheels[choice] else -1.0

		prediction=[mygames*w+(inc if ix==choice else 0) for ix,w in enumerate(prediction)]
		s=sum(prediction)
		prediction=[w/s for w in prediction]
		mygames+=1
		i+=1

		score+=(1+inc)/2.0

	print('score',score)
	total_score+=score

	t+=1

print('total_score',total_score)
print('avg_total_score per game',total_score/M)
print('avg_total_score per turn',total_score/(M*N))







