# Time complexity: O(N^2)
# Space complexity: O(2N)

def printCheapestFlights(delhi_to_mumbai, mumbai_to_delhi, k):
    response = []
    for dtm in delhi_to_mumbai:
        for mtd in mumbai_to_delhi:
            response.append([dtm, mtd])

    response.sort(key=lambda x: (x[0] + x[1]))
    for i in range(k):
        print(str(response[i][0])+","+str(response[i][1]))


delhi_to_mumbai = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
mumbai_to_delhi = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
k = 10
printCheapestFlights(delhi_to_mumbai, mumbai_to_delhi, k)
