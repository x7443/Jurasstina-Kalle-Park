import re
import pytest
from playwright.sync_api import Playwright, sync_playwright, expect

# Test-ID: TC-BOOK-13-NEG
@pytest.mark.VG_Almedin
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=2000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://127.0.0.1:8000/jurap.html")
    page.get_by_role("link", name="Register").click() #Förberedelse av test START
    page.get_by_role("textbox", name="Username:").click()
    page.get_by_role("textbox", name="Username:").fill("User4")
    page.get_by_role("textbox", name="Password:").click()
    page.get_by_role("textbox", name="Password:").fill(",.-12345")
    page.get_by_role("button", name="Register").click()

    expect(page.get_by_role("Heading", name="Login")).to_be_visible()

    page.get_by_role("textbox", name="Username:").click()
    page.get_by_role("textbox", name="Username:").click()
    page.get_by_role("textbox", name="Username:").fill("User4")
    page.get_by_role("textbox", name="Username:").press("Tab")
    page.get_by_role("textbox", name="Password:").fill(",.-12345")
    page.get_by_role("button", name="Login").click() #Förberedelse SLUT

    # Användare trycker på flik "Buy tickets"
    page.get_by_role("link", name="Buy Tickets", exact=True).click()

    # Användare fyller i antalet biljetter
    page.get_by_role("spinbutton", name="Quantity:").click()
    page.get_by_role("spinbutton", name="Quantity:").fill("5")
    page.once("dialog", lambda dialog: dialog.dismiss())

    # Användare trycker på knappen "Add to cart" för att lägga till biljetterna
    page.get_by_role("button", name="Add to Cart").click()

    # Användare trycker på flik "Book Safari"
    page.get_by_role("link", name="Book Safaris").click()

    # Användare fyller i ett datum som passerat/ bakåt i tiden
    page.get_by_role("textbox", name="Select Safari Date:").fill("2026-02-10")

    # Användare väljer safarityp
    page.get_by_label("Select Safari Type:").select_option("Herbivore Tour")

    # Användare lägger till vald safarityp i kundvagnen genom att trycka på "Add to cart"
    page.get_by_role("button", name="Add to Cart").click()

    expect(page.get_by_text("You cannot book a safari for"))

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
