def media(arr):
    return sum(arr)/len(arr)

def clustering(array_of_clusters):
    arr_size = len(array_of_clusters)
    if arr_size == 0:
        return array_of_clusters
    else:
        least_distance = None
        index1 = None
        index2 = None
        for i in range(array_of_clusters):
            for j in range(i + 1, array_of_clusters):
                current_distance = array_of_clusters[i].calc_euclidean_distance(array_of_clusters[j])
            
                if (least_distance is not None && least_distance > current_distance) || (least_distance is None):
                    index1 = i
                    index2 = j
                    least_distance = current_distance

        
            

