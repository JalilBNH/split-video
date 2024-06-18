import cv2
import numpy as np
import datetime
import argparse
import os

video_path = "datasets/video_players_detection/video1.mp4"

video = cv2.VideoCapture(video_path)

seq_duration = 30 
fps = int(video.get(cv2.CAP_PROP_FPS))
nb_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
duration = int(nb_frames / fps) 
frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

def print_duration(duration):
    time = datetime.timedelta(seconds=duration)
    print(f'duration of the video  : {time}')


def compute_requirement(nb_frames, fps, seq_duration):
    frame_per_seq = int(fps * seq_duration)
    nb_of_seq = nb_frames // frame_per_seq + (nb_frames % frame_per_seq != 0)
    return frame_per_seq, nb_of_seq
    
def save_video(output_dir, nb_of_seq, frame_per_seq):
    for i in range(nb_of_seq):
        file_name = os.path.join(output_dir, str(i) + '.mp4')
        fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
        out = cv2.VideoWriter(file_name, fourcc, fps, (frame_width, frame_height))
        for j in range(frame_per_seq):
            ret, frame = video.read()
            if not ret:
                break
            out.write(frame)


if not video.isOpened():
    print("Error establishing connection")
print("This is good !")

frame_per_seq, nb_of_seq = compute_requirement(nb_frames, fps, seq_duration)
save_video("datasets/video_players_detection", nb_of_seq, frame_per_seq)

video.release()