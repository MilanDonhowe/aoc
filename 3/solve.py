import re
from functools import reduce
with open("input", "r") as input_file:
    corrupted_program = input_file.read()
# uncomment to test
#corrupted_program="xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
good_mul = re.findall(r'mul\(\d{1,3},\d{1,3}\)', corrupted_program)
print("Part 1: ", sum([reduce(lambda a,b: int(a,10)*int(b,10), re.findall(r'\d+', instruction)) for instruction in good_mul]))

parsed_text=[]
include = True
last_i = 0
for match in re.finditer(r"don't()|do()", corrupted_program):
    span = match.span(0)
    if match.group(0) == "don't" and include == True:
        parsed_text.append(corrupted_program[last_i:span[0]])
        include = False
    if match.group(0) == 'do' and include == False:
        include = True
        last_i = span[1]+1
if include == True:
    parsed_text.append(corrupted_program[last_i:])
corrupted_test = ''.join(parsed_text)
good_mul = re.findall(r'mul\(\d{1,3},\d{1,3}\)', corrupted_test)
print("Part 2:",sum([reduce(lambda a,b: int(a,10)*int(b,10), re.findall(r'\d+', instruction)) for instruction in good_mul]))
