"""Initial stage: return raw Watson NLP emotion analysis response."""

import requests


def emotion_detector(text_to_analyze):
    """Submit text to Watson and return the original response text."""
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
    return response.text
