import csv


def main():
    # Open the file
    f = open('reviews_spotify.csv', 'r', encoding="utf8")
    # Create a reader object
    reader = csv.reader(f)
    # Create a set
    s = set()
    # Read each row in the file
    for row in reader:
        row = tuple(row)
        # Add the row to the set
        s.add(row)
    # Close the file
    f.close()
    # Print the set
    print(s)


if __name__ == '__main__':
    main()





