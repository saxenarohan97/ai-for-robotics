p = [0.2]*5

world = ['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'red']
motions = [1, 1]

pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

def sense(p, Z):
	q = []

	for i in range(len(p)):
		hit = (Z == world[i])
		q.append(p[i]* (pHit*hit + pMiss*(1-hit)))

	s = sum(q)
	for i in range(len(q)):
		q[i] /= s

	return q

def move(p, U):
	q = [0]*len(p)

	for i in range(len(p)):
		new_index = i+U

		if new_index > len(p)-1:
			new_index %= len(p)

		q[new_index] += p[i]*pExact

		overshot_index = (new_index-1) % len(p)
		q[overshot_index] += p[i]*pOvershoot
		undershot_index = (new_index+1) % len(p)
		q[undershot_index] += p[i]*pUndershoot

	return q

for i in range(len(motions)):
	p = sense(p, measurements[i])
	p = move(p, motions[i])

print p