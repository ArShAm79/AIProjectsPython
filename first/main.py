from collections import deque


class Graph:

    def __init__(self, edges=None, length=0):

        self.length = length
        self.edges = [[] for _ in range(length)]

        for (src, dest) in edges:

            self.edges[src].append(dest)

            self.edges[dest].append(src)

        print(self.edges)


def read_from_file(address):
    edges = []

    file = open(address, "r")
    stream = file.read()

    data = stream.split("\n")

    for node in data:
        numbers = node.split(" ")
        edges.append((int(numbers[0]), int(numbers[1])))

    return edges


def checkEdges(edges):
    length = len(edges)+1

    graph = Graph(edges, length)

    if is_bipartite(graph):
        return True
    else:
        return False


def is_bipartite(graph):

    visited = [False] * graph.length

    color = [None] * graph.length

    visited[0] = True
    color[0] = 0

    start = 0

    numbers = deque()
    numbers.append(start)

    while numbers:

        start = numbers.popleft()
        for item in graph.edges[start]:
            if not visited[item]:
                visited[item] = True

                color[item] = color[start] + 1

                numbers.append(item)

            elif color[start] == color[item]:
                return False

    return True


if __name__ == '__main__':

    addresses = ["graph6.edgelist",
                 #  "graph2.edgelist",
                 #  "graph3.edgelist",
                 #  "graph4.edgelist",
                 #  "graph5.edgelist"
                 ]

    for address in addresses:
        data = read_from_file(address)

        if checkEdges(data):
            print(address.replace(".edgelist", "").capitalize()+" is Bipartite")
        else:
            print(address.replace(".edgelist", "").capitalize()+" is not Bipartite")
