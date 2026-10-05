# Local Podcast Clips

A Codex skill for turning podcast footage into short clips with local tools. It supports Telugu transcription and Telugu-script captions without an OpusClip account or paid API.

## Install in Codex

```sh
git clone https://github.com/vamshicreates/local-podcast-clips.git ~/.codex/skills/local-podcast-clips
```

Read [the setup guide](references/setup.md) to install Python, FFmpeg, and `faster-whisper`, then run `python3 scripts/check_env.py` from the skill folder. The first transcription downloads a multilingual Whisper model. No podcast footage or model weights are included in this repository.

## Try it

In a Codex chat, say:

> Use $local-podcast-clips to review my Telugu podcast at `/path/to/episode.mp4`. Transcribe it locally, suggest timestamped short clips, and wait for my choice before exporting.

For a specified passage, ask Codex to export that passage directly. The skill's [instructions](SKILL.md) describe the workflow, commands, and limits.

This skill can transcribe and export a continuous excerpt with captions. It does not include OpusClip's hosted highlight ranking, face tracking, or AI Producer backend. Review Telugu spelling, captions, framing, and the finished video before publishing.
