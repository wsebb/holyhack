import csv


def get_dict():
    # Open the file
    f = open('reviews_spotify.csv', 'r', encoding="utf8")
    # Create a reader object
    reader = csv.reader(f)
    # Create a set
    d = dict()
    # Read each row in the file
    count = 0
    for row in reader:
        review = dict()
        review['review'] = row[1]
        review['rating'] = row[2]
        review['thumbs_up'] = row[3]
        review['reply'] = row[4]

        d[count] = review
        count += 1
    # Close the file
    f.close()
    # Print the set
    return d


def get_dict_json():
    # read a json file and make a dictionary from it
    import json
    with open('reviews_pakket.json', encoding="utf8") as f:
        data = json.load(f)
        if isinstance(data, list):
            data = {i: d for i, d in enumerate(data)}
    return data

print(get_dict_json())
print(len(get_dict_json()))
print(type(get_dict_json()))
