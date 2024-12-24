
ORDER = {}

with open('input', 'r') as update_rules:
    rules, updates = update_rules.read().strip().split('\n\n')
    for rule in rules.split('\n'):
        prior, post = map(int, rule.split('|'))
        if not (prior in ORDER):
            ORDER[prior] = set()
        ORDER[prior].add(post)
    # part 1
    def fix_in_place(update):
        copy=update
        good = False
        while good == False:
            good = True
            for i in range(len(copy)-1):
                check = copy[i]
                if check not in ORDER:
                    continue
                for x in range(i, len(copy)):
                    if copy[x] in ORDER[check]:
                        good = False
                        # swap
                        copy[x], copy[i] = copy[i], copy[x]
                        break
        return copy
    valid_updates = []
    invalid_updates = []
    for update in updates.split('\n'):
        pages = list(reversed(list(map(int, update.split(',')))))
        valid = True
        for i in range(len(pages)-1):
            check = pages[i]
            if check not in ORDER:
                continue
            for x in range(i, len(pages)):
                if pages[x] in ORDER[check]:
                    valid = False
                    break
            if valid == False:
                break
        if valid:
            valid_updates.append(pages)
        else:
            invalid_updates.append(pages)

    part1_sum = 0
    for update in valid_updates:
        part1_sum += update[len(update)//2]
    print("Part 1:", part1_sum)
    # part 2
    part2_sum = 0
    for invalid_update in invalid_updates:
        fixed = fix_in_place(invalid_update)
        part2_sum += fixed[len(fixed)//2]
    print("Part 2:", part2_sum)


