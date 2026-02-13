import re
from csv import excel
import pytest

from playwright.sync_api import Playwright, sync_playwright, expect
#  Test-ID: TC-BOOK-09-NEG
@pytest.mark.VG_Almedin
def run(playwright: Playwright) -> None:

    #Jag fattar inte varför tester går igenom med slow mo = 2000 och inte när man kör det utan slow_mo=
    browser = playwright.chromium.launch(headless=False, slow_mo= 2000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://127.0.0.1:8000/jurap.html")

    # Kod för registrering och login, förberedelse för test; START
    page.get_by_role("link", name="Register").click()
    page.get_by_role("textbox", name="Username:").click()
    page.get_by_role("textbox", name="Username:").fill("User1")
    page.get_by_role("textbox", name="Username:").press("Tab")
    page.get_by_role("textbox", name="Password:").fill("12345678")
    page.get_by_role("button", name="Register").click()

    expect(page.get_by_role("Heading", name="Login")).to_be_visible()

    page.get_by_role("textbox", name="Username:").click()
    page.get_by_role("textbox", name="Username:").fill("User1")
    page.get_by_role("textbox", name="Username:").press("Tab")
    page.get_by_role("textbox", name="Password:").fill("12345678")
    page.get_by_role("button", name="Login").click() # Förberedelse SLUT

    # TEST BÖRJA HÄR
    page.get_by_role("link", name="Book Safaris").click() # Användare trycker på flik "Book Safari"
    page.get_by_role("textbox", name="Select Safari Date:").fill("2026-02-18") # Användare trycker på kalenderikonen och väljer datum i fältet "Select Safari date"
    page.get_by_role("button", name="Add to Cart").click() # Användare trycker på knapp "Add to cart" för att lägga till vad safaribokning

    # Resultat: Följande felmeddelande med en ruta dyker upp:
    expect(page.get_by_text("You must purchase a general admission ticket before booking a safari.")).to_be_visible()


    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)



