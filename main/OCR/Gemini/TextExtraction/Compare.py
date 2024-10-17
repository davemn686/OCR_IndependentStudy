import sys

def compare_arrays(expectedArr, resultArr):
    # Compare the two arrays element by element
    differences = []
    min_length = min(len(expectedArr), len(resultArr))

    # Iterate through both arrays and compare their elements
    for i in range(min_length):
        if expectedArr[i] != resultArr[i]:
            differences.append((i, expectedArr[i], resultArr[i]))

    # Check if one array is longer than the other
    if len(expectedArr) > len(resultArr):
        differences.extend([(i, expectedArr[i], None) for i in range(min_length, len(expectedArr))])
    elif len(resultArr) > len(expectedArr):
        differences.extend([(i, None, resultArr[i]) for i in range(min_length, len(resultArr))])

    # Output the differences
    if differences:
        for index, expected, result in differences:
            print(f"Difference at index {index}: expected '{expected}' but got '{result}'")
    else:
        print("Both arrays match exactly!")

# This function reads arrays passed as arguments
if __name__ == "__main__":
    # Ensure the correct number of arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python Compare.py '<expectedArr_str>' '<resultArr_str>'")
        sys.exit(1)

    # Parse the two arguments (which are comma-separated strings) and convert them to lists
    expectedArr_str = sys.argv[1]
    resultArr_str = sys.argv[2]

    # Convert the comma-separated strings back into lists
    expectedArr = expectedArr_str.split(',')
    resultArr = resultArr_str.split(',')

    # Perform the comparison
    compare_arrays(expectedArr, resultArr)
