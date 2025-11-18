"""
Test all possible trees with 4 vertices to find which have tree complements.
"""

from tree_complement import Graph

def test_all_4_vertex_trees():
    """Test all possible tree structures with 4 vertices."""
    
    # All possible trees with 4 vertices (labeled 0, 1, 2, 3)
    # There are only 2 non-isomorphic trees with 4 vertices:
    # 1. Path graph: 0-1-2-3
    # 2. Star graph: 0 connected to 1, 2, 3
    
    trees = []
    
    # Tree 1: Path graph 0-1-2-3
    path = Graph(4)
    path.add_edge(0, 1)
    path.add_edge(1, 2)
    path.add_edge(2, 3)
    trees.append(("Path (0-1-2-3)", path))
    
    # Tree 2: Star graph K_{1,3} with center at vertex 0
    star = Graph(4)
    star.add_edge(0, 1)
    star.add_edge(0, 2)
    star.add_edge(0, 3)
    trees.append(("Star K_{1,3}", star))
    
    # Test each tree
    print("=" * 80)
    print("Testing all non-isomorphic trees with 4 vertices")
    print("=" * 80)
    print()
    
    valid_trees = []
    
    for name, tree in trees:
        print(f"{name}:")
        print(f"  Edges: {sorted(tree.edges)}")
        print(f"  Is tree: {tree.is_tree()}")
        
        complement = tree.complement()
        print(f"  Complement edges: {sorted(complement.edges)}")
        print(f"  Complement is connected: {complement.is_connected()}")
        print(f"  Complement has cycle: {complement.has_cycle()}")
        print(f"  Complement is tree: {complement.is_tree()}")
        
        if complement.is_tree():
            valid_trees.append((name, tree))
            print(f"  ✓ THIS TREE HAS A TREE COMPLEMENT!")
        else:
            print(f"  ✗ Complement is not a tree")
        
        print()
    
    print("=" * 80)
    print("CONCLUSION:")
    print("=" * 80)
    if valid_trees:
        print(f"Found {len(valid_trees)} tree(s) with 4 vertices that have tree complements:")
        for name, tree in valid_trees:
            print(f"  - {name}")
    else:
        print("NO trees with 4 vertices have complements that are also trees!")
    print()
    print("Therefore, the ONLY tree with a tree complement is:")
    print("  • n = 1: Single vertex (trivial case)")
    print("=" * 80)

if __name__ == "__main__":
    test_all_4_vertex_trees()
