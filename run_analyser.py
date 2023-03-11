import time

import cluster_generator
import utils
import score_csv as op
import score_json as opj


def generate_scores_cluster_csv():
    # Generates clusters for the json data file
    # Runs (avg) 0s + 50s + 60s = 110 seconds
    start_time = time.time()
    print("Generating datastruct for cvs...")
    dict_cvs = utils.get_dict()
    dict_cvs = {k: dict_cvs[k] for k in list(dict_cvs)[:2000]}
    print(f"--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    print("Generating scores for reviews...")
    op.generate_scores(dict_cvs)
    print(f"--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    print("Generating clusters...")
    cluster_generator.generate_cvs_cluster(dict_cvs, 10)
    print(f"--- %s seconds ---" % (time.time() - start_time))
    print("Done!")


def generate_scores_cluster_json():
    # Generates clusters for the json data file
    # Runs (avg) 1s + 300s + 2500s = 2801 seconds
    start_time = time.time()
    print("Generating datastruct for json...")
    dict_json = utils.get_dict_json()
    dict_json = {k: dict_json[k] for k in list(dict_json)[:2000]}
    print(f"--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    print("Generating scores for reviews...")
    opj.generate_scores_json(dict_json)
    print(f"--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    print("Generating clusters...")
    cluster_generator.generate_json_cluster(dict_json, 10)
    print(f"--- %s seconds ---" % (time.time() - start_time))
    print("Done!")


if __name__ == '__main__':
    generate_scores_cluster_csv()
    generate_scores_cluster_json()
