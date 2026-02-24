# Changelog

All notable changes to **uTube** will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] - 2025-02-24

### Added

- **Interactive CLI** with URL input loop and graceful exit (`q` to quit)
- **Quality picker** — fetches all available MP4 resolutions from YouTube and displays them with estimated file sizes before downloading
- **Smart format merging** — automatically merges separate video and audio streams into a single MP4 file using `ffmpeg` when YouTube doesn't offer a combined format
- **Auto-install** — detects if `yt-dlp` is missing and installs it automatically on first run via `pip`
- **URL validation** — accepts `youtube.com` and `youtu.be` links, rejects invalid URLs with a friendly message
- **Single-video mode** — `noplaylist: True` by default to prevent accidental playlist downloads
- **Cross-platform support** — tested on Windows, macOS, and Linux
- **README.md** — comprehensive documentation with architecture diagrams, installation guides, troubleshooting, and security model (OpenClaw-inspired style)
- **requirements.txt** — dependency file with annotated instructions
- **CHANGELOG.md** — this file

### Technical Details

- Built on top of [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) as the extraction engine
- Optional [`ffmpeg`](https://ffmpeg.org/) dependency for stream merging
- Single-file architecture (~160 lines of Python)
- Four core functions: `install_yt_dlp()`, `get_available_qualities()`, `download_video()`, `main()`

---

## [Unreleased]

### Planned

- Audio-only download mode (MP3 extraction)
- Playlist support (download all videos in a playlist)
- Custom output folder via CLI argument
- Progress bar with ETA during download
- Subtitle download support
- GUI version (Tkinter or web-based)

---

[1.0.0]: https://github.com/aquilu/utube/releases/tag/v1.0.0
[Unreleased]: https://github.com/aquilu/utube/compare/v1.0.0...HEAD
