import heapq


def get_highest_calories(file_name, n=1):
    highest_calories = []
    running_sum = 0

    with open(file_name) as file:
        for line in file:
            line = line.strip()

            if line == "":
                if len(highest_calories) < n:
                    heapq.heappush(highest_calories, running_sum)
                else:
                    heapq.heappushpop(highest_calories, running_sum)
                running_sum = 0

            else:
                running_sum += int(line)
    heapq.heappushpop(highest_calories, running_sum)
    return sum(highest_calories)


print(get_highest_calories("sample.txt"))
print(get_highest_calories("input.txt"))
print(get_highest_calories("input.txt", n=3))
