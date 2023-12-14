import torch
from TTS.api import TTS
# from VoiceToText import text
import os



os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "max_split_size_mb:30"
torch.cuda.empty_cache()

torch.set_default_device('cuda')

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to('cuda')

wav = tts.tts_to_file(text="Hello World this product made by reco team", speaker_wav="./ipda/temp/pbaudio.mp3", file_path="./ipda/temp/output.wav", language="en")