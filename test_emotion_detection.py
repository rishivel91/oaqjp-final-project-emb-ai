"""Tests for the five emotion labels using mocked Watson NLP responses."""

import unittest
from unittest.mock import Mock, patch

from EmotionDetection.emotion_detection import emotion_detector


def mock_response(dominant):
    """Return a Watson-style response with the requested top emotion."""
    emotions = {
        "anger": 0.05,
        "disgust": 0.05,
        "fear": 0.05,
        "joy": 0.05,
        "sadness": 0.05,
    }
    emotions[dominant] = 0.8
    response = Mock(status_code=200)
    response.json.return_value = {
        "emotionPredictions": [{"emotion": emotions}]
    }
    return response


class TestEmotionDetection(unittest.TestCase):
    """Verify response formatting for the five required emotions."""

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_joy(self, post):
        """Joy example returns joy."""
        post.return_value = mock_response("joy")
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result["dominant_emotion"], "joy")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_anger(self, post):
        """Anger example returns anger."""
        post.return_value = mock_response("anger")
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result["dominant_emotion"], "anger")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_disgust(self, post):
        """Disgust example returns disgust."""
        post.return_value = mock_response("disgust")
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result["dominant_emotion"], "disgust")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_sadness(self, post):
        """Sadness example returns sadness."""
        post.return_value = mock_response("sadness")
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result["dominant_emotion"], "sadness")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_fear(self, post):
        """Fear example returns fear."""
        post.return_value = mock_response("fear")
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result["dominant_emotion"], "fear")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_blank_input(self, post):
        """Blank text is not sent to Watson."""
        result = emotion_detector("   ")
        self.assertIsNone(result["dominant_emotion"])
        post.assert_not_called()

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_http_400(self, post):
        """Watson 400 returns empty emotion fields."""
        post.return_value = Mock(status_code=400)
        result = emotion_detector("invalid")
        self.assertTrue(all(value is None for value in result.values()))


if __name__ == "__main__":
    unittest.main()
