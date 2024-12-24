
with open("input", "r") as topography_file:
    topography = list(map(list, topography_file.read().strip().split('\n')))
    trail_heads = []
    for y, line in enumerate(topography):
        for x, token in enumerate(line):
            if token == '0':
                trail_heads.append((y, x))
    def get_neighbors(y, x):
        return [(y, x) for y,x in [(y+1, x), (y-1, x), (y, x+1), (y, x-1)] if (-1 < x < len(topography[0])) and (-1 < y < len(topography))]

    def search(root):
        # Part 1 find unique terminal points
        searched = set()
        nodes = [root]
        while len(nodes) > 0:
            current_node = nodes.pop()
            neighbors = filter(lambda x: x not in searched, get_neighbors(current_node[0], current_node[1]))
            for (ny, nx) in neighbors:
                cost = int(topography[ny][nx]) - int(topography[current_node[0]][current_node[1]])
                if cost == 1:
                    nodes.append((ny,nx))
            # ok, we processed this node
            searched.add(current_node)
        return sum([1 for y,x in searched if topography[y][x] == '9'])
    
    def find_paths(root):
        # Part 2 find unique paths to terminal points
        nodes = [root]
        paths = [[root]]
        while len(nodes) > 0:
            current_node = nodes.pop()
            current_paths = list(filter(lambda x: current_node == x[-1], paths))
            neighbors = get_neighbors(current_node[0], current_node[1])
            for (ny, nx) in neighbors:
                cost = int(topography[ny][nx]) - int(topography[current_node[0]][current_node[1]])
                if cost == 1:
                    for path in current_paths:
                        if path+[(ny,nx)] not in paths:
                            paths.append(path + [(ny,nx)])
                    nodes.append((ny,nx))
        return list(filter(lambda x: topography[x[-1][0]][x[-1][1]] == '9', paths))


    print("Part 1:", sum(map(search, trail_heads)))
    print("Part 2:", sum(map(len, map(find_paths, trail_heads))) )
