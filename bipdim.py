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


if __name__ == "__main__":
    n_u, n_v, edges = read_instance(sys.argv[1])
    print(f"|U| = {n_u}, |V| = {n_v}, {len(edges)} edges")
    print(sorted(edges))