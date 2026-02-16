import re
from playwright.sync_api import Playwright, sync_playwright, expect

# Test-ID: TC-MAP-15-POS
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=700)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://127.0.0.1:8000/jurap.html")

    page.get_by_role("link", name="Park Map").click()

    page.get_by_role("img", name="Jurasstina-Kalle Park Map").wait_for(state="visible")
    page.get_by_role("img", name="Jurasstina-Kalle Park Map").click()

    expect(page.get_by_role())

    page.get_by_role("link", name="Raptor Valley").wait_for(state="visible")
    page.get_by_role("link", name="Raptor Valley").click()

    page.get_by_role("link", name="Carnivore Zone").wait_for(state="visible")
    page.get_by_role("link", name="Carnivore Zone").click()

    page.get_by_role("link", name="Night Exhibit").wait_for(state="visible")
    page.get_by_role("link", name="Night Exhibit").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
