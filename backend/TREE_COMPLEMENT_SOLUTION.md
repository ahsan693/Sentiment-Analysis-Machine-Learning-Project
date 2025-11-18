# Problem 4.23: Trees with Tree Complements

## Problem Statement
Find all trees T such that the complement T̄ is also a tree.

## Solution

### Answer
There are exactly **2 trees** (up to isomorphism) that satisfy this property:

1. **n = 1**: A single vertex (trivial case)
2. **n = 4**: The path graph P₄ with vertices connected as 0-1-2-3

### Mathematical Proof

#### Edge Count Constraint
For a tree T with n vertices:
- T has exactly **n - 1** edges
- The complement T̄ has **n(n-1)/2 - (n-1)** edges

For T̄ to also be a tree with n vertices, it must have **n - 1** edges.

Setting up the equation:
```
n(n-1)/2 - (n-1) = n - 1
n(n-1)/2 = 2(n-1)
n(n-1) = 4(n-1)
n² - n = 4n - 4
n² - 5n + 4 = 0
(n-1)(n-4) = 0
```

**Therefore: n = 1 or n = 4**

#### Verification for n = 4
There are exactly 2 non-isomorphic trees with 4 vertices:

1. **Path P₄** (0-1-2-3):
   - Original edges: (0,1), (1,2), (2,3)
   - Complement edges: (0,2), (0,3), (1,3)
   - The complement is connected and has no cycles ✓
   - **The complement IS a tree!**

2. **Star K₁,₃** (center 0 connected to 1, 2, 3):
   - Original edges: (0,1), (0,2), (0,3)
   - Complement edges: (1,2), (1,3), (2,3)
   - The complement forms a triangle (3-cycle) ✗
   - **The complement is NOT a tree!**

### Visualization

#### Case 1: n = 1
```
Original: •
Complement: •
```
Both are trivially trees.

#### Case 2: n = 4 (Path P₄)
```
Original (Path):
0 — 1 — 2 — 3

Complement:
0       2
 \     / \
  \   /   \
   \ /     3
    1
    
Edges: (0,2), (0,3), (1,3)
This forms a tree!
```

#### Counter-example: n = 4 (Star K₁,₃)
```
Original (Star):
    1
    |
0 — 0 — 2
    |
    3

Complement (Triangle):
1 — 2
 \ /
  3
  
Edges: (1,2), (1,3), (2,3)
This forms a cycle, NOT a tree!
```

## Usage

### Run the solver
```bash
python tree_complement.py
```

### Run tests
```bash
python -m unittest test_tree_complement -v
```

### Import as a module
```python
from tree_complement import find_trees_with_tree_complement, verify_solution, Graph

# Find all solutions
results = find_trees_with_tree_complement()
for n, tree, description in results:
    print(f"n={n}: {description}")

# Verify a specific tree
tree = Graph(4)
tree.add_edge(0, 1)
tree.add_edge(1, 2)
tree.add_edge(2, 3)

if verify_solution(tree):
    print("This tree has a complement that is also a tree!")
```

## Files
- `tree_complement.py` - Main solver implementation
- `test_tree_complement.py` - Unit tests
- `test_4_vertex_trees.py` - Detailed analysis of all 4-vertex trees
- `TREE_COMPLEMENT_SOLUTION.md` - This documentation

## Key Insights
1. The edge count constraint limits solutions to n=1 or n=4
2. For n=4, the structure matters: only the path graph works
3. The star graph's complement forms a triangle, which has a cycle
4. This is a rare case in graph theory where complementation preserves the tree property
