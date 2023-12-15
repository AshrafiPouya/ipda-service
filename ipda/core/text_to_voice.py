import torch
from TTS.api import TTS
from core.file_handler import FileHandler
from decorators.ttv_decorators import command_line

class TextToVoice:

    @command_line
    @staticmethod
    def ttv(file_name: str = None, audio_file: str = None):
        if torch.cuda.is_available():
            device = "cuda"
        else:
            device = "cpu"

        tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device=device)

        f = open(f"./ipda/exports/{file_name}", "r")

        fh = FileHandler()
        output_name = fh.get_file_name('exports')

        wav = tts.tts_to_file(text=f.read(), speaker_wav=f"./ipda/resources/{audio_file}", file_path=f"./ipda/exports/{output_name}.wav", language="en")
        print(f'file save name is: {output_name}')
