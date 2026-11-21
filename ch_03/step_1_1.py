from pathlib import Path

WORK_DIR = Path(__file__).parent
IN_DIR, OUT_DRI, IMG_DIR = WORK_DIR / "input", WORK_DIR / "output",  WORK_DIR / "img"

if __name__ == "__main__":
  IMG_DIR.mkdir(exist_ok=True)
  IN_DIR.mkdir(exist_ok=True)
  OUT_DRI.mkdir(exist_ok=True)
  