from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector


app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/emotionDetector")
def emotionDetector():
    text_to_analyze = request.args.get('textToAnalyze')
    resp = emotion_detector(text_to_analyze)

    return "For the given statement, the system response is " \
           "'anger': {}, " \
           "'disgust': {}, " \
           "'fear': {}, " \
           "'joy': {} and " \
           "'sadness': {}. " \
           "The dominant emotion is <b>{}</b>.".format(
            resp['anger'], resp['disgust'], resp['fear'], resp['joy'], resp['sadness'], resp['dominant_emotion'])

if __name__ == '__main__':
    app.run()