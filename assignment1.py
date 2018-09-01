import networkx as nx
import numpy as np
import random
from operator import itemgetter
def pagerank(G):
	m = G.number_of_nodes()
	itr = 1000000
	count = {}
	for i in range(0,m):
		count[str(i)] = i
	#print(count)
	for i in range(0,itr):
		r = random.randint(0,m-1)
		#print(r)
		succ = G.successors(r)
		r1 = random.randint(0,itr)
		if r1 < int(0.2*itr):
			r = random.randint(0,m-1)
		for s in succ:
				count[str(s)] = count[str(s)] + 1
	#print(count1)
	#print(count)
	count1 = sorted(count.items(), key = itemgetter(1), reverse = True)
	#print(count1)
	pagerank1 = []
	for k in count1:
		pagerank1.append(int(k[0]))

	return pagerank1

print("This program will determine the pagerank of Nodes based on their ability of being found interesting")
print(" ")
print("This is a naive approach in which we start at a random node every time and see its neighbors. We maintain a count of the number of times a particular node has been pointed towards. We repeat this experiment at least 1000000 times to get a good approximation of the pagerank.")
G = nx.DiGraph()
e = open("pagerank.txt", "r")
lines = e.read().splitlines()
#print(len(lines))
line_set = set()
line_set.add(line for line in lines)
#print(len(list(line_set)))
nodes = set()
for line in lines:
	#print(line)
	node1 = line.split(' ')
	nodes.add(int(node1[0]))
	nodes.add(int(node1[1]))
nodes1 = list(nodes)
no_of_nodes = len(nodes1)
nodes1.sort()
#print(nodes1)
prev_to_curr = {}
curr_to_prev = {}
for i in range(0,no_of_nodes):
	prev_to_curr[nodes1[i]] = i
	curr_to_prev[i] = nodes1[i]
G.add_nodes_from(i for i in range(0,no_of_nodes))
for line in lines:
	a = line.split(' ')
	G.add_edge(prev_to_curr[int(a[0])],prev_to_curr[int(a[1])])

#print(list(G.nodes()))
#print(G.edges())
'''for i in range(0,500):
	r1 = random.randint(0,99)
	r2 = random.randint(0,99)
	if r1!=r2:
		G.add_edge(r1,r2)
'''
print("The number of nodes in the directed graph is ", G.number_of_nodes())
#print(G.edges)
print("The number of edges in the directed graph is ", G.number_of_edges())
pr = pagerank(G)
for i in range(0,len(pr)):
	pr[i] = curr_to_prev[pr[i]]
print("The list of nodes sorted in ascending order according to their pagerank is:")
print(pr)