from copy import deepcopy
FREE_SPACE='.'
with open("input", "r") as disk_map_file:
    disk_map = disk_map_file.read().strip()
    disk = []
    id=0
    for index, size in enumerate(disk_map):
        indicator = FREE_SPACE
        if index % 2 == 0:
            indicator=id
            id+=1
        for x in range(int(size)):
            disk.append(indicator)
    # re-arrange disk right -> left
    def print_disk():
        print(''.join(map(str,disk)))
    #print_disk()
    disk_copy = deepcopy(disk)
    # Part 1
    insert_idx = 0
    def increment_insert_idx():
        global insert_idx
        while insert_idx < len(disk) and disk[insert_idx] != FREE_SPACE:
            insert_idx += 1
    increment_insert_idx()
    for j in range(len(disk)-1, -1, -1):
        if disk[j] != FREE_SPACE and j > insert_idx:
            disk[insert_idx]=disk[j]
            disk[j] = FREE_SPACE
            increment_insert_idx()
    #print_disk()
    checksum = sum([i * id for i, id in enumerate(disk) if id != FREE_SPACE])
    print("Part 1:", checksum)
    # part 2
    disk=disk_copy
    #print_disk()
    # init moving window
    free_spaces = [i for i,v in enumerate(disk) if v == FREE_SPACE]
    free_blocks = [] #( start i, end i, size)
    fb_start = free_spaces[0]
    fb_end = fb_start
    for i in free_spaces[1:]:
        if i - fb_end > 1:
            free_blocks.append([fb_start, fb_end, fb_end - fb_start + 1])
            fb_start = i
            fb_end = i
            continue
        fb_end = i
    free_blocks.append([fb_start, fb_end, fb_end-fb_start+1])
    processed = set()
    for j in range(len(disk)-1, -1, -1):
        if (disk[j] != FREE_SPACE) and (disk[j] not in processed):
            processed.add(disk[j])
            #print(f'processing {disk[j]}')
            block_end = j
            block_start = j
            while disk[block_start] == disk[j] and block_start > -1:
                block_start -= 1
            block_size = block_end - block_start
            block_start += 1
            no_matches = True
            for i, fb in enumerate(free_blocks):
                if block_size <= fb[2] and fb[0] < block_start:
                    no_matches = False
                    # perform swap
                    #print('performing swap')
                    for write_i, blank_i in zip(range(fb[0], fb[0]+block_size), range(block_start, block_start+block_size)):
                        disk[write_i] = disk[j]
                        disk[blank_i] = FREE_SPACE
                    # update free block metadata
                    fb[2] -= block_size
                    fb[0] = fb[0]+block_size
                    assert fb[0] == free_blocks[i][0]
                    assert fb[2] == free_blocks[i][2]
                    break


    checksum = sum([i * id for i, id in enumerate(disk) if id != FREE_SPACE])
    print("Part 2:", checksum)
