"""
Module to find all trees T such that the complement of T is also a tree.

Problem 4.23: Find all trees T such that T̄ (complement) is also a tree.

Mathematical Background:
- A tree is a connected acyclic graph
- The complement of a graph G = (V, E) is Ḡ = (V, Ē) where Ē contains all edges not in E
- For a tree with n vertices, it has exactly n-1 edges
- The complement has exactly n(n-1)/2 - (n-1) edges

Theorem: A tree T with n vertices has a complement T̄ that is also a tree if and only if:
1. n = 1 (trivial case: single vertex)
2. n = 4 and T is the path graph P₄ (vertices connected in a line 0-1-2-3)

Proof:
- For T̄ to be a tree with n vertices, it must have exactly n-1 edges
- T has n-1 edges, so T̄ has n(n-1)/2 - (n-1) edges
- For T̄ to be a tree: n(n-1)/2 - (n-1) = n-1
- Solving: n(n-1)/2 = 2(n-1)
- n(n-1) = 4(n-1)
- n(n-1) - 4(n-1) = 0
- (n-1)(n-4) = 0
- Therefore: n = 1 or n = 4

Verification for n = 4:
- Path P₄ (0-1-2-3): Complement edges are (0,2), (0,3), (1,3) → Tree ✓
- Star K₁,₃: Complement edges are (1,2), (1,3), (2,3) → Triangle (has cycle) ✗
"""

import itertools
from typing import List, Set, Tuple


