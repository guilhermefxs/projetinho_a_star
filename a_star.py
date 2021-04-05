import csv

with open('dis_reta.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)


lines = [["blue"], ["blue", "yellow"], ["blue", "red"], ["blue", "green"], ["blue", "yellow"], ["blue"], 
["yellow"], ["yellow", "green"], ["yellow", "red"], ["yellow"], ["red"], ["green"], ["green", "red"], ["green"] ]


bestPath = [
    {"blue": (-1, -1},
    {"blue": (-1,-1), "yellow": (-1,-1)},
    {"blue": (-1,-1), "red": (-1,-1)},
    {"blue": (-1,-1), "green": (-1,-1)},
    {"blue": (-1,-1), "yellow": (-1,-1)},
    {"blue": (-1,-1)},
    {"yellow": (-1,-1)},
    {"yellow": (-1,-1), "green": (-1,-1)},
    {"yellow": (-1,-1), "red": (-1,-1)},
    {"yellow": (-1,-1)},
    {"red": (-1,-1)},
    {"green": (-1,-1)},
    {"green": (-1,-1), "red": (-1,-1)},
    {"green": (-1,-1)}
]
lowerCost = [{"blue": -1},
    {"blue": -1, "yellow": -1},
    {"blue": -1, "red": -1},
    {"blue": -1, "green": -1},
    {"blue": -1, "yellow": -1},
    {"blue": -1},
    {"yellow": -1},
    {"yellow": -1, "green": -1},
    {"yellow": -1, "red": -1},
    {"yellow": -1},
    {"red": -1},
    {"green": -1},
    {"green": -1, "red": -1},
    {"green": -1}]

#Grafo de conexões
connections = [
    [(2, 10)], 
    [(1, 10), (3, 8.5), (9, 10), (10, 3.5)], 
    [(2, 8.5), (4, 6.3),(9, 9.4), (13, 18.7)],
    [(3, 6.3), (5, 13), (8, 15.3), (13, 12.8)],
    [(4, 13), (6, 3),(7, 2.4),(8, 30)],
    [(5, 3)],
    [(5, 2.4)],
    [(4, 15.3), (5, 30), (9, 9.6), (12, 6.4)],
    [(2, 10), (3, 9.4), (11, 12.2)],
    [(2, 3.5)],
    [(9, 12.2)],
    [(8, 6.4)],
    [(3, 18.7), (4, 12.8), (14, 5.1)],
    [(13, 5.1)]
    ]

def aStar (start_point, end_point):
    #Variavel para checar se chegou ao fim
    finished = False
    
    #Adicionando o ponto de partida na nossa lista de prioridades
    priority_queue.append(start_point)

    #Setando o custo para chegar no estado inicial para 0
    lowerCost[start_point[0]-1][start_point[1]] = 0

    #Loop que itera enquanto a lista nao for vazia e ainda nao tivermos chegado ao fim
    while(priority_queue.count>0 and not finished):

        #Seta o estado atual para o primeiro elemento da lista
        current_state = priority_queue.pop() #provavelment n é pop aq!!!!!!!!


        #Checa se o estado atual é o estado final
        if(current_state[0] == end_point[0] and current_state[1] == end_point[1]):
            finished = True 

        else:
            #Itera por todas as conexões do estado atual
            for connection in connections[current_state[0] - 1]:

                #Inicializa a linha com a linha do estado atual
                thisLine = current_state[1]

                #Checa se será necessário uma mudança de linha 
                changeLine = changeLine(current_state[0], connection[0])
               
               #Se for necessario uma mudança de linha, atualiza o custo de mudança p 4 e atualiza a linha para a linha que o estado atual e essa conexão tem em comum
                if(changeLine):
                    changeLineCost = 4
                    thisLine = thisLine(current_state[0], connection[0])
                    
                #Se nao for necessario, seta custo para 0
                else:
                    changeLineCost = 0

                #Calcula a heuristica referente a essa conexao
                h = data[connection[0] - 1][end_point[0] - 1]

                #Calcula o custo real referente a essa conexao
                cost = lowerCost[current_state[0]-1][current_state[1]] +  cost(current_state[0], connection) + changeLineCost

                #Se o custo real calculado para chegar a esse estado for menor do que tem-se armazenado(ou se não tiver sido calculado previamente), atualiza-se ele
                if(lowerCost[connection[0]-1][thisLine] == -1) or (cost <= lowerCost[connection[0]-1][thisLine]):

                    #Atualiza menor custo real para esse estado
                    lowerCost[connection[0]-1][thisLine] = cost

                    #Atualiza o estado que leva a esse estado com esse menor custo
                    bestPath[connection[0]-1][thisLine] = (current_state[0], current_state[1])
                    
                #Insere na nossa lista em ordem o estado (conexao, linha)
                    counter = -1
                    inserted = False

                    #Itera pelos elementos na nossa lista
                    for station in priority_queue:
                        counter = counter + 1

                        #Checa se a soma (valor real + heuristica) do estado que desejamos inserir é menor que essa mesma soma do elemento atual da lista
                        if(lowerCost[connection[0]-1][thisLine] + h <= lowerCost[station[0][station] +  data[station[0] - 1][end_point[0] - 1] ):
                            priority_queue.insert(counter, (connection[0], thisLine))
                            inserted = True
                            break

                    #Se não tiver inserido, insere no fim
                    if(not inserted):
                         priority_queue.insert(counter+1, station)


#Restorna o custo real entre um estado e outro    
def cost(current_state, next_station):
    for connection in connections[current_state-1]:
        if(connection[0] == (next_station-1)):
            return (connection[0] + h)  
    

#Retorna se é necessário trocar de linha
def changeLine(destination, line):
    for linesInStation in lines[destination-1]:
        if linesInStation == line:
            return False
    return True

#Retorna primeira linha em comum encontrada entre duas estações
def newLine(station1, station2):
    for linesInStation1 in lines[station1-1]:
        for linesInStation2 in lines[station2-1]:
            if(linesInStation1 == linesInStation2):
                retun linesInStation1


def main():
