import re
from playwright.sync_api import Playwright, sync_playwright, expect

# Test-ID: TC-BOOK-12-POS
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=700)
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
    page.get_by_role("button", name="Login").click() #Förberedelse SLUT

    # START AV TEST
    # Användare väljer flik "Buy tickets"
    page.get_by_role("link", name="Buy Tickets", exact=True).click()

    # Användare väljer senior i de förvalda/statiska valen
    page.get_by_label("Ticket Type:").select_option("Senior")

    # Användare väljer biljett-kategori "VIP-biljett"
    page.get_by_label("Ticket Category:").select_option("VIP")
    page.once("dialog", lambda dialog: dialog.dismiss())

    # Användare trycker på knapp "Add to cart"
    page.get_by_role("button", name="Add to Cart").click()

    # ANvändare trycker på flik "Book Safari"
    page.get_by_role("link", name="Book Safaris").click()

    # Användare tabbar för att komma till "Select Safari date"-fältet
    page.get_by_role("textbox", name="Select Safari Date:").press("Tab")

    # Användare matar in datum genom det fysiska tangentbordet
    page.get_by_role("textbox", name="Select Safari Date:").fill("2026-02-28")

    # Användare väljer "Herbivore Tour with feeding" i fältet "Select safari type"
    page.get_by_label("Select Safari Type:").select_option("Herbivore Tour with Feeding")
    page.once("dialog", lambda dialog: dialog.dismiss())

    # Användare lägger till bokningen i kundvagnen genom att trycka på "Add to cart"
    page.get_by_role("button", name="Add to Cart").click()

    # Användaren trcker på cart för att se resultatet av testet
    page.get_by_role("link", name="Cart").click()
    page.once("dialog", lambda dialog: dialog.dismiss())

    # Användaren trycker på "Proceed to checkout" för att simulera ett genomfört köp
    page.get_by_role("button", name="Proceed to Checkout").click()

    # Använder trycker på "cart" igen för att kontrollera att köpet gått igenom och inget är kvar i kundvagnen
    page.get_by_role("link", name="Cart").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)