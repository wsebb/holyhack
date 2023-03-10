import utils

dict_reviews = utils.get_dict()
print(dict_reviews)

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
    value = 1 * likes + 1 * aantal_woorden - 1 * aantal_scheldwoorden
    if premium or trial or subscription:
        value += 1
    return value

def get_review_text(dict_reviews):
    return dict_reviews['review']

def get_premium(review_text):
    woorden = review_text.split()
    list_of_premium = []
    for i in range(len(woorden)):
        for j in range(len(list_of_premium)):
            if list_of_premium[j] == woorden[i]:
                return True
    return False

def get_trial(review_text):
    woorden = review_text.split()
    list_of_trial = []
    for i in range(len(woorden)):
        for j in range(len(list_of_trial)):
            if list_of_trial[j] == woorden[i]:
                return True
    return False

def get_subscription(review_text):
    woorden = review_text.split()
    list_of_subscription = []
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
    list_of_scheldwoorden = []
    aantal = 0
    for i in range(len(woorden)):
        for j in range(len(list_of_scheldwoorden)):
            if list_of_scheldwoorden[j] == woorden[i]:
                aantal += 1
    return aantal
