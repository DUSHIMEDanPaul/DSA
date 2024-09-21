import os

# Constants for the integer range
MIN_INT = -1023
MAX_INT = 1023
RANGE_SIZE = MAX_INT - MIN_INT + 1

# Process the file and write unique sorted integers to the destination file
def handle_file(src_file_path, dest_file_path):
    # Initialize a boolean array to track unique integers
    unique_numbers = [False] * RANGE_SIZE

    try:
        with open(src_file_path, 'r') as src_file:
            for line in src_file:
                value = parse_line(line.strip())
                if value is not None:
                    # Mark the integer as seen
                    unique_numbers[value - MIN_INT] = True

        with open(dest_file_path, 'w') as dest_file:
            # Write out the unique sorted integers
            for i in range(RANGE_SIZE):
                if unique_numbers[i]:
                    dest_file.write(f"{i + MIN_INT}\n")

    except (FileNotFoundError, IOError) as error:
        print(f"File operation failed: {error}")

# Parse a line to check if it contains a valid single integer
def parse_line(line):
    # Split the line by whitespace
    parts = line.split()

    # Skip if there are multiple numbers or non-integer input
    if len(parts) != 1:
        return None

    # Check if the part is a valid integer and within the specified range
    try:
        number = int(parts[0])
        if MIN_INT <= number <= MAX_INT:
            return number
    except ValueError:
        pass

    return None

if __name__ == "__main__":
    src_path = 'DSA/small_sample_input_02.txt'
    dest_path = 'DSA/sample_input_02.txt_results.txt'

    if os.path.exists(src_path):
        handle_file(src_path, dest_path)
        print(f"The file has been processed and saved to {dest_path}")
    else:
        print(f"The file {src_path} is not found")
