import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Open web sidan frän lokal på datum.
    page.goto("http://127.0.0.1:8000/jurap.html")

    # Klickar på "Register" för att öppna registreringsformuläret.
    page.get_by_role("link", name="Register").click()

    # Skriva en användarnamn och en password med färre än 8 tecken och clicka Register.
    page.get_by_role("textbox", name="Username:").click()
    page.get_by_role("textbox", name="Username:").fill("Javilon9")
    page.get_by_role("textbox", name="Password:").click()
    page.get_by_role("textbox", name="Password:").fill("Panta")

    # Klickar på "Register".
    page.get_by_role("button", name="Register").click()

    # Verifierar att ett varningsmeddelande visas om lösenordet är kortare än 8 tecken
    expect(page.get_by_text("Password must be at least 8 characters long.")).to_be_visible()


    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

