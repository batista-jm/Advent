def count_normal(txt):
    total = 0
    for y in range(len(txt)):  # Iterate over rows
        x = 0
        while x < len(txt[y]) - 3:  # Ensure there's space for a 4-character comparison
            if (
                txt[y][x] == 'X' and
                txt[y][x + 1] == 'M' and
                txt[y][x + 2] == 'A' and
                txt[y][x + 3] == 'S'
            ):
                total += 1
                x += 4  # Skip ahead to avoid overlapping matches
            else:
                x += 1
    return total


def count_reverse(txt):
    total = 0
    for y in range(len(txt)):  # Iterate over rows
        x = 0
        while x < len(txt[y]) - 3:  # Ensure there's space for a 4-character comparison
            if (
                txt[y][x] == 'S' and
                txt[y][x + 1] == 'A' and
                txt[y][x + 2] == 'M' and
                txt[y][x + 3] == 'X'
            ):
                total += 1
                x += 4  # Skip ahead to avoid overlapping matches
            else:
                x += 1
    return total


def count_vertical(txt):
    

def main():
    file_name = "db4.txt"

    # First, read the file and populate a 2D list
    txt = []
    with open(file_name, 'r') as file:
        for line in file:
            txt.append(list(line.strip()))  # Convert each line into a list of characters

    # Count occurrences of "XMAS" in the 2D list
    result = count_normal(txt) + count_reverse(txt)
    print(f"Total occurrences of 'XMAS': {result}")


if __name__ == "__main__":
    main()
