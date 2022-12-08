class Range:
    def __init__(self, minimum: int, maximum: int):
        self.min = minimum
        self.max = maximum

    def __repr__(self):
        return f"({self.min}-{self.max})"

    def contains_range(self, other: "Range") -> bool:
        return self.min <= other.min and self.max >= other.max

    def has_any_overlap(self, other: "Range") -> bool:
        return not (self.min > other.max or self.max < other.min)


def parse_range_raw_to_range(range_raw: str) -> Range:
    minimum, maximum = [int(value) for value in range_raw.split("-")]
    return Range(minimum, maximum)


def parse_to_ranges(line) -> tuple[Range, Range]:
    range_a_raw, range_b_raw = line.strip().split(",")
    return (
        parse_range_raw_to_range(range_a_raw),
        parse_range_raw_to_range(range_b_raw),
    )


def is_range_contained(a: Range, b: Range) -> bool:
    return a.contains_range(b) or b.contains_range(a)


def process_input(filename, is_part_two=False) -> int:
    overlaps = 0
    with open(filename) as f:
        for line in f:
            a, b = parse_to_ranges(line.strip())
            if is_part_two:
                overlaps += 1 if a.has_any_overlap(b) else 0
            else:
                overlaps += 1 if is_range_contained(a, b) else 0

    return overlaps

# print(is_range_contained(*parse_to_ranges("2-8,3-7")))  # -> True
# print(is_range_contained(*parse_to_ranges("2-6,4-8")))  # -> False

print("----- Part 1 -----")
print(process_input("sample.txt"))
print(process_input("input.txt"))
print("----- Part 2 -----")
print(process_input("sample.txt", is_part_two=True))
print(process_input("input.txt", is_part_two=True))
