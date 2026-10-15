"""Render .github/banner/banner.html to .github/assets/banner.png (2x, transparent corners)."""
from pathlib import Path
from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent
OUT = HERE.parent / "assets" / "banner.png"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1280, "height": 440}, device_scale_factor=2)
    page.goto((HERE / "banner.html").as_uri())
    page.wait_for_timeout(300)
    page.screenshot(path=str(OUT), omit_background=True)
    browser.close()
print(f"wrote {OUT}")
