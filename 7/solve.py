
with open('input', 'r') as calculations_file:
    calculations = calculations_file.read().strip().split('\n')
    part1_sum = 0
    for calculation in calculations:
        result, parameters = calculation.split(':')
        parameters = list(map(int, parameters.split()))
        result = int(result)
        steps=[parameters[0]]
        for p in parameters[1:]:
            next_steps = []
            for c in steps:
                next_steps.append(c + p)
                next_steps.append(c * p)
            steps = next_steps
        if result in steps:
            part1_sum += result
    print('Part 1:', part1_sum)
    # part 2 (copy & paste babyyyy)
    part2_sum = 0
    for calculation in calculations:
        result, parameters = calculation.split(':')
        parameters = list(map(int, parameters.split()))
        result = int(result)
        steps=[parameters[0]]
        for p in parameters[1:]:
            next_steps = []
            for c in steps:
                next_steps.append(c + p)
                next_steps.append(c * p)
                next_steps.append(int(str(c)+str(p)))
            steps = next_steps
        if result in steps:
            part2_sum += result
    print('Part 2:', part2_sum)
