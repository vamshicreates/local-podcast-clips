# Setup on another laptop

This skill needs Python 3.11 or 3.12, FFmpeg with FFprobe, and the Python package `faster-whisper`. Install FFmpeg through the operating system's usual package manager. Confirm `ffmpeg -version`, `ffprobe -version`, and `python3 --version` before use.

From the skill folder:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install faster-whisper
python scripts/check_env.py
```

On Windows PowerShell, activate with `.venv\Scripts\Activate.ps1` and use `python` in place of `python3`. Keep the virtual environment in the skill folder; it is excluded from the portable ZIP.

The first transcription downloads the selected Whisper model. For Telugu, use a multilingual model such as `medium` or `large-v3`, not a name ending in `.en`. `medium` is the default balance between speed and accuracy; switch to `large-v3` if the hardware permits and accuracy needs improvement. Explicitly set `--language te` and leave translation off to keep Telugu output. Verify code-switched English names and Telugu spelling by listening.

To burn Telugu captions, install a font with Telugu glyphs, such as Noto Sans Telugu, on the laptop. Run a short test export and inspect the shaped glyphs; a successful FFmpeg exit code does not prove the captions look correct. The default export leaves captions as a separate `.srt`, which can be corrected and imported into an editor.

The helper does a single continuous cut with a fixed crop position. Use `--position 0` for the left edge, `0.5` for center, or `1` for the right edge; values between these are allowed. It cannot automatically track a moving speaker or combine multiple camera angles.

The workflow uses no OpusClip key or credits. Model downloads and package installation need an internet connection once; subsequent transcription can run locally.
