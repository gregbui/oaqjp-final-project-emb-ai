import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }

    resp = requests.post(url, json=input_json, headers=headers)
    f_resp = json.loads(resp.text)

    anger_score = float(f_resp['emotionPredictions'][0]['emotion']['anger'])
    dominant = 'anger'
    dominant_score = anger_score

    disgust_score = float(f_resp['emotionPredictions'][0]['emotion']['disgust'])
    if disgust_score > dominant_score:
        dominant = 'disgust'
        dominant_score = disgust_score

    fear_score = float(f_resp['emotionPredictions'][0]['emotion']['fear'])
    if fear_score > dominant_score:
        dominant = 'fear'
        dominant_score = fear_score

    joy_score = float(f_resp['emotionPredictions'][0]['emotion']['joy'])
    if joy_score > dominant_score:
        dominant = 'joy'
        dominant_score = joy_score

    sadness_score = float(f_resp['emotionPredictions'][0]['emotion']['sadness'])
    if sadness_score > dominant_score:
        dominant = 'sadness'

    return {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, \
            'joy': joy_score, 'sadness': sadness_score, 'dominant_emotion': dominant}