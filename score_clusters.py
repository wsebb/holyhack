import random

import cluster_generator
import utils


def generate_scores_cluster():
    dict_cvs = utils.get_dict()
    for review in dict_cvs.values():
        # generate a random integer between 0 and 100
        review['score'] = random.randint(0, 100)
    cluster_generator.generate_cvs_cluster(dict_cvs, 1000)


if __name__ == '__main__':
    generate_scores_cluster()
