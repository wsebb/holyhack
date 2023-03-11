import sys
import time

import cluster_generator
import utils
import score_csv as op
import score_json as opj


def generate_scores_cluster_csv(clusters):
    # Generates clusters for the json data file
    # Runs (avg) 0s + 50s + 60s = 110 seconds
    start_time = time.time()
    print("Generating datastruct for csv...")
    dict_csv = utils.get_dict()
    print(f"--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    print("Generating scores for reviews...")
    op.generate_scores(dict_csv)
    print(f"--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    print("Generating clusters...")
    cluster_generator.generate_csv_cluster(dict_csv, clusters)
    print(f"--- %s seconds ---" % (time.time() - start_time))
    print("Done!")


def generate_scores_cluster_json(clusters):
    # Generates clusters for the json data file
    # Runs (avg) 1s + 300s + 2500s = 2801 seconds
    start_time = time.time()
    print("Generating datastruct for json...")
    dict_json = utils.get_dict_json()
    print(f"--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    print("Generating scores for reviews...")
    opj.generate_scores_json(dict_json)
    print(f"--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    print("Generating clusters...")
    cluster_generator.generate_json_cluster(dict_json, clusters)
    print(f"--- %s seconds ---" % (time.time() - start_time))
    print("Done!")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        clusters = int(sys.argv[1])
    else:
        clusters = 1000
    generate_scores_cluster_csv(clusters)
    generate_scores_cluster_json(clusters)
