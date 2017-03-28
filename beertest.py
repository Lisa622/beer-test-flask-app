import flask
import random

# Initialize the app
app = flask.Flask(__name__)

#---------------------Python function----------------------------#

def getrecs(beer):

    #hard-coded fake recs
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

    # recs should be replaced with actual beer recommendation function

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