import unittest
from src.graph import Graph

class TestGraph(unittest.TestCase):
    def test_add_edge(self):
        g = Graph(3)
        g.add_edge(0, 1, 1000)
        self.assertEqual(g.get_graph()[0][1], 1000)

if __name__ == "__main__":
    unittest.main()