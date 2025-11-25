import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }

    resp = requests.post(url, json=input_json, headers=headers)
    f_resp = json.loads(resp.text)

    anger_score = f_resp['emotionPredictions'][0]['emotion']['anger']
    disgust_score = f_resp['emotionPredictions'][0]['emotion']['disgust']
    fear_score = f_resp['emotionPredictions'][0]['emotion']['fear']
    joy_score = f_resp['emotionPredictions'][0]['emotion']['joy']
    sadness_score = f_resp['emotionPredictions'][0]['emotion']['sadness']
    dominant = 'joy'

    return {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, \
    'joy': joy_score, 'sadness': sadness_score, 'dominant_emotion': dominant}