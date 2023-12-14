import requests
from tqdm import tqdm
# import ResourceGatherers as rg
from decorators.downloader_decorators import command_line

class DownloadManager:
    @command_line
    @staticmethod
    def download_file(url: str = None, address: str = None, fname: str = None, chunk_size=10241024):
        resp = requests.get(url, stream=True)
        total = int(resp.headers.get('content-length', 0))
        with open(address+fname, 'wb') as file, tqdm(
            desc=fname,
            total=total,
            unit='iB',
            unit_scale=True,
            unit_divisor=1024,
        ) as bar:
            for data in resp.iter_content(chunk_size=chunk_size):
                size = file.write(data)
                bar.update(size)

