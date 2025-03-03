import matplotlib.pyplot as plt

class Airport:
    def __init__(self, runways):
        self.runways = ["R" + str(i) for i in range(1, runways+1)]

    def iddfs(self, flights):
        for depth in range(len(self.runways)):
            allocated = self.dls(flights, depth, {})
            if allocated:
                return allocated
        return None

    def dls(self, flights, depth, allocated):
        if not flights:
            return allocated

        flight = flights[0]
        if depth < len(self.runways):
            allocated[flight] = self.runways[depth]
            return self.dls(flights[1:], depth + 1, allocated)

        return None

    def visualize_allocation(self, allocation):
        plt.figure(figsize=(6, 4))
        
        # Plot bars correctly using indices for flights
        y_pos = list(range(len(allocation)))  # Flight positions on y-axis
        plt.barh(y_pos, [1] * len(allocation), color='lightblue
