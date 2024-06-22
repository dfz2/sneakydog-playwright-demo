

from playwright.sync_api import sync_playwright, expect, Browser, BrowserContext, Page


with sync_playwright() as  _playwright:
    browser = _playwright.chromium.launch(headless=False)
    _context = browser.new_context(record_video_dir="./")
    _page = _context.new_page()
    
    _page.goto("https://bilibili.com/")
    _profile_img = _page.locator('//img[@class="bili-avatar-img bili-avatar-face bili-avatar-img-radius"]')
    expect(_profile_img).to_be_visible(timeout=10 * 60 * 1000)

    _context.storage_state(path="/home/pi/.config/bilibili/state.json")

 
