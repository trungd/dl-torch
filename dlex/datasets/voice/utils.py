import os
from struct import unpack
from subprocess import call

import numpy as np

from dlex.utils import logger


def read_htk(path):
    try:
        with open(path, "rb") as fh:
            spam = fh.read(12)
            nSamples, sampPeriod, sampSize, parmKind = unpack(">IIHH", spam)
            veclen = int(sampSize / 4)
            fh.seek(12, 0)
            dat = np.fromfile(fh, dtype=np.float32)
            dat = dat.reshape(len(dat) // veclen, veclen)
            dat = dat.byteswap()
        return dat
    except Exception:
        logger.error("Error reading '%s'." % path)
        return None


def audio2wav(audio_path, wav_path):
    if not os.path.exists(wav_path):
        call(
            ["ffmpeg", "-i", audio_path, "-ar", "16000", "-ac", "1", wav_path],
            stdout=audio_path,
            stderr=audio_path)


def wav2htk(wav_path, htk_path):
    if not os.path.exists(htk_path):
        call([
            os.path.join(os.getenv('HCOPY_PATH', 'HCopy')),
            wav_path,
            htk_path,
            "-C", "config.lmfb.40ch"])