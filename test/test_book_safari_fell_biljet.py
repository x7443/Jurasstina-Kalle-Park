import re

import pytest
from playwright.sync_api import Playwright, sync_playwright, expect
#Test ID: TC-SAF-02.1-NEG

@pytest.mark.VG_Javi
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False,slow_mo=700)
    context = browser.new_context()
    page = context.new_page()

    # Open web sidan frän lokal på datum.
    page.goto("http://127.0.0.1:8000/jurap.html")

    # Klickar på "Register" för att öppna registreringsformuläret.
    page.get_by_role("link", name="Register").click()

    # Skriva en användarnamn och en password och clicka Register.
    page.get_by_role("link", name="Register").click()
    page.get_by_role("textbox", name="Username:").click()
    page.get_by_role("textbox", name="Username:").fill("Javi10")
    page.get_by_role("textbox", name="Password:").click()
    page.get_by_role("textbox", name="Password:").fill("965312396")
    page.get_by_role("button", name="Register").click()
    expect(page.get_by_role("heading", name="Login")).to_be_visible()


    # Skriva en användarnamn och en password för att "loga in".
    page.get_by_role("link", name="Login").click()
    page.get_by_role("textbox", name="Username:").click()
    page.get_by_role("textbox", name="Username:").fill("Javi10")
    page.get_by_role("textbox", name="Password:").click()
    page.get_by_role("textbox", name="Password:").fill("965312396")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_text("Welcome to Jurasstina-Kalle Park!")).to_be_visible()

    ### HÄR BÖRJAR TESTET ###

    #Väljer en Regular-biljett för att köpa den och lägga till den i varukorgen.
    page.get_by_role("link", name="Buy Tickets", exact=True).click()
    page.get_by_role("button", name="Add to Cart").click()
    page.get_by_role("link", name="Book Safaris").click()
    page.get_by_role("textbox", name="Select Safari Date:").fill("2026-12-19")
    page.get_by_role("button", name="Add to Cart").click()



    #Felvalidering: systemet visar ett felmeddelande
    expect(page.get_by_text("VIP tickets required to book safaris on weekends.")).to_be_visible


    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
