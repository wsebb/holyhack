import utils
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import pandas as pd
import time


def generate_cvs_cluster(data, amount_of_clusters):
    start_time = time.time()

    # create a list of all the reviews
    reviews = [review['review'] for review in data.values()]

    nltk.download('stopwords')
    # create the TF-IDF vectorizer
    vectorizer = TfidfVectorizer(stop_words=stopwords.words('english'))

    # fit the vectorizer on the reviews
    vectors = vectorizer.fit_transform(reviews)

    # get the feature names
    features = vectorizer.get_feature_names_out()


    # create the KMeans model
    model = KMeans(n_clusters=amount_of_clusters, init='k-means++', max_iter=100, n_init=1)

    # fit the model on the vectors
    model.fit(vectors)

    # get the cluster assignments
    labels = model.labels_

    # create a new dataframe that includes the cluster assignments
    df = pd.DataFrame({'cluster': labels, 'review': reviews})

    # Make a text file for each cluster named cluster_1.txt, cluster_2.txt, etc. Each file should first contain the cluster number, the amount of reviews and then the reviews in that cluster.
    for i in range(amount_of_clusters):
        with open(f"cvs_clusters/cluster_{i}_{len(df[df['cluster'] == i])}.txt", "w") as my_file:
            my_file.write(f"Cluster: {i}\n")
            my_file.write(f"Amount of reviews: {len(df[df['cluster'] == i])}\n\n")
            for review in df[df['cluster'] == i]['review']:
                my_file.write(f"{review}\n\n")
                print(f"Score: {data[review]}\n\n")
                my_file.write(f"Score: {data[review]['score']}\n\n")

    # end the timer
    print(f"--- %s seconds ---" % (time.time() - start_time))
    # print some stats about the clusters
    print(f"Amount of clusters: {amount_of_clusters}")
    print(f"Amount of reviews: {len(df)}")
    print(f"Average amount of reviews per cluster: {len(df) / amount_of_clusters}")


def generate_json_cluster(amount_of_clusters):
    start_time = time.time()

    data = utils.get_dict_json()
    # create a list of all the reviews
    reviews = [review['opinion'] for review in data.values()]

    nltk.download('stopwords')
    # create the TF-IDF vectorizer
    vectorizer = TfidfVectorizer(stop_words=stopwords.words('dutch'))

    # fit the vectorizer on the reviews
    vectors = vectorizer.fit_transform(reviews)

    # get the feature names
    features = vectorizer.get_feature_names_out()

    # create the KMeans model
    model = KMeans(n_clusters=amount_of_clusters, init='k-means++', max_iter=100, n_init=1)

    # fit the model on the vectors
    model.fit(vectors)

    # get the cluster assignments
    labels = model.labels_

    # create a new dataframe that includes the cluster assignments
    df = pd.DataFrame({'cluster': labels, 'review': reviews})

    # Make a text file for each cluster named cluster_1.txt, cluster_2.txt, etc. Each file should first contain the cluster number, the amount of reviews and then the reviews in that cluster.
    for i in range(amount_of_clusters):
        with open(f"json_clusters/cluster_{i}_{len(df[df['cluster'] == i])}.txt", "w") as my_file:
            my_file.write(f"Cluster: {i}\n")
            my_file.write(f"Amount of reviews: {len(df[df['cluster'] == i])}\n\n")
            for review in df[df['cluster'] == i]['review']:
                my_file.write(f"{review}\n\n")
    # end the timer
    print(f"--- %s seconds ---" % (time.time() - start_time))
    # print some stats about the clusters
    print(f"Amount of clusters: {amount_of_clusters}")
    print(f"Amount of reviews: {len(df)}")
    print(f"Average amount of reviews per cluster: {len(df) / amount_of_clusters}")


if __name__ == '__main__':
    # generate_cvs_cluster()
    generate_json_cluster(100)

