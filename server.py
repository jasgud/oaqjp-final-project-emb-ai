# Import Flask, render_template, request from the flask
from flask import Flask, render_template, request

# Import the emotion_detection function from the package created
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detector")

#Make endpoint for emotionDetector
@app.route("/emotionDetector")
def emotionDetector():
    """
    Retrieve the text to detect from the request arguments
    """
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    return response

#Make endpoint for root
@app.route("/")
def render_index_page():
    """
    Render page
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
