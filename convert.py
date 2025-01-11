import os
import cv2
from moviepy.editor import VideoClip, concatenate_videoclips, VideoFileClip, AudioFileClip, CompositeVideoClip

def images_to_video(image_folder, output_video, transition="crossfadein"):
    available_transitions = {
        "crossfadein": lambda clip, start_time: clip.set_start(start_time).crossfadein(0.5),
        "fadein": lambda clip, start_time: clip.set_start(start_time).fadein(0.5),
        # Add more transitions as needed
    }
    
    image_files = sorted([img for img in os.listdir(image_folder) if img.endswith(".jpg") or img.endswith(".png")])
    clips = []
    transition_func = available_transitions.get(transition, available_transitions["crossfadein"])  # Default to crossfadein if invalid option provided
    for idx, image_file in enumerate(image_files):
        image_path = os.path.join(image_folder, image_file)
        img_clip = VideoClip(make_frame=lambda t, img=cv2.imread(image_path): img, duration=2)
        if idx > 0:
            img_clip = transition_func(img_clip, idx * 2)
        clips.append(img_clip)
    final_clip = concatenate_videoclips(clips, method="compose")
    final_clip.write_videofile(output_video, fps=24)  # Adjust fps as needed

def add_audio_to_video(video_file, audio_file, output_video):
    video = VideoFileClip(video_file)
    audio = AudioFileClip(audio_file)
    
    # Ensure audio duration matches video duration
    if audio.duration < video.duration:
        audio = audio.set_duration(video.duration)
    elif audio.duration > video.duration:
        audio = audio.subclip(0, video.duration)
        
    final_clip = video.set_audio(audio)
    final_clip.write_videofile(output_video, codec='libx264', audio_codec='aac', temp_audiofile='temp-audio.m4a', remove_temp=True)


from flask import Flask, request

app = Flask(__name__)

@app.route('/generate_video', methods=['POST'])
def generate_video():
    
    image_folder = "images"
    output_video = './static/images/output_video.mp4'
    # audio_file = "audio1.mp3"

    selected_transition = request.form['transition']
    images_to_video(image_folder, output_video, transition=selected_transition)
    # add_audio_to_video(output_video, audio_file, output_video)

    
    return "Video generation started with transition: {}".format(selected_transition)

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app in debug mode





if __name__ == "__main__":
    image_folder = "images"
    output_video = './static/images/output_video.mp4'
    # audio_file = "audio1.mp3"

    selected_transition = input("Enter transition type (crossfadein, fadein, etc.): ")
    images_to_video(image_folder, output_video, transition=selected_transition)
    # add_audio_to_video(output_video, audio_file, output_video)


selected_transition = "a"
selected_duration = 1
selected_resolution = (1920, 1080)

@app.route('/duration_ha', methods=['POST'])
def duration_ha():
    selected_duration = request.form['duration']
    return "Video generation started with duration: {}".format(selected_duration)

@app.route('/transition_ha', methods=['POST'])
def transition_ha():
    selected_duration= request.form['transition']
    return "Video generation started with transition: {}".format(selected_transition)

@app.route('/generate_video', methods=['POST'])
def generate_video():
    
    image_folder = "images"
    output_video = 'static/images/output_video.mp4'
    # audio_file = "audio1.mp3"

    selected_resolution = request.form['videoresol']


    images_to_video(image_folder, output_video, selected_resolution, selected_duration, selected_transition)
    # add_audio_to_video(output_video, audio_file, output_video)

    
    return "Video generated started with resolution: {}".format(selected_resolution)

