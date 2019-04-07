from image_emotion_gender_demo import getFaceEmotion

def main_func():
    image_path = 'snap.jpg'
    mood = getFaceEmotion(image_path)
    return mood
