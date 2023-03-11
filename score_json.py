import utils
import os
import numpy as np
import csv


def optimisation_func(review):
    review_text = get_review_text(review)

    # criteria
    premium = get_premium(review_text)
    trial = get_trial(review_text)
    subscription = get_subscription(review_text)
    word_count = get_word_count(review_text)
    swear_count = get_swear_count(review_text)

    # weights
    value = 1 * np.log(1 + word_count) - 1 * np.log(1 + swear_count)  # logarithmic scale
    if premium or trial or subscription:
        value += 1.5
    review["rating"] = round(value, 2)


def get_review_text(dict_reviews):
    return dict_reviews['opinion']


def get_premium(review_text):
    words = review_text.split()
    list_of_premium = read_file("/spelling/premium.txt")

    for i in range(len(words)):
        for j in range(len(list_of_premium)):
            if list_of_premium[j] == words[i]:
                return True
    return False


def get_trial(review_text):
    words = review_text.split()
    list_of_trial = read_file('/spelling/trial.txt')
    for i in range(len(words)):
        for j in range(len(list_of_trial)):
            if list_of_trial[j] == words[i]:
                return True
    return False


def get_subscription(review_text):
    words = review_text.split()
    list_of_subscription = read_file('/spelling/subscription.txt')
    for i in range(len(words)):
        for j in range(len(list_of_subscription)):
            if list_of_subscription[j] == words[i]:
                return True
    return False


def get_word_count(review_text):
    words = review_text.split()
    return len(words)


def get_swear_count(review_text):
    words = review_text.split()
    swear_list = read_file('/spelling/badwords.txt')
    count = 0
    for i in range(len(words)):
        for j in range(len(swear_list)):
            if swear_list[j] == words[i]:
                count += 1
    return count


def read_file(file_name):
    path = os.getcwd() + file_name
    with open(path, "r") as my_file:
        return [line.rstrip('\n') for line in my_file]


def generate_scores_json(dict_cvs):
    for review in dict_cvs:
        optimisation_func(dict_cvs[review])
