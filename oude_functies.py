import utils
import operator

d = utils.get_dict()


def get_replies():
    with open("spelling/replies.txt", "w") as my_file:
        for review in d.values():
            if review['reply']:
                reply = f"Review: {review['review']}\nReply: {review['reply']}\n\n"
                my_file.write(reply)


def get_word_count():
    word_counts = dict()

    for review in d.values():
        for word in [x.lower() for x in review['review'].split()]:
            try:
                word_counts[word] += 1
            except KeyError:
                word_counts[word] = 1

    # write the word counts to a file in descending order
    with open("word_counts.txt", "w") as my_file:
        for word, count in sorted(word_counts.items(), key=operator.itemgetter(1), reverse=True):
            my_file.write(f"{word}: {count}\n")
