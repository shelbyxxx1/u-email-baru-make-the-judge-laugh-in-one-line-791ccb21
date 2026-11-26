import os
import shutil
from pathlib import Path


LINE = "I joined a gym in January, went twice, and now I pay $40 a month for a stranger to email me that he misses me, like an ex with better cardio."


def main() -> None:
    assert 1 <= len(LINE) <= 200, "The entry must contain 1 to 200 characters."
    output_directory = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    output_directory.mkdir(parents=True, exist_ok=True)
    for output_entry in output_directory.iterdir():
        if output_entry.is_dir() and not output_entry.is_symlink():
            shutil.rmtree(output_entry)
        else:
            output_entry.unlink()
    output_path = output_directory / "entry.txt"
    output_path.write_bytes((LINE + "\n").encode("utf-8"))
    assert output_path.read_bytes().decode("utf-8") == LINE + "\n", "Output verification failed."


if __name__ == "__main__":
    main()
