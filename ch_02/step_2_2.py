from pathlib import Path
from fnmatch import fnmatch
import unicodedata
import pandas as pd
from step_01 import IN_DIR, OUT_DRI

OUT_2_2 = OUT_DRI / f"{Path(__file__).stem}.xlsx"

if __name__ == "__main__":
  result = []

  for xlsx_path in sorted(Path(IN_DIR).glob("*.xlsx")):
    # macOS에서는 한글 파일명이 자모로 분리되어 저장될 수 있습니다.
    filename = unicodedata.normalize("NFC", xlsx_path.name)
    if not fnmatch(filename, "2024년*월.xlsx"):
      continue
    df_raw = pd.read_excel(
      xlsx_path, 
      sheet_name="Sheet1", 
      usecols="B:E", 
      skiprows=2
    )
    result.append(df_raw)

  if not result:
    raise FileNotFoundError(f"{IN_DIR}에서 '2024년*월.xlsx' 파일을 찾지 못했습니다.")

  df_concat = pd.concat(result, ignore_index=True)
  OUT_DRI.mkdir(parents=True, exist_ok=True)
  df_concat.to_excel(OUT_2_2, index=False)
