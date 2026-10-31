"""Intermediate stage: format emotion predictions as a Python dictionary."""

import requests


def emotion_detector(text_to_analyze):
    """Call Watson and return five scores plus the dominant emotion."""
    response = requests.post(
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict",
        headers={
            "grpc-metadata-mm-model-id":
            "emotion_aggregated-workflow_lang_en_stock"
        },
        json={"raw_document": {"text": text_to_analyze}},
        timeout=30,
    )
    response.raise_for_status()
    emotion = response.json()["emotionPredictions"][0]["emotion"]
    result = {
        label: emotion[label]
        for label in ("anger", "disgust", "fear", "joy", "sadness")
    }
    result["dominant_emotion"] = max(result, key=result.get)
    return result
