import string_db as sdb

class Graph():
	def __init__(self, edges):
		self.edges = edges

	def add_Edge(self, edge, weight):
		self.edges[edge] = weight 
		temp = (edge[1], edge[0])
		self.edges[temp] = weight

	def get_subGraph(self, node_list):
		sub_graph_edges={}
		for node1 in node_list:
			for node2 in node_list:
				if((node1 != node2) and ((node1, node2) in self.edges)):
					sub_graph_edges[(node1, node2)] = self.edges[(node1, node2)]
		sub_graph = Graph(sub_graph_edges)
		return sub_graph

	def get_all_edge_weights(self, node):
		sum = 0
		for edge in self.edges.keys():
			if(edge[0] == node):
				sum += self.edges[edge]
		return sum

class FullGraphProteins(Graph):
	def __init__(self, list_of_proteins):
		super().__init__({})
		for protein in list_of_proteins:
			self.add_Edge((protein, ''), 0)

		full_list = sdb.Protein_Network(list_of_proteins)
		for each_edge in full_list.data:
			self.add_Edge((each_edge['preferredName_A'], each_edge['preferredName_B']), each_edge['score'])

if __name__ == "__main__":
	my_full_graph = FullGraphProteins(['APOE', 'APOC1', 'GREM', 'AKBR1', 'NOS3', 'CARS',
		'ACE', 'UNC13B', 'FRMD3', 'HSPG2', 'EPO', 'VEGFA'])
	print(my_full_graph.edges)

