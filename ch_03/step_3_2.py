from pathlib import Path
from PIL import Image, ImageOps
from step_1_1 import IMG_DIR, OUT_DRI



OUT_3_2 = OUT_DRI / f"{Path(__file__).stem}.jpg"

if __name__ == "__main__":
  ROWS, COLS = 5, 8
  W_IMG, H_IMG = 500, 500
  W_BG, H_BG = COLS * W_IMG, ROWS * H_IMG
  start_X, start_Y = 0, 0

  img_bg = Image.new(mode="RGB", size=(W_BG, H_BG))
  path_sorted = sorted(Path(IMG_DIR).glob("*.jpg"))

  for path in path_sorted:
    img = Image.open(path)
    img_fit = ImageOps.fit(img, (W_IMG, H_IMG))
    img_bg.paste(img_fit, box=(start_X, start_Y))
    start_X += W_IMG
    if start_X >= W_BG:
      start_X = 0
      start_Y += H_IMG

  img_bg.save(OUT_3_2)