class Graph:
    """Represents an undirected graph."""
    
    def __init__(self, num_vertices: int):
        self.num_vertices = num_vertices
        self.edges: Set[Tuple[int, int]] = set()
    
    def add_edge(self, u: int, v: int):
        """Add an undirected edge between vertices u and v."""
        if u > v:
            u, v = v, u
        self.edges.add((u, v))
    
    def is_connected(self) -> bool:
        """Check if the graph is connected using BFS."""
        if self.num_vertices == 0:
            return True
        if self.num_vertices == 1:
            return True
        
        # Build adjacency list
        adj = {i: [] for i in range(self.num_vertices)}
        for u, v in self.edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # BFS from vertex 0
        visited = set([0])
        queue = [0]
        
        while queue:
            curr = queue.pop(0)
            for neighbor in adj[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return len(visited) == self.num_vertices
    
    def has_cycle(self) -> bool:
        """Check if the graph has a cycle using DFS."""
        if self.num_vertices == 0:
            return False
        
        # Build adjacency list
        adj = {i: [] for i in range(self.num_vertices)}
        for u, v in self.edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()
        
        def dfs(node: int, parent: int) -> bool:
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor not in visited:
                    if dfs(neighbor, node):
                        return True
                elif neighbor != parent:
                    return True
            return False
        
        # Check all components
        for start in range(self.num_vertices):
            if start not in visited:
                if dfs(start, -1):
                    return True
        
        return False
    
    def is_tree(self) -> bool:
        """Check if the graph is a tree (connected and acyclic)."""
        if len(self.edges) != self.num_vertices - 1:
            return False
        return self.is_connected() and not self.has_cycle()
    
    def complement(self) -> 'Graph':
        """Return the complement graph."""
        comp = Graph(self.num_vertices)
        
        # Add all possible edges that are not in this graph
        for u in range(self.num_vertices):
            for v in range(u + 1, self.num_vertices):
                if (u, v) not in self.edges:
                    comp.add_edge(u, v)
        
        return comp
    
    def __str__(self) -> str:
        """String representation of the graph."""
        return f"Graph({self.num_vertices} vertices, {len(self.edges)} edges: {sorted(self.edges)})"


def create_star_graph(n: int) -> Graph:
    """Create a star graph K₁,ₙ₋₁ with n vertices."""
    tree = Graph(n)
    # Connect vertex 0 (center) to all other vertices
    for i in range(1, n):
        tree.add_edge(0, i)
    return tree


def create_path_graph(n: int) -> Graph:
    """Create a path graph Pₙ with n vertices."""
    tree = Graph(n)
    # Connect vertices in a path: 0-1-2-...-n-1
    for i in range(n - 1):
        tree.add_edge(i, i + 1)
    return tree


def find_trees_with_tree_complement() -> List[Tuple[int, Graph, str]]:
    """
    Find all trees T such that the complement of T is also a tree.
    
    Based on mathematical proof and verification:
    1. n = 1: Single vertex (trivial)
    2. n = 4: Path graph P₄ (0-1-2-3)
    
    Mathematical constraint: For a tree with n vertices to have a complement
    that is also a tree, we need n(n-1)/2 - (n-1) = n-1, which gives n=1 or n=4.
    
    However, not all trees with n=4 work:
    - Path P₄: ✓ Complement is also a tree
    - Star K₁,₃: ✗ Complement has a cycle (triangle)
    
    Returns:
        List of tuples (n, tree, description)
    """
    results = []
    
    # Case 1: Single vertex tree (n = 1)
    tree1 = Graph(1)
    results.append((1, tree1, "Single vertex (trivial)"))
    
    # Case 2: Path graph with 4 vertices (n = 4)
    tree4 = create_path_graph(4)
    results.append((4, tree4, "Path graph P₄ (0-1-2-3)"))
    
    return results


def verify_solution(tree: Graph) -> bool:
    """Verify that a tree has a complement that is also a tree."""
    if not tree.is_tree():
        return False
    
    complement = tree.complement()
    return complement.is_tree()


def display_results(results: List[Tuple[int, Graph, str]]):
    """Display the results in a readable format."""
    print("=" * 70)
    print("Problem 4.23: Trees T such that complement T̄ is also a tree")
    print("=" * 70)
    print()
    
    if not results:
        print("No trees found with tree complement.")
        return
    
    # Group by number of vertices
    by_vertices = {}
    for n, tree, desc in results:
        if n not in by_vertices:
            by_vertices[n] = []
        by_vertices[n].append((tree, desc))
    
    for n in sorted(by_vertices.keys()):
        print(f"Trees with {n} vertex/vertices:")
        print("-" * 70)
        
        for i, (tree, desc) in enumerate(by_vertices[n], 1):
            print(f"  Tree {i}: {desc}")
            print(f"    Structure: {tree}")
            print(f"    Edges: {sorted(tree.edges) if tree.edges else 'No edges (single vertex)'}")
            
            complement = tree.complement()
            print(f"    Complement edges: {sorted(complement.edges) if complement.edges else 'No edges'}")
            print(f"    Complement is tree: {complement.is_tree()} ✓")
            print()
    
    print("=" * 70)
    print("Summary:")
    print("-" * 70)
    print(f"Total trees found: {len(results)}")
    print()
    print("Complete answer:")
    print("  1. n = 1: Single vertex (trivial case)")
    print("  2. n = 4: Path graph P₄ where vertices are connected 0-1-2-3")
    print()
    print("Mathematical insight:")
    print("  • Only n=1 and n=4 satisfy the edge count constraint")
    print("  • For n=4, only the path graph P₄ works (not the star K₁,₃)")
    print("  • Path complement: (0,2), (0,3), (1,3) forms a tree")
    print("  • Star complement: (1,2), (1,3), (2,3) forms a triangle (cycle)")
    print("=" * 70)


if __name__ == "__main__":
    print("Finding all trees T such that T̄ (complement) is also a tree...")
    print()
    
    # Find the trees (based on mathematical proof and verification)
    results = find_trees_with_tree_complement()
    
    # Verify each solution
    print("Verifying solutions...")
    for n, tree, desc in results:
        is_valid = verify_solution(tree)
        print(f"  n={n} ({desc}): {'✓ Valid' if is_valid else '✗ Invalid'}")
    print()
    
    display_results(results)
