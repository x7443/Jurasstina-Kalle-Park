import re
import pytest
from playwright.sync_api import Playwright, sync_playwright, expect

# Test-ID: TC-BOOK-11-NEG
@pytest.mark.VG_Almedin
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=700)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://127.0.0.1:8000/jurap.html")

    #Kod för registrering och login, förberedelse för test; START
    page.get_by_role("link", name="Register").click()
    page.get_by_role("textbox", name="Username:").click()
    page.get_by_role("textbox", name="Username:").fill("User2")
    page.get_by_role("textbox", name="Username:").press("Tab")
    page.get_by_role("textbox", name="Password:").fill("ABCD1234")
    page.get_by_role("button", name="Register").click()

    expect(page.get_by_role("Heading", name="Login")).to_be_visible()

    page.get_by_role("textbox", name="Username:").click()
    page.get_by_role("textbox", name="Username:").fill("User2")
    page.get_by_role("textbox", name="Username:").press("Tab")
    page.get_by_role("textbox", name="Password:").fill("ABCD1234")
    page.get_by_role("button", name="Login").click() # Förberedelse SLUT

    # START AV TEST
    # Användare trycker på flik "Buy tickets"
    page.get_by_role("link", name="Buy Tickets", exact=True).click()

    # Användare väljer "child" i fältet "ticket type" bland de förvalda valen
    page.get_by_label("Ticket Type:").select_option("Child")
    page.once("dialog", lambda dialog: dialog.dismiss())

    # Användare trycker på knapp "Add to cart"
    page.get_by_role("button", name="Add to Cart").click()

    # Användare trycker på flik "Book safari"
    page.get_by_role("link", name="Book Safaris").click()

    # Användare trycker på kalenderikon och väljer datum i kalendern
    page.get_by_role("textbox", name="Select Safari Date:").fill("2026-02-28")

    # Användare väljer bland de förvalda valen "T-Rex Rumble"
    page.get_by_label("Select Safari Type:").select_option("T-Rex Rumble")

    # Användare trycker på "Add to cart" för att lägga till bokningen i kundvagnen
    page.get_by_role("button", name="Add to Cart").click()

    expect(page.get_by_text("VIP tickets required to book")).to_be_visible()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)