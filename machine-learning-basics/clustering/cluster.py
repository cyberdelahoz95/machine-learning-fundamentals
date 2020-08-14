
class Cluster:
    def __init__(self, x, y, sub_clusters, distance_btwn_sub_clusters):
        self.x = x
        self.y = y
        self.sub_clusters = sub_clusters
        self.distance_btwn_sub_clusters = distance_btwn_sub_clusters

    def calc_euclidean_distance(self, another_cluster):
        delta_x = another_cluster.x - self.x
        delta_y = another_cluster.y - self.y

        return (delta_x**2 + delta_y**2)**0.5
