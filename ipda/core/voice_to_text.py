import whisper
import torch

from decorators.vtt_decorators import command_line
from decorators.general_decorators import del_and_collect

from core.file_handler import FileHandler


class VoiceToText:

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(VoiceToText, cls).__new__(cls)
        return cls.instance


    @command_line
    def vtt(self, file_name: str = None):
        if torch.cuda.is_available():
            model = whisper.load_model("base")
            model.to('cuda')

            result = model.transcribe(f"./ipda/temp/{file_name}")
            self.text = result["text"]


            torch.cuda.empty_cache()

            torch.cuda.reset_max_memory_allocated()
            torch.cuda.synchronize()

        return result["text"]
    
    @del_and_collect('text')
    def save_file(self):
        fh = FileHandler()
        fh.create_text_file(content=self.text)
