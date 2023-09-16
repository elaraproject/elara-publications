#!/usr/bin/env python3

import mistune
import sys
from pathlib import Path

HTML_TEMPLATE = Path("template.html").read_text()

def info(i):
  print("[INFO]", i)

def error(e):
  print("[ERROR]", e)
  help()

# TODO: add convert to PDF directly with Pyppeteer
def help():
  print("Usage: build.py [input.md]")

def main():
  if len(sys.argv) < 2 or len(sys.argv) > 2:
    error("Check your arguments")
    return 1
  input_path = Path(sys.argv[1])
  if input_path.is_file() == False:
    error("Check if input file exists?")
    return 1
  if input_path.suffix != ".md":
    error(f"Check if input file {str(input_path)} is a markdown file?")
    return 1
  info(f"Processing {str(input_path)}")
  markdown = input_path.read_text()
  title = markdown.split("\n")[0][2:]
  html = mistune.html(markdown)
  output_html = HTML_TEMPLATE.format(title, html)
  output_path = Path(str(input_path.with_suffix(".html")).replace("papers", "dist"))
  info(f"Writing to {str(output_path)}")
  output_path.write_text(output_html)
  info("All done")

if __name__ == "__main__":
  main()
