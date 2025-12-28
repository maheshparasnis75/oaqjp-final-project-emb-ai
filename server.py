"""
The server-side api functions, that
- display user interface for input entry
- initiate emotion detection analysis, upon user submit the form
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detect():
    """
    The api function that initiates emotion detection analysis.
    """

    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    out = "For the given statement, the system response is "
    dominant_emotion_key = "dominant_emotion"

    # error handling
    if response[dominant_emotion_key] is not None:
        dominant_emotion_value = ""
        for emotion_key in response.keys():
            if emotion_key == dominant_emotion_key:
                dominant_emotion_value = response[emotion_key]
            else:
                out = out + "'" + emotion_key + "': " + str(response[emotion_key]) + ", "

        #replace last comma with period
        out = out[:out.rfind(",")] + "."
        out = out + " The dominant emotion is " + "<b>" + dominant_emotion_value + "</b>" + "."
    else:
        out = "Invalid text! Please try again!"

    return out

@app.route("/")
def render_index_page():
    """
    The api function that displays default landing page, that is user entry form.
    """

    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
