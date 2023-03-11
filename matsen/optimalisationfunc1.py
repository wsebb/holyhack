import utils
import os
import numpy as np



def optimisationfunc(review):
    value = 0
    review_text = get_review_text(review)

    #criteria

    likes = review['thumbs_up']
    premium = get_premium(review_text)
    trial = get_trial(review_text)
    subscription = get_subscription(review_text)
    aantal_woorden = get_aantal_woorden(review_text)
    aantal_scheldwoorden = get_aantal_scheldwoorden(review_text)

    #weights
    value = 1 * np.log(1 + int(likes)) + 1 * np.log(1 + aantal_woorden) - 1 * np.log(1 + aantal_scheldwoorden) #logarithmic scale
    if premium or trial or subscription:
        value += 1.5
    review["score"] = round(value, 2)

def get_review_text(dict_reviews):
    return dict_reviews['review']

def get_premium(review_text):
    woorden = review_text.split()
    list_of_premium = read_file("/premium.txt")


    for i in range(len(woorden)):
        for j in range(len(list_of_premium)):
            if list_of_premium[j] == woorden[i]:
                return True
    return False

def get_trial(review_text):
    woorden = review_text.split()
    list_of_trial = read_file('/trial.txt')
    for i in range(len(woorden)):
        for j in range(len(list_of_trial)):
            if list_of_trial[j] == woorden[i]:
                return True
    return False

def get_subscription(review_text):
    woorden = review_text.split()
    list_of_subscription = read_file('/subscription.txt')
    for i in range(len(woorden)):
        for j in range(len(list_of_subscription)):
            if list_of_subscription[j] == woorden[i]:
                return True
    return False

def get_aantal_woorden(review_text):
    woorden = review_text.split()
    return len(woorden)

def get_aantal_scheldwoorden(review_text):
    woorden = review_text.split()
    list_of_scheldwoorden = read_file('/badwords.txt')
    aantal = 0
    for i in range(len(woorden)):
        for j in range(len(list_of_scheldwoorden)):
            if list_of_scheldwoorden[j] == woorden[i]:
                aantal += 1
    return aantal

def read_file(file_name):

    path = os.getcwd() + file_name
    with open(path, "r") as my_file:
        return [line.rstrip('\n') for line in my_file]


def generate_scores(dict_cvs):
    for review in dict_cvs:
        optimisationfunc(dict_cvs[review])

dicti = utils.get_dict()
generate_scores(dicti)

with open("reviews_scores.txt", "w",encoding="utf8") as my_file:

    for review in dicti.values():
        print(review)
        my_file.write(f"Review: {review['review']}\nScore: {review['score']}\nDuimpjes: {review['thumbs_up']}\n\n")


