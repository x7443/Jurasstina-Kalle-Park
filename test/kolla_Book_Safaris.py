import re
from playwright.sync_api import Playwright, sync_playwright, expect

#Test-ID: TC-SAF-02-POS

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Open web sidan frän lokal på datum.
    page.goto("http://127.0.0.1:8000/jurap.html")

    # Skriva en användarnamn och en password med färre än 8 tecken och clicka Register.
    page.get_by_role("link", name="Register").click()
    page.get_by_role("textbox", name="Username:").click()
    page.get_by_role("textbox", name="Username:").fill("Javi10")
    page.get_by_role("textbox", name="Password:").click()
    page.get_by_role("textbox", name="Password:").fill("965312396")
    page.get_by_role("button", name="Register").click()

    # Skriva en användarnamn och en password för att "registrera sig".
    page.get_by_role("link", name="Login").click()
    page.get_by_role("textbox", name="Username:").click()
    page.get_by_role("textbox", name="Username:").fill("Javi10")
    page.get_by_role("textbox", name="Password:").click()
    page.get_by_role("textbox", name="Password:").fill("965312396")

    # Skriva en användarnamn och en password för att  "logga in".
    page.get_by_role("button", name="Login").click()
    page.get_by_role("link", name="Buy Tickets").click()
    page.get_by_role("link", name="Buy Tickets", exact=True).click()
    page.get_by_label("Ticket Category:").select_option("VIP")
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Add to Cart").click()
    page.get_by_role("link", name="Book Safaris").click()
    page.get_by_role("textbox", name="Select Safari Date:").fill("2026-12-19")
    page.get_by_label("Select Safari Type:").select_option("T-Rex Rumble")
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Add to Cart").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)