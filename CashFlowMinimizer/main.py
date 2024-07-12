from src.graph import Graph
from src.cash_flow import min_cash_flow

def main():
    g = Graph(3)
    g.add_edge(0, 1, 1000)
    g.add_edge(1, 2, 5000)
    g.add_edge(0, 2, 2000)

    min_cash_flow(g.get_graph())

if __name__ == "__main__":
    main()