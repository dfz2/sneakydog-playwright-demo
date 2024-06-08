

from playwright.sync_api import sync_playwright, Page


with sync_playwright() as  _playwright:
    browser = _playwright.chromium.launch(headless=False)
    _context = browser.new_context(storage_state="/home/dfz/Projects/sneakydog-playwright-demo/state.json", record_video_dir="./")
    _page: Page = _context.new_page()
    _page.goto("https://member.bilibili.com/platform/upload/video/frame")

    _page.wait_for_timeout(2000)
    _file_input = _page.locator("//div[@class='bcc-upload-wrapper']/input[@type='file']")
    _file_input.set_input_files("e608ec95350d359a40a2ac34f9fa3ca7.webm")
    _page.wait_for_load_state()

    video_title = _page.locator("//div[@class='video-title']").get_by_placeholder("清晰明了表明内容亮点的标题会更受观众欢迎哟！")
    video_title.fill("dasgadgadgadgag")

    video_tag = _page.locator("//div[@id='tag-container']").locator("//input[@type='text']")
    video_tag.fill("testsetseate")
    video_tag.press("Enter")

    _page.wait_for_timeout(10000)
    _page.locator("//div[@class='submit-container']").locator("//span[@class='submit-add']").click()
    
    _page.wait_for_timeout(10000)

