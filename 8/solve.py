from copy import deepcopy
with open("input", "r") as layout_file:
    layout = layout_file.read().strip().split('\n')
    boundry = (len(layout[0]), len(layout))
    all_stations = {}
    for y, line in enumerate(layout):
        for x, token in enumerate(line):
            if token != '.':
                if token not in all_stations:
                    all_stations[token]=[]
                all_stations[token].append((x,y))
    def in_bounds(point):
        return (-1 < point[0] < boundry[0]) and (-1 < point[1] < boundry[1])
    # let's check each station to determine what antinodes they create
    # part 1:
    antinodes = set()
    for station_id in all_stations:
        stations = all_stations[station_id]
        
        for i in range(len(stations)-1):
            for j in range(i+1, len(stations)):
                station_a_x, station_a_y = stations[i]
                station_b_x, station_b_y = stations[j]
                delta_x = station_b_x - station_a_x
                delta_y = station_b_y - station_a_y
                a1 = (station_a_x + delta_x*2, station_a_y + delta_y*2)
                # I believe we need to change signs here (since we calculate delta going from station a first)
                a2 = (station_b_x - delta_x*2, station_b_y - delta_y*2)
                # check if this points can exist in our grid as coordinates
                #print(f"* DEBUG: ({station_a_x},{station_a_y}) and ({station_b_x},{station_b_y}) create antinodes {a1}, {a2}")
                for antinode in [a1,a2]:
                    if in_bounds(antinode):
                        antinodes.add(antinode)
    # Debugging purposes
    #layout_copy = list(map(list, deepcopy(layout)))
    #for x,y in antinodes:
    #    layout_copy[y][x]='#'
    #for line in layout_copy:
    #    print(''.join(line))
    print("Part 1:", len(antinodes))
    # part 2:
    antinodes = set()
    for station_id in all_stations:
        stations = all_stations[station_id]
        
        for i in range(len(stations)-1):
            for j in range(i+1, len(stations)):
                station_a_x, station_a_y = stations[i]
                station_b_x, station_b_y = stations[j]
                delta_x = station_b_x - station_a_x
                delta_y = station_b_y - station_a_y
                a1 = (station_a_x + delta_x*2, station_a_y + delta_y*2)
                while in_bounds(a1):
                    antinodes.add(a1)
                    a1 = (a1[0]+delta_x, a1[1]+delta_y)
                a2 = (station_b_x - delta_x*2, station_b_y - delta_y*2)
                # check if this points can exist in our grid as coordinates
                while in_bounds(a2):
                    antinodes.add(a2)
                    a2 = (a2[0] - delta_x, a2[1] - delta_y)
                antinodes.add(stations[i])
                antinodes.add(stations[j])
    #layout_copy = list(map(list, deepcopy(layout)))
    #for x,y in antinodes:
    #    layout_copy[y][x]='#'
    #for line in layout_copy:
    #    print(''.join(line))
    print("Part 2:", len(antinodes))
    
