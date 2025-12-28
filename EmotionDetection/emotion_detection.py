import requests
import json

def emotion_detector(text_to_analyze):
    # Define the URL for the emotion predict API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create the payload with the text to be analyzed
    input_json = { "raw_document": { "text": text_to_analyze } }

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=input_json, headers=header)

    formatted_response = json.loads(response.text)
    dominant_emotion_score = None
    dominant_emotion = None

    if response.status_code == 400:
        formatted_response = {'emotionPredictions': [{'emotion': {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None}}]}
        emotionPredictions = formatted_response["emotionPredictions"][0]["emotion"]
    else:        
        emotionPredictions = formatted_response["emotionPredictions"][0]["emotion"]
        
        # Get the dominant emotion score
        dominant_emotion_score = max(emotionPredictions.values())

    # match the dominant emotion score with the corresponding emotion    
    for emotion_key in emotionPredictions.keys():
        if dominant_emotion_score is not None and emotionPredictions[emotion_key] == dominant_emotion_score:
            dominant_emotion = emotion_key
            break

    # add the dominant emotion in the response
    emotionPredictions['dominant_emotion'] = dominant_emotion

    return emotionPredictions
