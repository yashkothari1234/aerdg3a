from flask import Flask, jsonify, request

from storage import all_articles, liked_articles, not_liked_articles


app = Flask(__name__)

@app.route("/get-article")
def get_article():
    article_data = {
        "title": all_articles[0][14],
        "text" : all_articles[0][15],
        "eventType" : all_articles[0][4],
        "lang" : all_articles[0][16]
       
    }
    return jsonify({
        "data": article_data,
        "status": "success"
    })

@app.route("/liked-article", methods=["POST"])
def liked_article():
    articles = all_articles[0]
    liked_articles.append(movie)
    all_articles.pop(0)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/unliked-movie", methods=["POST"])
def unliked_article():
    articles = all_articles[0]
    not_liked_articles.append(articles)
    all_articles.pop(0)
    return jsonify({
        "status": "success"
    }), 201




    return jsonify({
        "data": article_data,
        "status": "success"
    }), 200

if __name__ == "__main__":
  app.run()