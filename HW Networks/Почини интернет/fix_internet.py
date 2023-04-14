
class Connection:
    def __init__(self, v1 ,v2):
        self.v1 = v1
        self.v2 = v2
    def __str__(self):
        return "( "+str(self.v1)+" ; "+str(self.v2)+" )"

connections = []
visitedVertexes = []

def find_connected(vertex):
    result = []
    for i in connections:
        if i.v1==vertex:
            result.append(i.v2)
        elif i.v2==vertex:
            result.append(i.v1)
    return result

def deep_search(root):
    visitedVertexes[root] = True
    conts = find_connected(root)
    for i in conts:
        if not visitedVertexes[i]:
            deep_search(i)

def main():
    print("Input amount of connections")
    n = int(input())
    for i in range(n+1):
        visitedVertexes.append(False)
    print("Input connections")
    input_string = input()
    input_array = input_string.split(" ")
    for i in range(len(input_array)):
        input_array[i] = int(input_array[i])
    for i in list((input_array[i:i + 2] for i in range(0, len(input_array), 2))):
        v1,v2 = i
        connections.append(Connection(v1,v2))

    print("Connections:")
    for i in connections:
        print(i)
    print("")
    islands = 0
    for i in range(len(visitedVertexes)):
        if i==0:
            continue
        if not visitedVertexes[i]:
            islands+=1
            deep_search(i)
    print("Anwser is: ",islands-1)




if __name__=='__main__':
    main()
