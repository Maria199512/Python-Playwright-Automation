import time

from playwright.sync_api import Page, expect

def test_verify_pwlocators(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    # time.sleep(5)
    page.wait_for_timeout(5000)
    logo=page.get_by_alt_text("logo image")
    expect(logo).to_be_visible()



    expect(page.get_by_text(" text that you might want to locate.")).to_be_visible()
    expect(page.get_by_role("button", name="Primary Action")).to_be_visible()

