import re
from playwright.sync_api import Playwright, sync_playwright, expect

#Test-ID: TC-ALERTS-14-POS
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1500)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://127.0.0.1:8000/jurap.html")

    # Användaren trycker på fliken "Dino alerts"
    page.get_by_role("link", name="Dino Alerts").click()

    # Användaren scrollar ner på båda sidorna stegvis för att läsa allt innehåll
    for i in range(5):
        page.mouse.wheel(0,1000)
        page.wait_for_timeout(500)


    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)