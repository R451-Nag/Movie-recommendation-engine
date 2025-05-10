import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

data = pd.DataFrame({
    'title': ['The Matrix', 'Inception', 'Interstellar', 'The Dark Knight'],
    'description': [
        'sci-fi action dystopia',
        'dream heist thriller sci-fi',
        'space travel love sci-fi',
        'batman superhero thriller'
    ]
})

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(data['description'])

def recommend(movie_title):
    if movie_title not in data['title'].values:
        raise ValueError("Movie not found in dataset.")
    idx = data[data['title'] == movie_title].index[0]
    cosine_sim = cosine_similarity(tfidf_matrix[idx], tfidf_matrix).flatten()
    scores = list(enumerate(cosine_sim))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    recommended = [data['title'][i[0]] for i in scores[1:4]]
    return recommended
