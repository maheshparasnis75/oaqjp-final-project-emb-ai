import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):

    def test_emotion_detector(self):
        statement1 = "I am glad this happened"
        result1 = emotion_detector(statement1)
        self.assertEqual(result1["dominant_emotion"], "joy")

        statement2 = "I am really mad about this"
        result2 = emotion_detector(statement2)
        self.assertEqual(result2["dominant_emotion"], "anger")

        statement3 = "I feel disgusted just hearing about this"
        result3 = emotion_detector(statement3)
        self.assertEqual(result3["dominant_emotion"], "disgust")

        statement4 = "I am so sad about this"
        result4 = emotion_detector(statement4)
        self.assertEqual(result4["dominant_emotion"], "sadness")

        statement5 = "I am really afraid that this will happen"
        result5 = emotion_detector(statement5)
        self.assertEqual(result5["dominant_emotion"], "fear")

unittest.main()()