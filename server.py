from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name)

@app.route('/emotionDetector', methods=['POST'])
def emotion_analyzer():
    """
    Analyze the emotion in the provided text.

    Returns:
    JSON object containing emotion scores and dominant emotion.
    """
    if request.method == 'POST':
        text_to_analyze = request.form.get("textToAnalyze")  # Read the 'textToAnalyze' from form data
    else:
        return "Unsupported method", 405

    result = emotion_detector(text_to_analyze)

    # Extracting the dominant emotion and its score
    dominant_emotion = result['dominant_emotion']
    dominant_score = result[dominant_emotion]

    return jsonify({
        'anger': result['anger'],
        'disgust': result['disgust'],
        'fear': result['fear'],
        'joy': result['joy'],
        'sadness': result['sadness'],
        'dominant_emotion': dominant_emotion,
        'dominant_score': dominant_score
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)
