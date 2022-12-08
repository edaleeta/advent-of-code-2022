import copy

CHARS_APART = 4


def parse_starting_state(filename: str, num_stacks: int) -> list[list[str]]:
    stacks = [[] for _ in range(num_stacks)]
    with open(filename) as f:
        for line_number, line in enumerate(reversed(list(f.readlines()))):
            # skip numbers row
            if line_number == 0:
                continue
            i = 1
            stack_number = 0
            while i < len(line):
                value = line[i]
                if value.strip():
                    stacks[stack_number].append(value)
                i += CHARS_APART
                stack_number += 1
    return stacks


def apply_direction(
        stacks: list[list[str]],
        direction: str,
        is_part_two: bool = False,
) -> list[list[str]]:
    new_stacks = copy.deepcopy(stacks)

    _, num_to_move, _, start_stack, _, end_stack = direction.split()
    num_to_move = int(num_to_move)
    # convert to 0-index
    start_stack = int(start_stack) - 1
    end_stack = int(end_stack) - 1

    to_append = [new_stacks[start_stack].pop() for _ in range(num_to_move)]

    if is_part_two:
        to_append.reverse()

    new_stacks[end_stack].extend(to_append)

    return new_stacks


def process_directions(
        filename: str,
        stacks: list[list[str]],
        is_part_two: bool = False
) -> str:
    with open(filename) as f:
        for line in f:
            direction = line.strip()
            stacks = apply_direction(stacks, direction, is_part_two)

    return "".join([stack[-1] for stack in stacks if stack])


print("----- Sample -----")
start_stacks = parse_starting_state("sample-state.txt", num_stacks=3)
print(process_directions("sample-directions.txt", start_stacks))

print("----- Part 1 -----")
start_stacks = parse_starting_state("input-state.txt", num_stacks=10)
print(process_directions("input-directions.txt", start_stacks))

print("----- Part 2 -----")
start_stacks = parse_starting_state("sample-state.txt", num_stacks=3)
print(process_directions("sample-directions.txt", start_stacks, is_part_two=True))

start_stacks = parse_starting_state("input-state.txt", num_stacks=10)
print(process_directions("input-directions.txt", start_stacks, is_part_two=True))