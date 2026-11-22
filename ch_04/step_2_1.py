
from pathlib import Path
from step_1_1 import OUT_DIR

data = [
  "BEGIN:VCARD",
  "VERSION:3.0",
  "N:유;승도;;;",
  "FN:유승도",
  "TEL;type=CELL:+82 10-9342-3216",
  "END:VCARD",
]

vcf = "\n".join(data)
with open(OUT_DIR / f"{Path(__file__).stem}.vcf", "w", encoding="utf-8") as fp:
  fp.write(vcf)

import qrcode

img = qrcode.make(vcf)
img