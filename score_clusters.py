import time

import cluster_generator
import utils
import optimalisationfunc1 as op
import optimalisationfuncJson as opj


def generate_scores_cluster_csv():
    # Runt in ongeveer 0 + 50 + 60 = 110 seconden
    start_time = time.time()
    print("Generating datastruct for cvs...")
    dict_cvs = utils.get_dict()
    print(f"--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    print("Generating scores for reviews...")
    op.generate_scores(dict_cvs)
    print(f"--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    print("Generating clusters...")
    cluster_generator.generate_cvs_cluster(dict_cvs, 1000)
    print(f"--- %s seconds ---" % (time.time() - start_time))
    print("Done!")

def generate_scores_cluster_json():
    # Runt in ongeveer 1.5 + 311 +  = seconden
    start_time = time.time()
    print("Generating datastruct for json...")
    dict_json = utils.get_dict_json()
    # dict_json = {k: dict_json[k] for k in list(dict_json)[:200000]}
    print(f"--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    print("Generating scores for reviews...")
    opj.generate_scores_json(dict_json)
    print(f"--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    print("Generating clusters...")
    cluster_generator.generate_json_cluster(dict_json, 2000)
    print(f"--- %s seconds ---" % (time.time() - start_time))
    print("Done!")


if __name__ == '__main__':
    # generate_scores_cluster_csv()
    generate_scores_cluster_json()
