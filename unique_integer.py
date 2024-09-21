import os

# Define bounds for the integer range
LOW_LIMIT = -1023
HIGH_LIMIT = 1023
TOTAL_NUMBERS = HIGH_LIMIT - LOW_LIMIT + 1

# Function to read from the input file and save unique sorted numbers in the output file
def process_file(input_path, output_path):
    # Boolean list to track occurrence of integers
    number_tracker = [False] * TOTAL_NUMBERS

    try:
        with open(input_path, 'r') as infile:
            for line in infile:
                num = extract_integer(line.strip())
                if num is not None:
                    # Mark the number as found
                    number_tracker[num - LOW_LIMIT] = True

        with open(output_path, 'w') as outfile:
            # Write sorted unique numbers to output file
            for index in range(TOTAL_NUMBERS):
                if number_tracker[index]:
                    outfile.write(f"{index + LOW_LIMIT}\n")

    except (IOError, FileNotFoundError) as e:
        print(f"Error handling the file: {e}")

# Function to extract a valid integer from a line
def extract_integer(line):
    # Break the line into components based on whitespace
    elements = line.split()

    # Return None if there's more than one element or if it's not an integer
    if len(elements) != 1:
        return None

    # Try to convert to an integer and verify it falls within the specified range
    try:
        parsed_num = int(elements[0])
        if LOW_LIMIT <= parsed_num <= HIGH_LIMIT:
            return parsed_num
    except ValueError:
        return None

    return None

if __name__ == "__main__":
    input_file = 'DSA/small_sample_input_02.txt'
    output_file = 'DSA/sample_input_02.txt_results.txt'

    if os.path.isfile(input_file):
        process_file(input_file, output_file)
        print(f"File processing completed and saved to {output_file}")
    else:
        print(f"Error: Input file {input_file} not found")
