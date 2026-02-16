import re
from playwright.sync_api import Playwright, sync_playwright, expect

#Test-ID: TC-BOOK-10-POS
def run(playwright: Playwright) -> None:

    browser = playwright.chromium.launch(headless=False, slow_mo=700)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://127.0.0.1:8000/jurap.html")

    #Kod för registrering och login, förberedelse för test; START
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

    # TEST BÖRJAR HÄR - Användare trycker på flik "Buy tickets"
    page.get_by_role("link", name="Buy Tickets", exact=True).click()

    page.once("dialog", lambda dialog: dialog.dismiss()) # Biljettyp: vuxen, Ailjettkategori: vanlig, Antal biljetter: 1
    page.get_by_role("button", name="Add to Cart").click() # Användare trycker på knappen "Add to cart" för att lägga till vald biljett i kundvagnen
    page.get_by_role("link", name="Book Safaris").click() # Användare trycker på flik "Book safari" för att boka safarityp
    page.get_by_role("textbox", name="Select Safari Date:").fill("2026-02-18")  #Användare trycker på kalenderikonen och väljer ett datum framåt i tiden i kalender i fältet "Select safari Date"
    page.once("dialog", lambda dialog: dialog.dismiss()) # Användaren väljer den förvalda safaritypen "Herbivore tour" i fältet "Select Safari Type"
    page.get_by_role("button", name="Add to Cart").click() # Användaren trycker på knappen "Add to Cart" för att lägga till bokning av valt datum och vald safarityp

    # Användaren trycker på knappen "Cart"
    page.get_by_role("link", name="Cart").click()
    page.once("dialog", lambda dialog: dialog.dismiss())

    # Resultat: Man ser en överblick med information om tillagda biljetter och bokade safarityper

    # Användaren trycker på knappen "Proceed to checkout" för att fullfölja köpet av innehållet i kundvagnen
    page.get_by_role("button", name="Proceed to Checkout").click()

    # Resultat: Köpet lyckas och går igenom!

    # Användaren trycker på kundvagnen "Cart" igen för att säkerställa att kundvagnen är tom, slut på test
    page.get_by_role("link", name="Cart").click()
    page.once("dialog", lambda dialog: dialog.dismiss())

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
