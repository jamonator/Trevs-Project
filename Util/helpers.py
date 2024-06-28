import os
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips, ImageClip, CompositeVideoClip, vfx
from pytube import YouTube
import librosa
from PyQt5.QtCore import QThread, pyqtSignal

class YouTubeDownloadThread(QThread):
    download_progress = pyqtSignal(int)
    download_complete = pyqtSignal(str)

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        try:
            yt = YouTube(self.url)
            ys = yt.streams.filter(only_audio=True).first()
            output_file = ys.download()
            base, ext = os.path.splitext(output_file)
            new_file = base + '.mp3'
            os.rename(output_file, new_file)
            self.download_complete.emit(new_file)
        except Exception as e:
            print(f"Error downloading audio: {e}")

class CompilationThread(QThread):
    progress = pyqtSignal(int)
    finished = pyqtSignal(str)

    def __init__(self, media_paths, audio_path, filter_name, overlay_name):
        super().__init__()
        self.media_paths = media_paths
        self.audio_path = audio_path
        self.filter_name = filter_name
        self.overlay_name = overlay_name

    def apply_filter(self, clip):
        if self.filter_name == "Grayscale":
            return clip.fx(vfx.blackwhite)
        elif self.filter_name == "Sepia":
            return clip.fx(vfx.colorx, 0.3)
        elif self.filter_name == "Invert":
            return clip.fx(vfx.invert_colors)
        return clip

    def apply_overlay(self, clip):
        overlay_path = ""
        if self.overlay_name == "Camcorder 1":
            overlay_path = "images/camcorder1.png"  # Ensure this path is correct
        elif self.overlay_name == "Camcorder 2":
            overlay_path = "images/camcorder2.png"  # Ensure this path is correct

        if overlay_path:
            overlay = ImageClip(overlay_path).set_duration(clip.duration).resize(height=clip.h).set_pos("center")
            return CompositeVideoClip([clip, overlay])
        return clip

    def run(self):
        try:
            total_steps = len(self.media_paths) * 2 + 2  # Load, filter/overlay for each clip, concatenate, write
            current_step = 0

            # Load audio and detect beats
            y, sr = librosa.load(self.audio_path)
            tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
            beat_times = librosa.frames_to_time(beat_frames, sr=sr)

            if not beat_times.any():
                raise ValueError("No beats detected in the audio file.")

            clips = []
            for media_path in self.media_paths:
                try:
                    if media_path.lower().endswith(('.jpg', '.jpeg', '.png')):
                        clip = ImageClip(media_path).set_duration(2)  # Assuming each image to be shown for 2 seconds
                    else:
                        clip = VideoFileClip(media_path)

                    current_step += 1
                    self.progress.emit(int((current_step / total_steps) * 100))

                    # Apply filter
                    clip = self.apply_filter(clip)

                    # Apply overlay
                    clip = self.apply_overlay(clip)

                    clips.append(clip)
                except Exception as e:
                    print(f"Error loading media file {media_path}: {e}")
                    continue

            if not clips:
                raise ValueError("No valid media clips loaded.")

            # Concatenate clips according to beat times
            final_clips = []
            for i, start_time in enumerate(beat_times[:-1]):
                end_time = beat_times[i + 1]
                duration = end_time - start_time
                clip_index = i % len(clips)
                clip = clips[clip_index]

                # Ensure the duration doesn't exceed the clip's duration
                if duration > clip.duration:
                    duration = clip.duration

                try:
                    subclip = clip.subclip(0, duration).set_start(start_time)
                    final_clips.append(subclip)
                except Exception as e:
                    print(f"Error creating subclip: {e}")
                    continue

            if not final_clips:
                raise ValueError("No valid final clips created.")

            final_clip = concatenate_videoclips(final_clips)

            # Add audio
            audio = AudioFileClip(self.audio_path)
            final_clip = final_clip.set_audio(audio).set_duration(audio.duration)
            current_step += 1
            self.progress.emit(int((current_step / total_steps) * 100))

            # Write final video
            output_path = "output_video.mp4"
            final_clip.write_videofile(output_path, codec="libx264", audio_codec="aac", fps=24, preset='ultafast')
            current_step += 1
            self.progress.emit(int((current_step / total_steps) * 100))

            self.finished.emit(output_path)
        except Exception as e:
            print(f"Error in compilation: {e}")