import os

from nltk.corpus import stopwords
import pandas as pd
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

nltk.download('stopwords')


def generate_csv_cluster(data, amount_of_clusters):
    # create a list of all the reviews
    reviews = [f"{review['review']} &{review['rating']} &{review['score']} &{review['thumbs_up']}" for review in
               data.values()]

    # create the TF-IDF vectorizer. Only use words that are longer than 2 characters and don't contain numbers.
    vectorizer = TfidfVectorizer(stop_words=stopwords.words('english'), token_pattern=r"(?u)\b[^&^\d\W][^&^\d\W]+\b")

    # fit the vectorizer on the reviews and also save the scores
    vectors = vectorizer.fit_transform(reviews)

    # create the KMeans model
    model = KMeans(n_clusters=amount_of_clusters, init='k-means++', n_init=1)

    # fit the model on the vectors
    model.fit(vectors)

    # get the cluster assignments
    labels = model.labels_

    # create a new dataframe that includes the cluster assignments
    df = pd.DataFrame(
        {'cluster': labels, 'review': reviews, 'score': [float(review.rsplit("&", 3)[2].strip()) for review in reviews],
         'rating': [float(review.rsplit("&", 3)[1].strip()) for review in reviews]})

    if not os.path.exists('csv_clusters'):
        os.makedirs('csv_clusters')
    else:
        for file in os.listdir('csv_clusters'):
            os.remove(os.path.join('csv_clusters', file))
    # Make a text file per cluster containing all the reviews and some data at the top
    for i in range(amount_of_clusters):
        # Extract the data from the dataframe by first identifying the cluster
        cluster_df = df[df['cluster'] == i]
        num_reviews = len(cluster_df)
        avg_rating = round(cluster_df['rating'].astype(float).mean(), 2)
        summed_score = round(cluster_df['score'].sum(), 2)

        # write this to a txt file
        with open(f"csv_clusters/cluster_{summed_score}_{avg_rating}_avg_{num_reviews}_sum_{i}.txt", "w") as my_file:
            my_file.write(f"Cluster: {i}\n")
            my_file.write(f"Amount of reviews: {num_reviews}\n")
            my_file.write(f"Average rating: {avg_rating}\n")
            my_file.write(f"Summed score: {summed_score}\n\n")

            # create a list of tuples where each tuple contains the review text, rating, score, and likes as a string
            reviews = [
                (review.rsplit("&", 3)[0], review.rsplit("&", 3)[1].strip(), float(review.rsplit("&", 3)[2].strip()),
                 review.rsplit("&", 1)[1].strip() if '&' in review else 'Error')
                for review in cluster_df['review']]

            # sort the list of tuples based on the score in descending order
            reviews.sort(key=lambda x: x[2], reverse=True)

            # loop through all the reviews in the sorted list of tuples and write them to the file
            for review in reviews:
                # write the review, rating, score, and likes to the file
                my_file.write(f"{review[0]}\n")
                my_file.write(f"Rating: {review[1]}\n")
                my_file.write(f"Score: {review[2]}\n")
                my_file.write(f"Likes: {review[3]}\n\n")


def generate_json_cluster(data, amount_of_clusters):
    # create a list of all the reviews
    reviews = [f"{review['opinion']} &{review['score']} &{review['rating']}" for review in
               data.values()]

    # create the TF-IDF vectorizer. Only use words that are longer than 2 characters and don't contain numbers.
    vectorizer = TfidfVectorizer(stop_words=stopwords.words('dutch'), token_pattern=r"(?u)\b[^&^\d\W][^&^\d\W]+\b")

    # fit the vectorizer on the reviews and also save the scores
    vectors = vectorizer.fit_transform(reviews)

    # create the KMeans model
    model = KMeans(n_clusters=amount_of_clusters, init='k-means++', n_init=1)

    # fit the model on the vectors
    model.fit(vectors)

    # get the cluster assignments
    labels = model.labels_

    # create a new dataframe that includes the cluster assignments
    df = pd.DataFrame(
        {'cluster': labels, 'review': reviews, 'score': [float(review.rsplit("&", 2)[1].strip()) for review in reviews],
         'rating': [float(review.rsplit("&", 2)[2].strip()) for review in reviews]})

    if not os.path.exists('json_clusters'):
        os.makedirs('json_clusters')
    else:
        for file in os.listdir('json_clusters'):
            os.remove(os.path.join('json_clusters', file))
    # Make a text file per cluster containing all the reviews and some data at the top
    for i in range(amount_of_clusters):
        # Extract the data from the dataframe by first identifying the cluster
        cluster_df = df[df['cluster'] == i]
        num_reviews = len(cluster_df)
        avg_rating = round(cluster_df['score'].astype(float).mean(), 2)
        summed_score = round(cluster_df['rating'].sum(), 2)

        # write this to a txt file
        with open(f"json_clusters/cluster_{summed_score}_{avg_rating}_avg_{num_reviews}_sum_{i}.txt", "w") as my_file:
            my_file.write(f"Cluster: {i}\n")
            my_file.write(f"Amount of reviews: {num_reviews}\n")
            my_file.write(f"Average rating: {avg_rating}\n")
            my_file.write(f"Summed score: {summed_score}\n\n")

            # create a list of tuples where each tuple contains the review text, rating, and score as a string
            reviews = [
                (review.rsplit("&", 2)[0], review.rsplit("&", 2)[2].strip(), float(review.rsplit("&", 2)[1].strip()))
                for review in cluster_df['review']]

            # sort the list of tuples based on the score
            reviews.sort(key=lambda x: x[2], reverse=True)

            # loop through all the reviews in the sorted list of tuples and write them to the file
            for review in reviews:
                # write the review, rating, and score to the file
                my_file.write(f"{review[0]}\n")
                my_file.write(f"Rating: {review[2]}\n")
                my_file.write(f"Score: {review[1]}\n\n")
