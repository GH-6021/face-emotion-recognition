import os
data_classes={'Anger': 0, 'Disgust': 1, 'Fear': 2, 'Happiness': 3, 'Neutral': 4, 'Sadness': 5, 'Surprise': 6}

picture_dir = r'C:\baekjoon_Git_repository\face-emotion-recognition\src\occidental_picture\fear'
emotion = 'Fear'


for filename in os.listdir(picture_dir):
    if filename.endswith(".jpg"):

        if "_" in filename:
            print(f"{filename} 건너뜀 (이미 변경된 파일)")
            continue

        old_path = os.path.join(picture_dir, filename)
        new_fname = f"{filename.split('.')[0]}_{emotion}_.jpg"
        new_path = os.path.join(picture_dir, new_fname)

        os.rename(old_path, new_path)
        print(f"{filename} → {new_fname} 변경 완료")
