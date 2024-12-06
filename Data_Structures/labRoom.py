from Graph import Graph, NodeGraph, Traveler
from Graph.QuickSort import QuickSort


# ArcaneField = Graph()

# Vital = ArcaneField.registerNode("Vital")
# Knowledge = ArcaneField.registerNode("Knowledge")
# Dead = ArcaneField.registerNode("Dead")

# print(Vital)
# print(Knowledge)

# ArcaneField.connect(Vital, Knowledge, 1, True, 2)

# print(Vital)
# print(Knowledge)





# EXERCÍCIO 012
def a():
    GraphA = Graph()

    a = GraphA.registerNode("a")
    b = GraphA.registerNode("b")
    c = GraphA.registerNode("c")
    d = GraphA.registerNode("d")
    e = GraphA.registerNode("e")
    f = GraphA.registerNode("f")
    g = GraphA.registerNode("g")
    h = GraphA.registerNode("h")
    GraphA.connect(a, b)
    GraphA.connect(a, e)
    GraphA.connect(a, f)
    GraphA.connect(b, c)
    GraphA.connect(b, e)
    GraphA.connect(c, d)
    GraphA.connect(e, d)
    GraphA.connect(e, g)
    GraphA.connect(f, e)
    GraphA.connect(f, h)
    GraphA.connect(g, c)
    GraphA.connect(g, h)
    GraphA.connect(h, d)


# EXERCÍCIO 013
def b():
    GraphB = Graph()

    r = GraphB.registerNode("r")
    s = GraphB.registerNode("s")
    t = GraphB.registerNode("t")
    u = GraphB.registerNode("u")
    v = GraphB.registerNode("v")
    z = GraphB.registerNode("z")
    x = GraphB.registerNode("x")
    GraphB.connect(r, s, 7, True)
    GraphB.connect(r, u, 15, True)
    GraphB.connect(r, v, 17, True)
    GraphB.connect(r, z, 25, True)
    GraphB.connect(s, t, 12, True)# r
    GraphB.connect(s, u, 10, True)
    GraphB.connect(s, z, 20, True)
    GraphB.connect(t, u, 5, True)# r s
    GraphB.connect(u, v, 15, True)# r s t
    GraphB.connect(v, z, 35, True)# r s t u
    GraphB.connect(v, x, 30, True)
    GraphB.connect(x, z, 12, True)
    
    x = GraphB.getNodeByValue('x')
    t = GraphB.getNodeByValue('t')
    
    temp = GraphB.deepSearchAll(x, t)
    temp = QuickSort(temp, 1, 'cost').sorted
    print(temp[0])
# b()



# EXERCÍCIO 014
def c():
    GraphC = Graph()

    a = GraphC.registerNode("a")
    b = GraphC.registerNode("b")
    c = GraphC.registerNode("c")
    d = GraphC.registerNode("d")
    e = GraphC.registerNode("e")
    f = GraphC.registerNode("f")
    g = GraphC.registerNode("g")
    h = GraphC.registerNode("h")
    i = GraphC.registerNode("i")
    j = GraphC.registerNode("j")
    k = GraphC.registerNode("k")
    l = GraphC.registerNode("l")
    GraphC.connect(a, b)
    GraphC.connect(a, e)
    GraphC.connect(b, f)
    GraphC.connect(c, d)
    GraphC.connect(c, f)
    GraphC.connect(c, g)
    GraphC.connect(c, h)
    GraphC.connect(d, g)
    GraphC.connect(d, h)
    GraphC.connect(e, f) #a b c d
    GraphC.connect(e, i)
    GraphC.connect(f, g)
    GraphC.connect(f, i)
    GraphC.connect(f, j) # a b c d e f
    GraphC.connect(g, h)
    GraphC.connect(g, k)
    GraphC.connect(g, l) # a b c d e f g
    GraphC.connect(h, l) # a b c d e f g h
    GraphC.connect(j, k)
    GraphC.connect(k, l)
    
    f = GraphC.getNodeByValue('f')
    g = GraphC.getNodeByValue('l')
    
    res = GraphC.BFS(f)
    
    for node in res:
        print(node.data)
    
c()





def main():
    menu = '''
    [1] - Exibir informações do viajante
    [2] - Exibir mapa
    [3] - Viajar para <posição no mapa>
    [0] - Sair
    '''
    Nayahath = Traveler()
    Arcana = Graph()
    Graph.autofill(Arcana)
    Nayahath.setPosition(Arcana.registeredNodes[0])
    
    
    while True:
        print(menu)
        userInput = input("Digite o código da ação: ")
        if userInput == '1':
            print(Nayahath)
        elif userInput == '2':
            Nayahath.showMap()
        elif userInput == '3':
            while True:
                try:
                    pos = int(input("Digite a posição do destino no mapa: "))
                    break
                except:
                    print("Posição deve ser um número inteiro")
            Nayahath.travelTo(pos)
        elif userInput == '0':
            break
        else:
            print("Opção inválida")
    
# main()

# Nayahath = Traveler()
# Arcana = Graph()
# Graph.autofill(Arcana)
# a = Arcana.getNodeByValue('a')
# g = Arcana.getNodeByValue('g')
# res = Arcana.deepSearchAll(a, g)

# # print(res)

# for path in res:
        
#     print(path["path"])
#     print(path["cost"])
#     print("\n")