def get_marker_position(chars: str, window_size: int = 4) -> int:
    i = 0
    while i < len(chars) - window_size:
        unique_chars = set(chars[i:i+window_size])
        if len(unique_chars) == window_size:
            return i + window_size
        i += 1
    return -1


def process_file(filename: str, is_part_two: bool = False) -> int:
    with open(filename) as f:
        line = f.readline().strip()
        window_size = 14 if is_part_two else 4
        return get_marker_position(line, window_size)

print("----- Samples -----")
print(get_marker_position("bvwbjplbgvbhsrlpgdmjqwftvncz"))
print(get_marker_position("nppdvjthqldpwncqszvftbrmjlhg"))
print(get_marker_position("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"))
print(get_marker_position("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"))

print("----- Part 1 -----")
print(process_file("input.txt"))

print("----- Part 2 -----")
print(process_file("input.txt", is_part_two=True))
