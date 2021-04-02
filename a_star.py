import csv

with open('dis_reta.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)


lines = [["blue"], ["blue", "yellow"], ["blue", "red"], ["blue", "green"], ["blue", "yellow"], ["blue"], 
["yellow"], ["yellow", "green"], ["yellow", "red"], ["yellow"], ["red"], ["green"], ["green", "red"], ["green"] ]

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
    current_line = lines[start_point - 1][0]
    finished = False
    
    priority_queue = [(start_point, data[start_point-1][end_point-1])]
    acumulated_cost = 0

        # minCost = -1
        # current_cost = avaliation(start_point, connection.first, end_point)
        # if(avaliation<= minCost):

    while(priority_queue.count>0 and not finished):
        current_station = priority_queue.pop()

        for connection in connections[current_station - 1]:
            

            


def avaliation(current_station, next_station, end_point):
    #Retorna g(n) + h(n)
    h = data[next_station - 1][end_point - 1]
    for connection in connections[current_station-1]:
        if(connection[0] == (next_station-1)):
            return (connection[0] + h)  
    

def changeLineCost(destination, line):
    for linesInStation in lines[destination-1]:
        if linesInStation == line:
            return 0
    return 4 