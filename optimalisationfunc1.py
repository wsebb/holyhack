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
    value = 1 * likes + 1* aantal_woorden - 1 * aantal_scheldwoorden
    if premium or trial or subscription:
        value += 1
    return value

def get_review_text(dict_reviews):
    return dict_reviews['review']

def get_premium(review_text):
    woorden = review_text.split()
    if 'premium' in woorden:



