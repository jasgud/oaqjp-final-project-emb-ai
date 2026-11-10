
import requests
import json

def emotion_detector(text_to_analyze):
    # Define the URL for the emotion analysis API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)

    if response.status_code == 400:
        result = {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None
        }
        return result

    data = json.loads(response.text)
    emotions = data["emotionPredictions"][0]["emotion"]
    result = {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "dominant_emotion": max(emotions, key=emotions.get)
    }

    return result
    