from playwright.sync_api import sync_playwright

def test_open_site():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        page = browser.new_page()
        page.goto("https://www.saucedemo.com/")

        page.wait_for_timeout(3000)
        page.locator("#user-name").fill("standard_user")
        page.wait_for_timeout(3000)
        page.locator("#password").fill("secret_sauce")
        page.wait_for_timeout(3000)
        page.click('#login-button')
        page.wait_for_timeout(3000)

