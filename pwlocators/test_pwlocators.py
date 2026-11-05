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

    page.get_by_label("Email Address:").fill("test123@gmail.com")
    page.get_by_label("Your Age:").fill("23")
    page.wait_for_timeout(5000)

    page.get_by_placeholder("Enter your full name").fill("Jithin John")
    page.get_by_placeholder("Type your message here...").fill("Testing using python playwright")
    page.wait_for_timeout(5000)

    expect(page.get_by_title("Home page link")).to_have_text("Home")
    page.wait_for_timeout(5000)

    expect(page.get_by_test_id("profile-name")).to_have_text("John Doe")
