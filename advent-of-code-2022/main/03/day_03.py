LOWERCASE_NORMALIZER = 96
UPPERCASE_NORMALIZER = 38
GROUP_SIZE = 3


def get_priority(char: str) -> int:
    if 'a' <= char <= 'z':
        return ord(char) - LOWERCASE_NORMALIZER
    elif 'A' <= char <= 'Z':
        return ord(char) - UPPERCASE_NORMALIZER


def process_rucksack(rucksack: str) -> int:
    divider = len(rucksack) // 2
    compartment_a_uniques, compartment_b_uniques = set(rucksack[:divider]), set(rucksack[divider:])
    commons = compartment_a_uniques & compartment_b_uniques
    return get_priority(commons.pop())


def process_file_part_one(filename: str) -> int:
    total = 0
    with open(filename) as f:
        for line in f:
            total += process_rucksack(line.strip())
    return total


def process_group(group: list[str]) -> int:
    commons = set(group[0]) & set(group[1]) & set(group[2])
    return get_priority(commons.pop())


def process_file_part_two(filename: str) -> int:
    total = 0
    with open(filename) as f:
        group = []
        for line in f:
            group.append(line.strip())
            if len(group) == GROUP_SIZE:
                total += process_group(group)
                group = []
    return total


# print(get_priority('z'))
# print(get_priority('Z'))
# print(process_rucksack('vJrwpWtwJgWrhcsFMMfFFhFp'))


print("----- Part 1 -----")
print(process_file_part_one("sample.txt"))
print(process_file_part_one("input.txt"))
print("----- Part 2 -----")
print(process_file_part_two("sample.txt"))
print(process_file_part_two("input.txt"))
