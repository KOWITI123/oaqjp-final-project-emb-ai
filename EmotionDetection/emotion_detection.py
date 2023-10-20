import requests

def emotion_detector(text_to_analyse):
    url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json= { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json=input_json, headers=header )
    
    # Convert the response text into a dictionary
    formatted_response = response.json()

    # Extract set of emotions
    emotions = formatted_response["emotionPredictions"][0]["emotion"]

    # Find dominant emotion
    dominant_emotion = max(emotions, key = emotions.get)
    dominant_score = emotions[dominant_emotion]

    # Create a dictionary to store the output format
    result = {
        'anger': emotions.get('anger', 0.0),
        'disgust': emotions.get('disgust', 0.0),
        'fear': emotions.get('fear', 0.0),
        'joy': emotions.get('joy', 0.0),
        'sadness': emotions.get('sadness', 0.0),
        'dominant_emotion': dominant_emotion
    }

    return result

# Test
try:
    print(emotion_predictor("I love new technology."))
    print(emotion_predictor("")) # This should raise an error due to blank space
except Exception as e:
    print(f"Error: {e}")        


