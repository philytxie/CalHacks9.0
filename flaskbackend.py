# Load libraries
import flask
import pandas as pd
from sklearn.feature_extraction import DictVectorizer
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential, load_model

# instantiate flask
app = flask.Flask(__name__)
# we need to redefine our metric function in order 
# to use it when loading the model 
def auc(y_true, y_pred):
    auc = tf.metrics.auc(y_true, y_pred)[1]
    keras.backend.get_session().run(tf.local_variables_initializer())
    return auc

# load the model, and pass in the custom metric function
global graph
graph = tf.compat.v1.get_default_graph()

heart_model = keras.models.load_model("heart_attack_model.h5")
stroke_model = keras.models.load_model("stroke_model.h5")
kidney_disease_model = keras.models.load_model("kidney_disease_model.h5")
cancer_model = keras.models.load_model("cancer_model.h5")
diabetes_model = keras.models.load_model("diabetes_model.h5")
ang_or_chd_model = keras.models.load_model("ang_or_chd_model.h5")

# define a predict function as an endpoint 
@app.route("/predict", methods=["GET","POST"])
def predict():
    data = {"success": False}

    params = flask.request.json
    if (params == None):
        params = flask.request.args

    # if parameters are found, return a prediction
    if (params != None):
        vec = DictVectorizer()
        x = pd.DataFrame.from_dict(params, orient='index').to_dict('records')
        vector = vec.fit_transform(x).toarray()
        with graph.as_default():
            data["heart_attack"] = str(heart_model.predict(vector))
            data["stroke"] = str(stroke_model.predict(vector))
            data["kidney_disease"] = str(kidney_disease_model.predict(vector))
            data["cancer"] = str(cancer_model.predict(vector))
            data["ang_or_chd"] = str(ang_or_chd_model.predict(vector))
            data["success"] = True

    # return a response in json format 
    return flask.jsonify(data)    

# start the flask app, allow remote connections 
app.run(host='0.0.0.0')