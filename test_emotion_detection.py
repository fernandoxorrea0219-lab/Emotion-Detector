"""Unit tests for the emotion_detector function."""
import unittest

from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Validate the dominant emotion returned for each sample statement."""

    def test_emotion_detector(self):
        """Each statement must produce its expected dominant emotion."""
        cases = {
            "I am glad this happened": "joy",
            "I am really mad about this": "anger",
            "I feel disgusted just hearing about this": "disgust",
            "I am so sad about this": "sadness",
            "I am really afraid that this will happen": "fear",
        }
        for statement, expected in cases.items():
            with self.subTest(statement=statement):
                self.assertEqual(emotion_detector(statement)["dominant_emotion"], expected)


if __name__ == "__main__":
    unittest.main()
