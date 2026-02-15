import re

import pytest
from playwright.sync_api import Playwright, sync_playwright, expect
#Test ID: TC-SAF-02.2-NEG

@pytest.mark.VG_Javi
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Open web sidan frän lokal på datum.
    page.goto("http://127.0.0.1:8000/jurap.html")

    # Skriva en användarnamn och en password med färre än 8 tecken och clicka Register.
    page.get_by_role("link", name="Register").click()
    page.get_by_role("textbox", name="Username:").click()
    page.get_by_role("textbox", name="Username:").fill("PacoJavi10")
    page.get_by_role("textbox", name="Password:").click()
    page.get_by_role("textbox", name="Password:").fill("Panta")
    page.get_by_role("button", name="Register").click()

    #Felvalidering: systemet visar ett felmeddelande när lösenordet är ogiltigt (< 8 tecken)
    expect(page.get_by_text("Password must be at least 8 characters long.")).to_be_visible(timeout=5000)


    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
