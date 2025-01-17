import os

picture_dir = r'C:\Users\rkgus\OneDrive\바탕 화면\emotion code\face_emotion_recognition\face-emotion-recognition\src\random_picture'

gender_mapping = {'남': 'm', '여': 'w'}
emotion_mapping = {
    '기쁨': 'Happiness', 
    '중립': 'Neutral', 
    '상처': 'Disgust', 
    '슬픔': 'Sadness', 
    '불안': 'Fear', 
    '분노': 'Anger', 
    '당황': 'Surprise'
}

for filename in os.listdir(picture_dir):
    if filename.endswith(".jpg"):
        parts = filename.split('_')
        
        if len(parts) >= 5:
            publisher_id = parts[0]
            gender = parts[1]
            age = parts[2]
            emotion = parts[3]
            upload_number = parts[5].replace(".jpg", "")

            gender = gender_mapping.get(gender, gender)
            emotion = emotion_mapping.get(emotion, emotion)
            
            new_filename = f"{publisher_id}_{gender}_{age}_{emotion}_{upload_number}.jpg"
            
            old_file_path = os.path.join(picture_dir, filename)
            new_file_path = os.path.join(picture_dir, new_filename)
            
            os.rename(old_file_path, new_file_path)
            print(f"Renamed: {filename} -> {new_filename}")
