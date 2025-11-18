"""
Unit tests for the tree complement problem solver.
"""

import unittest
from tree_complement import Graph, find_trees_with_tree_complement, verify_solution


class TestGraph(unittest.TestCase):
    """Test the Graph class."""
    
    def test_single_vertex_is_tree(self):
        """Test that a single vertex is a tree."""
        g = Graph(1)
        self.assertTrue(g.is_tree())
    
    def test_path_is_tree(self):
        """Test that a path graph is a tree."""
        g = Graph(4)
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        g.add_edge(2, 3)
        self.assertTrue(g.is_tree())
    
    def test_star_is_tree(self):
        """Test that a star graph is a tree."""
        g = Graph(4)
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(0, 3)
        self.assertTrue(g.is_tree())
    
    def test_cycle_is_not_tree(self):
        """Test that a cycle is not a tree."""
        g = Graph(4)
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        g.add_edge(2, 3)
        g.add_edge(3, 0)
        self.assertFalse(g.is_tree())
    
    def test_disconnected_is_not_tree(self):
        """Test that a disconnected graph is not a tree."""
        g = Graph(4)
        g.add_edge(0, 1)
        g.add_edge(2, 3)
        self.assertFalse(g.is_tree())
    
    def test_path_complement(self):
        """Test the complement of a path graph."""
        g = Graph(4)
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        g.add_edge(2, 3)
        
        comp = g.complement()
        expected_edges = {(0, 2), (0, 3), (1, 3)}
        self.assertEqual(comp.edges, expected_edges)
    
    def test_star_complement(self):
        """Test the complement of a star graph."""
        g = Graph(4)
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(0, 3)
        
        comp = g.complement()
        expected_edges = {(1, 2), (1, 3), (2, 3)}
        self.assertEqual(comp.edges, expected_edges)


class TestTreeComplement(unittest.TestCase):
    """Test the tree complement finding algorithm."""
    
    def test_single_vertex_has_tree_complement(self):
        """Test that a single vertex has a tree complement."""
        g = Graph(1)
        self.assertTrue(verify_solution(g))
    
    def test_path_4_has_tree_complement(self):
        """Test that path P₄ has a tree complement."""
        g = Graph(4)
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        g.add_edge(2, 3)
        self.assertTrue(verify_solution(g))
    
    def test_star_4_has_no_tree_complement(self):
        """Test that star K₁,₃ does NOT have a tree complement."""
        g = Graph(4)
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(0, 3)
        self.assertFalse(verify_solution(g))
    
    def test_path_3_has_no_tree_complement(self):
        """Test that path P₃ does NOT have a tree complement."""
        g = Graph(3)
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        self.assertFalse(verify_solution(g))
    
    def test_path_5_has_no_tree_complement(self):
        """Test that path P₅ does NOT have a tree complement."""
        g = Graph(5)
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        g.add_edge(2, 3)
        g.add_edge(3, 4)
        self.assertFalse(verify_solution(g))
    
    def test_find_all_solutions(self):
        """Test that we find exactly 2 solutions."""
        results = find_trees_with_tree_complement()
        self.assertEqual(len(results), 2)
        
        # Check n values
        n_values = [n for n, _, _ in results]
        self.assertIn(1, n_values)
        self.assertIn(4, n_values)
    
    def test_all_solutions_are_valid(self):
        """Test that all found solutions are actually valid."""
        results = find_trees_with_tree_complement()
        for n, tree, desc in results:
            self.assertTrue(verify_solution(tree), 
                          f"Solution {desc} with n={n} is not valid")


class TestComplement(unittest.TestCase):
    """Test complement computation."""
    
    def test_complement_of_single_vertex(self):
        """Test complement of single vertex."""
        g = Graph(1)
        comp = g.complement()
        self.assertEqual(len(comp.edges), 0)
        self.assertTrue(comp.is_tree())
    
    def test_complement_has_correct_edge_count(self):
        """Test that complement has the correct number of edges."""
        for n in range(1, 6):
            for num_edges in range(n):
                g = Graph(n)
                # Add some edges
                edges_added = 0
                for i in range(n-1):
                    if edges_added >= num_edges:
                        break
                    g.add_edge(i, i+1)
                    edges_added += 1
                
                comp = g.complement()
                total_possible = n * (n - 1) // 2
                self.assertEqual(len(g.edges) + len(comp.edges), total_possible)


if __name__ == '__main__':
    unittest.main()
