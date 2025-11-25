''' Main server module for Emotion Detector final project '''

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    ''' render index page '''
    return render_template('index.html')

@app.route("/emotionDetector")
def detector():
    ''' process given text and return appropriate message '''
    text_to_analyze = request.args.get('textToAnalyze')
    resp = emotion_detector(text_to_analyze)

    if not resp['dominant_emotion']:
        return "Invalid text! Please try again!"

    return (f"For the given statement, the system response is "
           f"'anger': {resp['anger']}, "
           f"'disgust': {resp['disgust']}, "
           f"'fear': {resp['fear']}, "
           f"'joy': {resp['joy']} and "
           f"'sadness': {resp['sadness']}. "
           f"The dominant emotion is <b>{resp['dominant_emotion']}</b>.")

if __name__ == '__main__':
    app.run()
