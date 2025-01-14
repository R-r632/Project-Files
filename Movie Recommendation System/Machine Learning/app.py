import pickle
from flask import Flask, request, jsonify
from flask_cors import CORS

# Load the pickled files
movie_data = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

app = Flask(__name__)
CORS(app)

@app.route('/recommend', methods=['GET'])
def recommend():
    # Get movie name from the request
    movie = request.args.get('movie', '')
    
    if not movie:
        return jsonify({'error': 'No movie name provided'}), 400
    
    # Check if the movie exists in the data
    if movie not in movie_data['title'].values:
        return jsonify({'error': 'Movie not found'}), 404

    # Get index of the movie
    index = movie_data[movie_data['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    
    # Get top 5 recommendations
    recommendations = [movie_data.iloc[i[0]].title for i in distances[1:6]]

    return jsonify({'recommendations': recommendations})

if __name__ == '__main__':
    app.run(debug=True)