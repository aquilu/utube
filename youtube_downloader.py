"""
YouTube Video Downloader
A simple tool to download YouTube videos with quality selection.
Requires: pip install yt-dlp
"""

import subprocess
import sys


def install_yt_dlp():
    """Install yt-dlp if not already installed."""
    try:
        import yt_dlp
    except ImportError:
        print("Installing yt-dlp... please wait.")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "yt-dlp"])
        print("yt-dlp installed successfully!\n")


def get_available_qualities(url):
    """Fetch available video qualities for a YouTube URL."""
    import yt_dlp

    options = {"quiet": True, "noplaylist": True}

    with yt_dlp.YoutubeDL(options) as ydl:
        info = ydl.extract_info(url, download=False)

    title = info.get("title", "Unknown")
    duration = info.get("duration_string", "Unknown")

    # Collect unique mp4 video+audio qualities
    qualities = {}
    for f in info.get("formats", []):
        ext = f.get("ext", "")
        height = f.get("height")
        vcodec = f.get("vcodec", "none")
        acodec = f.get("acodec", "none")

        if ext == "mp4" and height and vcodec != "none" and acodec != "none":
            label = f"{height}p"
            filesize = f.get("filesize") or f.get("filesize_approx")
            size_str = f" (~{filesize / 1024 / 1024:.0f} MB)" if filesize else ""
            qualities[height] = {
                "label": f"{label}{size_str}",
                "format_id": f.get("format_id"),
                "height": height,
            }

    # If no combined mp4 formats, offer video+audio merge options
    if not qualities:
        video_formats = {}
        for f in info.get("formats", []):
            height = f.get("height")
            vcodec = f.get("vcodec", "none")
            if height and vcodec != "none":
                if height not in video_formats or (f.get("filesize") or 0) > (video_formats[height].get("filesize") or 0):
                    filesize = f.get("filesize") or f.get("filesize_approx")
                    size_str = f" (~{filesize / 1024 / 1024:.0f} MB)" if filesize else ""
                    video_formats[height] = {
                        "label": f"{height}p{size_str}",
                        "format_id": f.get("format_id"),
                        "height": height,
                        "needs_merge": True,
                    }
        qualities = video_formats

    return title, duration, qualities


def download_video(url, format_choice, needs_merge=False, output_folder="."):
    """Download a YouTube video with the selected format."""
    import yt_dlp

    if needs_merge:
        options = {
            "format": f"{format_choice}+bestaudio",
            "merge_output_format": "mp4",
            "outtmpl": f"{output_folder}/%(title)s.%(ext)s",
            "noplaylist": True,
        }
    else:
        options = {
            "format": format_choice,
            "outtmpl": f"{output_folder}/%(title)s.%(ext)s",
            "noplaylist": True,
        }

    with yt_dlp.YoutubeDL(options) as ydl:
        print("\nDownloading... please wait.")
        ydl.download([url])
        print("\nDownload complete!")


def main():
    print("=" * 50)
    print("   YouTube Video Downloader")
    print("=" * 50)
    print()

    while True:
        url = input("Paste a YouTube URL (or 'q' to quit): ").strip()

        if url.lower() == "q":
            print("Goodbye!")
            break

        if "youtube.com" not in url and "youtu.be" not in url:
            print("That doesn't look like a YouTube URL. Try again.\n")
            continue

        try:
            print("\nFetching video info...")
            title, duration, qualities = get_available_qualities(url)

            print(f"\nTitle:    {title}")
            print(f"Duration: {duration}")
            print("-" * 40)

            if not qualities:
                print("No downloadable qualities found.")
                continue

            # Sort by resolution (highest first)
            sorted_qualities = sorted(qualities.values(), key=lambda x: x["height"], reverse=True)

            print("\nAvailable qualities:")
            for i, q in enumerate(sorted_qualities, 1):
                print(f"  {i}. {q['label']}")

            print()
            choice = input(f"Choose quality (1-{len(sorted_qualities)}) [1 = best]: ").strip()

            if not choice:
                choice = "1"

            if not choice.isdigit() or int(choice) < 1 or int(choice) > len(sorted_qualities):
                print("Invalid choice, using best quality.")
                choice = "1"

            selected = sorted_qualities[int(choice) - 1]
            needs_merge = selected.get("needs_merge", False)

            print(f"\nSelected: {selected['label']}")
            download_video(url, selected["format_id"], needs_merge)

        except Exception as e:
            print(f"\nError: {e}")
            print("Please check the URL and try again.")

        print()


if __name__ == "__main__":
    install_yt_dlp()
    main()
