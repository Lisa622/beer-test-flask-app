import flask
import pickle
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Initialize the app
app = flask.Flask(__name__)



#---------------------Python function----------------------------#
#open pickled file as df
dfbeers = pd.read_pickle('beer_nmf_df')

def recs(df,numrecs, weights):
    df['score'] = (weights['abv']*df['abv_tier'])+(df['rating']/5)*weights['rating']+\
    (df['same_style']*weights['samestyle']) + (weights['text']*df['distance'])
    sort_distances = df.sort_values(by='score', axis=0, ascending=False, inplace=False)
    num_recs = numrecs
    recs = sort_distances.iloc[:num_recs,:2]
    reclist = list(recs.itertuples())
    reclist2 = []
    for i in reclist:
        reclist2.append(i[2]+' - '+i[1])
    return reclist2

def getrecs(userbeer,df):
    userdocs = dfbeers[dfbeers['beer']=='shock top belgian white']
    not_userbeer = dfbeers.loc[dfbeers['beer'] != userbeer]
    bmatrix = not_userbeer.ix[:,7:].copy()
    usermatrix = userdocs.ix[:,7:].copy()
    distance = pd.DataFrame(cosine_similarity(bmatrix,usermatrix))
    #join distances back to original dataframe with all beers (beside test beer)
    not_userbeer.reset_index(inplace=True)
    distance.reset_index(inplace=True)
    beer_distances = not_userbeer.join(distance, how='left', lsuffix='_l')
    beer_distances = beer_distances.rename(columns ={beer_distances.columns[-1]:'distance'})
    beer_distances.drop(['index_l','index'], axis=1, inplace=True)
    beer_distances['same_style']= beer_distances['beerstyle'] == str(userdocs.beerstyle).split()[1]
    def inABVrange(df):
        return ((float(str(userdocs['abv']).split()[1]))-2.2 <= df['abv']) and ((float(str(userdocs['abv']).split()[1]))+2.2 >= df['abv'])
    beer_distances['abv_tier'] = beer_distances.apply(inABVrange, axis=1)

    weightsdict = {'abv':.15,'rating':.3,'samestyle':0,'text':.55}
    num_recs = 10
    closestbeers = recs(beer_distances,num_recs,weightsdict)
    return closestbeers

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
    result = getrecs(userbeer, dfbeers) #get list of recs from previously defined function
    return flask.jsonify({'words': result})







#--------- RUN WEB APP SERVER ------------#

# Start the app server on port 80
# (The default website port)
app.run(host='0.0.0.0', port=8004)