<p align="center">
  <img src="https://img.icons8.com/color/150/youtube-play.png" alt="uTube Logo" width="150"/>
</p>

<h1 align="center">uTube</h1>
<p align="center"><strong>Your own personal YouTube ripper. Paste. Pick. Download. DONE!</strong></p>

<p align="center">
  <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python"></a>
  <a href="https://github.com/yt-dlp/yt-dlp"><img src="https://img.shields.io/badge/Powered_by-yt--dlp-red?style=for-the-badge&logo=youtube&logoColor=white" alt="yt-dlp"></a>
  <a href="https://github.com/aquilu/utube/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License"></a>
  <a href="https://github.com/aquilu/utube"><img src="https://img.shields.io/badge/Made_with-Love-ff69b4?style=for-the-badge" alt="Made with Love"></a>
</p>

---

> **Stop saving YouTube links that lead nowhere.** uTube grabs the actual video file — in the quality YOU choose — and drops it on your hard disk. No browser extensions. No shady websites. No bloatware. Just a clean Python script that does one thing and does it well.

---

## Table of Contents

- [TL;DR (Quick Start)](#-tldr-quick-start)
- [Highlights](#-highlights)
- [Installation](#-installation)
- [Usage](#-usage)
- [How It Works (Short)](#-how-it-works-short)
- [Architecture](#-architecture)
- [CLI Reference](#-cli-reference)
- [Configuration](#-configuration)
- [Security Model](#-security-model)
- [Dependencies & Runtime](#-dependencies--runtime)
- [Integrations](#-integrations)
- [Roadmap](#-roadmap)
- [Development / From Source](#-development--from-source)
- [Troubleshooting](#-troubleshooting)
- [Docs](#-docs)
- [Special Thanks](#-special-thanks)

---

## :zap: TL;DR (Quick Start)

Have Python 3.8+ installed? You're 10 seconds away:

```bash
# Clone
git clone https://github.com/aquilu/utube.git
cd utube

# Run
python youtube_downloader.py
```

That's it. Paste a URL. Pick a quality. Watch it download. **Real file on your real hard disk.**

> First run? `yt-dlp` will install itself automatically. Zero config needed.

---

## :fire: Highlights

- **One script, zero config** — just run it and go
- **Quality picker** — see every available resolution before downloading (1080p, 720p, 480p, 360p...)
- **File size estimates** — know how much disk space you need before committing
- **Auto-installs dependencies** — `yt-dlp` installs itself on first run if missing
- **Smart format merging** — if only separate video/audio streams exist, merges them into a single MP4
- **Always MP4** — no weird formats, no codec headaches, just universal MP4
- **Loop mode** — download as many videos as you want in a single session
- **Playlist-safe** — never accidentally downloads a 500-video playlist (single video mode by default)
- **Cross-platform** — works on Windows, macOS, and Linux
- **Lightweight** — single file, ~160 lines, no framework overhead

---

## :package: Installation

### Prerequisites

| Requirement | Version | Notes |
|-------------|---------|-------|
| **Python**  | 3.8+    | [Download here](https://www.python.org/downloads/) |
| **pip**     | Latest  | Comes with Python |
| **ffmpeg**  | Latest  | Required only for merging streams ([Download](https://ffmpeg.org/download.html)) |

### Option A: Clone (Recommended)

```bash
git clone https://github.com/aquilu/utube.git
cd utube
```

### Option B: Direct Download

Download `youtube_downloader.py` directly from the [releases page](https://github.com/aquilu/utube/releases) or just grab the raw file.

### Option C: pip install dependency manually

```bash
pip install yt-dlp
```

> **Note:** If you skip this step, uTube will install `yt-dlp` automatically on first run. We got you covered.

---

## :rocket: Usage

### Basic Flow

```bash
python youtube_downloader.py
```

You'll see this:

```
==================================================
   YouTube Video Downloader
==================================================

Paste a YouTube URL (or 'q' to quit): https://youtube.com/watch?v=dQw4w9WgXcQ

Fetching video info...

Title:    Rick Astley - Never Gonna Give You Up
Duration: 3:33
----------------------------------------

Available qualities:
  1. 1080p (~85 MB)
  2. 720p (~45 MB)
  3. 480p (~22 MB)
  4. 360p (~12 MB)

Choose quality (1-4) [1 = best]: 2

Selected: 720p (~45 MB)
Downloading... please wait.

Download complete!
```

### Pro Tips

| Action | How |
|--------|-----|
| **Best quality** | Just press Enter at the quality prompt (defaults to `1`) |
| **Download multiple** | After each download, paste another URL |
| **Exit** | Type `q` and press Enter |
| **Change output folder** | Modify the `output_folder` parameter in the code |

---

## :gear: How It Works (Short)

```
                          uTube Architecture
  ================================================================

  [You]
    |
    |  Paste YouTube URL
    v
  +---------------------------+
  |   youtube_downloader.py   |
  |                           |
  |  1. Validate URL          |
  |  2. Extract video info    |
  |  3. List MP4 qualities    |
  |  4. User picks quality    |
  |  5. Download selected     |
  +---------------------------+
    |               |
    |  yt-dlp       |  ffmpeg (if merge needed)
    v               v
  +----------+  +----------+
  | YouTube  |  |  Merge   |
  |  Servers |  |  Streams |
  +----------+  +----------+
    |               |
    v               v
  +---------------------------+
  |     your_video.mp4        |
  |     on YOUR hard disk     |
  +---------------------------+
```

---

## :building_construction: Architecture

uTube is intentionally minimal. One file. Four functions. No magic.

### Core Components

| Component | Function | Purpose |
|-----------|----------|---------|
| `install_yt_dlp()` | Bootstrap | Auto-installs `yt-dlp` if missing |
| `get_available_qualities()` | Inspector | Fetches video metadata and lists all available MP4 resolutions with estimated file sizes |
| `download_video()` | Downloader | Downloads the selected format, merges video+audio if needed |
| `main()` | Controller | Interactive loop: URL input → quality selection → download → repeat |

### Format Selection Logic

```
Available formats from YouTube
        |
        v
  Has combined MP4 (video+audio)?
       / \
     Yes   No
      |      |
      v      v
  Use as-is  Find best video stream
             + best audio stream
             → merge with ffmpeg → MP4
```

> **Why this matters:** YouTube increasingly serves video and audio as separate streams for higher resolutions. uTube handles the merge transparently — you always get a single, playable MP4 file.

---

## :keyboard: CLI Reference

uTube runs as an interactive CLI. No flags, no arguments, no manual pages to memorize.

```bash
# Launch
python youtube_downloader.py

# Inside the app:
# - Paste any YouTube URL to start
# - Enter a number to pick quality
# - Press Enter without a number for best quality
# - Type 'q' to quit
```

### Supported URL Formats

```
https://www.youtube.com/watch?v=VIDEO_ID       # Standard
https://youtu.be/VIDEO_ID                       # Short link
https://www.youtube.com/watch?v=ID&list=PL_ID   # Playlist link (downloads single video only)
```

---

## :wrench: Configuration

uTube works out of the box with sane defaults. Want to tweak? Edit these values in `youtube_downloader.py`:

```python
# Default output directory (current directory)
output_folder = "."

# Change to any path you want:
output_folder = "C:/Users/YourName/Videos"
output_folder = "/home/user/Downloads"

# Playlist behavior (True = single video only)
"noplaylist": True

# Output filename template
"outtmpl": f"{output_folder}/%(title)s.%(ext)s"
```

### Filename Template Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `%(title)s` | Video title | `My Cool Video` |
| `%(ext)s` | File extension | `mp4` |
| `%(id)s` | Video ID | `dQw4w9WgXcQ` |
| `%(upload_date)s` | Upload date | `20210101` |
| `%(resolution)s` | Resolution | `1080p` |

---

## :shield: Security Model

### What uTube Does

- **No data collection** — zero telemetry, zero analytics, zero phoning home
- **No accounts** — no login, no registration, no API keys
- **No network calls** — except to YouTube (via `yt-dlp`) to fetch the video you asked for
- **No file system access** — beyond writing the downloaded video to the output folder
- **No background processes** — runs only when you run it, exits when you tell it to
- **Open source** — every line of code is auditable right here

### What uTube Does NOT Do

- Does not store your watch history
- Does not access your YouTube/Google account
- Does not modify any system files
- Does not install system-wide services or daemons
- Does not require admin/root privileges

### Dependency Security

| Dependency | Source | Verified |
|------------|--------|----------|
| `yt-dlp` | [PyPI](https://pypi.org/project/yt-dlp/) / [GitHub](https://github.com/yt-dlp/yt-dlp) | Open source, 80k+ stars |
| `ffmpeg` | [ffmpeg.org](https://ffmpeg.org/) | Industry standard, open source |

---

## :jigsaw: Dependencies & Runtime

```
Python 3.8+
  └── yt-dlp (auto-installed)
        └── ffmpeg (optional, for stream merging)
```

| Package | Role | Auto-install? |
|---------|------|:---:|
| `yt-dlp` | YouTube extraction engine | Yes |
| `ffmpeg` | Audio/video stream merger | No (manual) |

### ffmpeg Installation

<details>
<summary><strong>Windows</strong></summary>

```bash
# Option 1: winget
winget install ffmpeg

# Option 2: choco
choco install ffmpeg

# Option 3: Download from https://ffmpeg.org/download.html
```
</details>

<details>
<summary><strong>macOS</strong></summary>

```bash
brew install ffmpeg
```
</details>

<details>
<summary><strong>Linux</strong></summary>

```bash
# Ubuntu/Debian
sudo apt install ffmpeg

# Fedora
sudo dnf install ffmpeg

# Arch
sudo pacman -S ffmpeg
```
</details>

---

## :electric_plug: Integrations

uTube is a standalone tool by design. However, it plays well with:

| Tool | Integration |
|------|-------------|
| **VLC** | Downloaded MP4 files open natively in VLC |
| **ffmpeg** | Used internally for stream merging |
| **Task Scheduler / cron** | Automate downloads with a URL list |
| **NAS / Network Drives** | Set `output_folder` to a network path |

### Batch Download (Power Users)

Want to download multiple videos from a text file? Create a wrapper:

```python
import subprocess

with open("urls.txt") as f:
    for url in f:
        url = url.strip()
        if url:
            subprocess.run(["python", "youtube_downloader.py"], input=f"{url}\n1\nq\n", text=True)
```

---

## :crystal_ball: Roadmap

- [ ] Audio-only download mode (MP3 extraction)
- [ ] Playlist support (download all videos in a playlist)
- [ ] Custom output folder via CLI argument
- [ ] Progress bar with ETA during download
- [ ] Subtitle download support
- [ ] GUI version (Tkinter or web-based)
- [ ] Docker container for server deployments
- [ ] URL list batch mode (built-in)
- [ ] Automatic `ffmpeg` installation

---

## :hammer_and_wrench: Development / From Source

```bash
# Clone the repository
git clone https://github.com/aquilu/utube.git
cd utube

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate          # Windows

# Install dependency
pip install yt-dlp

# Run
python youtube_downloader.py

# Run with a specific Python version
python3.11 youtube_downloader.py
```

### Project Structure

```
utube/
  ├── youtube_downloader.py   # The entire app. That's it. That's the project.
  ├── README.md               # You're reading it.
  └── LICENSE                  # MIT
```

> Yes, it's one file. That's the point. No build step. No transpilation. No Docker required. No 47 config files. **Just Python.**

---

## :sos: Troubleshooting

| Problem | Solution |
|---------|----------|
| `yt-dlp` not found | Run `pip install yt-dlp` manually |
| `ffmpeg` not found | Install ffmpeg ([see above](#ffmpeg-installation)) |
| Video won't download | Update yt-dlp: `pip install -U yt-dlp` |
| Permission error | Run from a folder where you have write access |
| URL not recognized | Make sure URL contains `youtube.com` or `youtu.be` |
| No qualities shown | Video may be age-restricted or region-locked |

---

## :books: Docs

| Resource | Link |
|----------|------|
| **yt-dlp Documentation** | [github.com/yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) |
| **ffmpeg Documentation** | [ffmpeg.org/documentation](https://ffmpeg.org/documentation.html) |
| **Python Downloads** | [python.org/downloads](https://www.python.org/downloads/) |
| **uTube Issues** | [github.com/aquilu/utube/issues](https://github.com/aquilu/utube/issues) |

---

## :heart: Special Thanks

- **[yt-dlp](https://github.com/yt-dlp/yt-dlp)** — The incredible engine under the hood. Without this project, none of this would work. 80k+ stars of pure community power.
- **[ffmpeg](https://ffmpeg.org/)** — The Swiss Army knife of multimedia. Decades of open-source excellence.
- **Mahmoud** — For the original request that sparked this project. Your friendship and perseverance through tough times inspire us. Wishing you the best of health always.
- **The Python Community** — For making it possible to build useful tools in 160 lines of code.

---

<p align="center">
  <strong>Made with :heart: by <a href="https://github.com/aquilu">aquilu</a></strong>
  <br>
  <sub>Because your videos deserve to live on your hard disk, not just as a link.</sub>
</p>

---

<p align="center">
  <sub>If uTube helped you, consider giving it a :star: on <a href="https://github.com/aquilu/utube">GitHub</a>.</sub>
</p>
