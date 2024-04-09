# What tasks can ipda perform?

1. With this service, you can extract text from videos and audio files.
2. Summarize the extracted text for easier comprehension.
3. Convert the summarized text or the original content into speech using any desired voice, providing a more accessible format for users.

## Install Dependencies

```
pip install -r requirements.txt
```

**for install cu118 manually (Recommended)**

```
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

**if you have problem with your nvidia driver in linux try to install nvidia-driver-535**

```
sudo apt install nvidia-driver-535
```

**also need ffmpeg**

```
sudo apt update && sudo apt install ffmpeg
```
