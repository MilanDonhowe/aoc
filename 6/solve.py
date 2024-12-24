from copy import deepcopy
import numpy as np

def simulate(area, start):
    seen_states = set()
    direction = np.array([-1,0])
    location = start
    seen_states.add((location[0],location[1],direction[0],direction[1]))
    while (-1 < location[0] < len(area)) and (-1 < location[1] < len(area[0])):
        ny = location[0]+direction[0]
        nx = location[1]+direction[1]
        if (-1 < ny < len(area)) and (-1 < nx < len(area[0])):
            if area[ny][nx] == '#':
                # rotation matrix
                direction = np.array([[0,1],[-1,0]]) @ direction
                continue
        location = [ny,nx]
        # loop check
        if (location[0], location[1], direction[0], direction[1]) in seen_states:
            return True
        seen_states.add((location[0], location[1], direction[0], direction[1]))
    return False

with open("input", "r") as area_file:
    area = list(map(list, area_file.read().strip().split('\n')))
    visited = deepcopy(area)
    location=(-1,-1)
    direction= np.array([-1,0])
    for y, line in enumerate(area):
        for x, token in enumerate(line):
            if token == '^':
                area[y][x]='.'
                location=(y,x)
                break
    part1_count=0
    start = location
    obstacles = set()
    while (-1 < location[0] < len(area)) and (-1 < location[1] < len(area[0])):
        if visited[location[0]][location[1]] != 'X':
            part1_count += 1
            visited[location[0]][location[1]]='X'
            obstacles.add((location[0], location[1]))
        ny = location[0]+direction[0]
        nx = location[1]+direction[1]
        if (-1 < ny < len(area)) and (-1 < nx < len(area[0])):
            if area[ny][nx] == '#':
                # rotation matrix
                direction = np.array([[0,1],[-1,0]]) @ direction
                continue
        location = [ny,nx]
    print("Part 1:", part1_count)
    # Part 2 logic, check if adding an obstruction here creates a loop
    obstacles.remove(start) # exclude starting location
    part2_count=0
    for ob in obstacles:
        hypothetical_map = deepcopy(area)
        hypothetical_map[ob[0]][ob[1]]='#'
        if simulate(hypothetical_map, start):
            part2_count += 1
    print("part 2:", part2_count)