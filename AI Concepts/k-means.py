import numpy as np

def euclidean_distance(point1, point2):
    
    euclu= np.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
    return euclu

def k_means_clustering(data):
    m1, m2 = data[0], data[1]
    n = 0
    flag = True
    
    cluster1 = []
    cluster2 = []
    
    while flag:
        sum1, sum2 = 0, 0
        cluster1.clear()
        cluster2.clear()
        n += 1
        k, j = 0, 0
        
        for point in data:
            distance_to_m1 = euclidean_distance(point, m1)
            distance_to_m2 = euclidean_distance(point, m2)
            if distance_to_m1 <= distance_to_m2:
                cluster1.append(point)
                k += 1
            else:
                cluster2.append(point)
                j += 1
        
        for point in cluster1:
            sum1 += np.array(point)
        for point in cluster2:
            sum2 += np.array(point)
        
        print(f"After iteration {n}, \n cluster 1:\n{cluster1}\n cluster 2:\n{cluster2}\n")
        
        a, b = m1, m2
        m1, m2 = list(np.round(sum1 / k)), list(np.round(sum2 / j))
    
        flag = not (m1 == a and m2 == b)
    
    print("Final cluster 1:\n", cluster1)
    print("Final cluster 2:\n", cluster2)
    
x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

data = list(zip(x, y))
print(data)

k_means_clustering(data)
