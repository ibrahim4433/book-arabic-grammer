import concurrent.futures
import csv
import sys
import threading
import time
from pathlib import Path

import questionary
from rich import box
from rich.console import Console
from rich.live import Live
from rich.table import Table

# Ensure modules are importable
sys.path.append(str(Path(__file__).parent))
from youtube_offline_transcriber import YouTubeOfflineTranscriber

console = Console()


class YouTubeOfflineUI:
    def __init__(self, project_root):
        self.project_root = Path(project_root)
        self.transcriber = YouTubeOfflineTranscriber(self.project_root)
        self.tasks_status = {}  # {seq_num: {"title": ..., "status": ..., "message": ...}}
        self.lock = threading.Lock()

    def generate_ui_table(self):
        table = Table(
            title="YouTube Transcription Progress (Max 3 Concurrent)", box=box.ROUNDED, expand=True
        )
        table.add_column("Seq", justify="right", style="cyan", width=4)
        table.add_column("Video Title", style="white")
        table.add_column("Status", style="bold")
        table.add_column("Message", style="dim")

        with self.lock:
            # Sort by sequence number
            for seq in sorted(self.tasks_status.keys()):
                t = self.tasks_status[seq]
                status_color = "yellow"
                if t["status"] == "SUCCESS":
                    status_color = "green"
                elif t["status"] == "ERROR":
                    status_color = "red"
                elif t["status"] == "PENDING":
                    status_color = "dim"

                table.add_row(
                    str(seq),
                    t["title"][:50] + ("..." if len(t["title"]) > 50 else ""),
                    f"[{status_color}]{t['status']}[/]",
                    t["message"],
                )
        return table

    def process_batch(self, videos):
        """
        videos is a list of tuples: (url, title, seq_num)
        """
        for url, title, seq in videos:
            self.tasks_status[seq] = {"title": title, "status": "PENDING", "message": "Waiting..."}

        start_time = time.time()

        with Live(self.generate_ui_table(), refresh_per_second=4, console=console) as live:

            def worker(video_info):
                url, title, seq = video_info
                with self.lock:
                    self.tasks_status[seq]["status"] = "RUNNING"
                    self.tasks_status[seq]["message"] = "Fetching and applying Tashkeel..."
                live.update(self.generate_ui_table())

                success, msg = self.transcriber.process_video(url, title, seq)

                with self.lock:
                    self.tasks_status[seq]["status"] = "SUCCESS" if success else "ERROR"
                    self.tasks_status[seq]["message"] = msg
                live.update(self.generate_ui_table())

            with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
                # Submit all tasks
                futures = [executor.submit(worker, v) for v in videos]
                concurrent.futures.wait(futures)

        console.print(
            f"[bold green]✅ Batch Completed in {int(time.time() - start_time)} seconds![/bold green]"
        )

    def parse_csv(self, csv_path):
        """Reads the CSV and extracts (url, title, seq_num)."""
        videos = []
        try:
            with open(csv_path, encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for i, row in enumerate(reader):
                    title = row.get("Video Title") or row.get("Title") or f"Video_{i + 1}"
                    url = row.get("Video URL") or row.get("URL") or ""
                    if url.strip():
                        videos.append((url.strip(), title.strip(), i + 1))
            return videos
        except Exception as e:
            console.print(f"[red]Error parsing CSV: {e}[/red]")
            return []


def run_jules_youtube_ui(state_manager=None):
    console.clear()
    console.print("[bold cyan]▶ Offline YouTube Transcriber (No API Keys Needed)[/bold cyan]\n")

    project_root = Path(__file__).parent.parent.parent.parent.parent
    ui = YouTubeOfflineUI(project_root)

    mode = questionary.select(
        "Select Mode:",
        choices=["1) Process Single YouTube Link", "2) Batch Process from CSV file", "3) Cancel"],
    ).ask()

    if not mode or mode.startswith("3"):
        return

    if mode.startswith("1"):
        url = questionary.text("Enter YouTube URL:").ask()
        if not url:
            return
        title = questionary.text("Enter Video Title (or leave blank):").ask()
        if not title:
            title = "Single_Video"

        ui.process_batch([(url, title, 1)])

    elif mode.startswith("2"):
        # Find CSV files
        csv_dirs = [project_root / "input" / "csv-youtube", project_root / "Pdf-new-resource"]

        csv_files = []
        for d in csv_dirs:
            if d.exists():
                csv_files.extend(list(d.glob("*.csv")))

        if not csv_files:
            console.print(
                "[red]No CSV files found in input/csv-youtube/ or Pdf-new-resource/.[/red]"
            )
            time.sleep(2)
            return

        choices = [str(f.relative_to(project_root)) for f in csv_files]
        selected = questionary.select("Select CSV file:", choices=choices).ask()

        if not selected:
            return

        csv_path = project_root / selected
        videos = ui.parse_csv(csv_path)

        if not videos:
            console.print("[yellow]No valid videos found in CSV.[/yellow]")
            time.sleep(2)
            return

        console.print(f"[green]Found {len(videos)} videos in {selected}. Starting batch...[/green]")
        time.sleep(1)
        ui.process_batch(videos)


if __name__ == "__main__":
    run_jules_youtube_ui()
