import re

import pytest
from playwright.sync_api import Playwright, sync_playwright, expect



# Test ID: TC-SAF-02.1-NEG

@pytest.mark.VG_Javi
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # Öppna webbsidan från lokal server
    page.goto("http://127.0.0.1:8000/jurap.html")

    # Skriva en användarnamn och en password och clicka Register.
    page.get_by_role("link", name="Register").click()
    page.get_by_role("textbox", name="Username:").fill("PacoJavi10")
    page.get_by_role("textbox", name="Password:").fill("965312396")
    page.get_by_role("button", name="Register").click()

    # Skriva en användarnamn och en password för att "loga in".
    page.get_by_role("textbox", name="Username:").fill("PacoJavi10")
    page.get_by_role("textbox", name="Password:").fill("965312396")
    page.get_by_role("button", name="Login").click()

    # Väljer en Regular-biljett för att köpa den på helgen datum.
    page.get_by_role("link", name="Buy Tickets", exact=True).click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Add to Cart").click()

    # Går till safari-bokningen och väljer ett datum på en helg
    page.get_by_role("link", name="Book Safaris").click()
    page.get_by_role("textbox", name="Select Safari Date:").fill("2026-12-19")

    #  Skapar en lyssnare som hanterar webbläsarens popup-dialoger.
    def handle_error_dialog(dialog):
        # Validerar felmeddelandet enligt krav: VIP krävs för helger
        expected_msg = "VIP tickets required to book safaris on weekends."
        print(f"Validando mensaje de error: {dialog.message}")
        assert expected_msg in dialog.message
        dialog.dismiss()

    # Aktiverar händelsehanteraren INNAN klicket utförs
    page.on("dialog", handle_error_dialog)

    # Triggar logiken som genererar felmeddelandet
    page.get_by_role("button", name="Add to Cart").click()
