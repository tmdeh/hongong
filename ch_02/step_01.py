from pathlib import Path

WORK_DIR = Path(__file__).parent
IN_DIR, OUT_DRI = WORK_DIR / "input", WORK_DIR / "output"

if __name__ == "__main__":
  IN_DIR.mkdir(exist_ok=True)
  OUT_DRI.mkdir(exist_ok=True)
  