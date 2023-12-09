from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
from flask import Flask,request,jsonify
import json
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    username="root",
    passwd="Pheonix@1234",
    database="datastore"
)

mycursor = mydb.cursor()

with open('CompanyAssignment/sentiment_model.json', 'r') as json_file:
    loaded_model_json = json_file.read()
    loaded_model = model_from_json(loaded_model_json)

# Load the model weights
loaded_model.load_weights('CompanyAssignment/sentiment_model_weights.h5')

# Load the tokenizer
with open('CompanyAssignment/tokenizer.pkl', 'rb') as tokenizer_file:
    tokenizer = pickle.load(tokenizer_file)

def predict_sentiment_label(text, threshold=0.5):
    # Tokenize and pad the input text
    sequence = tokenizer.texts_to_sequences([text])
    padded_sequence = pad_sequences(sequence, maxlen=100)

    # Make prediction
    prediction = loaded_model.predict(padded_sequence)[0][0]

    # Classify based on the threshold
    sentiment_label = 'positive' if prediction >= threshold else 'negative'

    return sentiment_label

app=Flask(__name__)

@app.route("/predict/<pred_data>")
def predictionOnS(pred_data):
    received  = str(pred_data)
    sentiment = predict_sentiment_label(received)
    pred_out = {
        "data": pred_data,
        "result":sentiment

    }

    return jsonify(pred_out) ,200

@app.route("/preddata",methods=["POST"])
def acceptData():
    data = request.get_json()
    if "data" not in data:
        return jsonify({"error": "Missing 'text' in the request data"}), 400
    text_to_predict = data["data"]
    sentiment = predict_sentiment_label(text_to_predict)

    sqlFormula = "INSERT INTO responses (text, sentiment) VALUES (%s, %s)"
    response1 = (text_to_predict , sentiment)

    mycursor.execute(str(sqlFormula),str(response1))

    mydb.commit()

    pred_out={
        "data" : text_to_predict,
        "sentiment" : sentiment

    }

    return jsonify(pred_out),201



if __name__ == "__main__":
    app.run(debug=True)