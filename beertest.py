import flask
import random

# Initialize the app
app = flask.Flask(__name__)

#---------------------Python function----------------------------#

def getrecs(beer):

    #hard-coded fake recs - to be replaced
    recs= [
            "brouwerij st. bernardus nv - st. bernardus witbier", 
            "avery brewing company - liliko'i kepolo",
            "fort george brewery + public house - quick wit",
            "catawba brewing co. - white zombie ale",
            "bierbrouwerij de koningshoeven b.v. - la trappe witte trappist",
            "einstök ölgerð (einstök beer company) - icelandic white ale",
            "harvest moon brewery - beltian white",
            "russian river brewing company - little white lie",
            "anheuser-busch - shock top belgian white",
            "full pint brewing company - white lightning"
        ]

    # EXAMPLE JSON - PREFERRED FOR STATIC DATA
    #
    # recs= [
    #     {
    #         brewery: "brouwerij st. bernardus nv",
    #         beer_name: "st. bernardus witbier",
    #         feature_img: "http://example.com/assets/img_123.jpg",
    #         alc_percent: 5.8
    #     }, 
    #     {
    #         brewery: "avery brewing company",
    #         beer_name: "liliko'i kepolo",
    #         feature_img: "http://example.com/assets/img_123.jpg",
    #         alc_percent: 5.8
    #     },
    #     {
    #         brewery: "fort george brewery + public house",
    #         beer_name: "quick wit",
    #         feature_img: "http://example.com/assets/img_123.jpg",
    #         alc_percent: 5.8
    #     },
    #     {
    #         brewery: "catawba brewing co.",
    #         beer_name: "white zombie ale",
    #         feature_img: "http://example.com/assets/img_123.jpg",
    #         alc_percent: 5.8
    #     },
    #     {
    #         brewery: "bierbrouwerij de koningshoeven b.v.",
    #         beer_name: "la trappe witte trappist",
    #         feature_img: "http://example.com/assets/img_123.jpg",
    #         alc_percent: 5.8
    #     },
    #     {
    #         brewery: "einstök ölgerð (einstök beer company)",
    #         beer_name: "icelandic white ale",
    #         feature_img: "http://example.com/assets/img_123.jpg",
    #         alc_percent: 5.8
    #     },
    #     {
    #         brewery: "harvest moon brewery",
    #         beer_name: "beltian white",
    #         feature_img: "http://example.com/assets/img_123.jpg",
    #         alc_percent: 5.8
    #     },
    #     {
    #         brewery: "russian river brewing company",
    #         beer_name: "little white lie",
    #         feature_img: "http://example.com/assets/img_123.jpg",
    #         alc_percent: 5.8
    #     },
    #     {
    #         brewery: "anheuser-busch",
    #         beer_name: "shock top belgian white",
    #         feature_img: "http://example.com/assets/img_123.jpg",
    #         alc_percent: 5.8
    #     },
    #     {
    #         brewery: "full pint brewing company",
    #         beer_name: "white lightning",
    #         feature_img: "http://example.com/assets/img_123.jpg",
    #         alc_percent: 5.8
    #     }
    # ]

    return recs

#loads the page
@app.route("/")
def viz_page():
    with open("index.html", 'r') as viz_file:
        return viz_file.read()
    
#listens
@app.route("/gof", methods=["POST"])
def score():
    """
    When A POST request with json data is made to this url,
    Read the grid from the json, update and send it back
    """
    #html "posts" a request and python gets the json  from that request 
    data = flask.request.json
    userbeer = data['grid'][0] #get the user input beer, do something with it in the model
    result = getrecs(userbeer) #get list of recs from previously defined function
    return flask.jsonify({'words': result})







#--------- RUN WEB APP SERVER ------------#

# Start the app server on port 80
# (The default website port)
app.run(host='0.0.0.0', port=8004)