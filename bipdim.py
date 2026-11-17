import sys


def read_instance(path):
    """Read a bipartite graph. Returns (n_u, n_v, set of edges (u, v))."""
    n_u = n_v = None
    edges = set()
    with open(path) as f:
        for line in f:
            line = line.split("#")[0].strip()   # drop comments
            if not line:
                continue
            a, b = map(int, line.split())
            if n_u is None:                     # first line = sizes
                n_u, n_v = a, b
            else:
                if not (0 <= a < n_u and 0 <= b < n_v):
                    raise ValueError(f"edge ({a}, {b}) out of range")
                edges.add((a, b))
    if n_u is None:
        raise ValueError("empty instance file")
    return n_u, n_v, edges

def u_var(u, l, k):
    """Variable number for 'U vertex u is in biclique l' (l = 0..k-1)."""
    return u * k + l + 1


def v_var(v, l, n_u, k):
    """Variable number for 'V vertex v is in biclique l' (l = 0..k-1)."""
    return n_u * k + v * k + l + 1

def encode(n_u, n_v, edges, k):
    """Building the CNF, returns a list of clauses such that each clause = list of ints."""
    clauses = []

    # Rule 1: non-adjacent u, v never share a biclique
    for u in range(n_u):
        for v in range(n_v):
            if (u, v) not in edges:
                for l in range(k):
                    clauses.append([-u_var(u, l, k), -v_var(v, l, n_u, k)])

    return clauses

if __name__ == "__main__":
    n_u, n_v, edges = read_instance(sys.argv[1])
    k = int(sys.argv[2])
    clauses = encode(n_u, n_v, edges, k)
    print(f"{len(clauses)} clauses")
    for c in clauses:
        print(c)