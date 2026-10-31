"""Detect emotions in English text using IBM Watson NLP."""

import requests

SERVICE_URL = (
    "https://sn-watson-emotion.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
MODEL_HEADERS = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
}
EMOTION_NAMES = ("anger", "disgust", "fear", "joy", "sadness")


def emotion_detector(text_to_analyze):
    """Return emotion scores and the dominant emotion for a sentence.

    For invalid input or a Watson HTTP 400 response, all fields are None.
    Unexpected service errors are raised rather than reported as success.
    """
    if not isinstance(text_to_analyze, str) or not text_to_analyze.strip():
        return {**dict.fromkeys(EMOTION_NAMES), "dominant_emotion": None}

    response = requests.post(
        SERVICE_URL,
        headers=MODEL_HEADERS,
        json={"raw_document": {"text": text_to_analyze}},
        timeout=30,
    )

    if response.status_code == 400:
        return {**dict.fromkeys(EMOTION_NAMES), "dominant_emotion": None}

    response.raise_for_status()
    emotions = response.json()["emotionPredictions"][0]["emotion"]
    scores = {name: emotions[name] for name in EMOTION_NAMES}
    scores["dominant_emotion"] = max(
        EMOTION_NAMES,
        key=lambda emotion: scores[emotion],
    )
    return scores
