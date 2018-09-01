# CSL622-Assignment1
This assignment will use a dataset created in CSL622 lab which contains indices of people and who they find interesting in each column.
The objective of this code is to assign a pagerank to all of the indices in the graph. The method use for this is a really naive approach
in which we choose a random node in the graph and see its neighbors. We maintain a count of how many times a particular node has been inspected
for each node. We repeat the process for at least 1,000,000 times. We sort the nodes in the descending orders of count. The indices of the
resulting list will give us the corresponding pagerank for each node.
