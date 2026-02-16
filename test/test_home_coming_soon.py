import re

from playwright.sync_api import Playwright, sync_playwright, expect
#Test-ID: TC-COM-03-POS

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=700)
    context = browser.new_context()
    page = context.new_page()

    # Open web sidan frän lokal på datum.
    page.goto("http://127.0.0.1:8000/jurap.html")

    # Verifiera att sektionen/knappen syns
    expect(page.get_by_text("Dine with Dinosaurs")).to_be_visible()
    coming_soon = page.get_by_text("Coming Soon!", exact=True)
    expect(coming_soon).to_be_visible()

    page.get_by_text("Coming Soon!").click()

    # Spara URL innan klick
    url_before = page.url

    # Ingen navigering och vi är kvar på Home
    expect(page).to_have_url(url_before)
    expect(page.get_by_text("Welcome to Jurasstina-Kalle Park!")).to_be_visible()




    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
