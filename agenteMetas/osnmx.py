import osmnx as ox
import matplotlib.pyplot as plt

# Definir el lugar y descargar el gráfico de red
place_name = "Miraflores, Lima, Peru"
G = ox.graph_from_place(place_name, network_type='drive')

# Convertir los nodos a un DataFrame
nodes, edges = ox.graph_to_gdfs(G)

# Visualizar el gráfico de red
fig, ax = ox.plot_graph(G)
plt.show()
