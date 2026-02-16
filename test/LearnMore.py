import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:

    browser = playwright.chromium.launch(headless=False, slow_mo=700)
    context = browser.new_context()
    page = context.new_page()


    #Öppnar hemsidan
    page.goto("http://127.0.0.1:8000/jurap.html")

    #Klickar på "Learn more" på "Unlock VIP perks"
    page.locator('//*[@id="home-section"]/div/div[2]/a').click()

    #Användaren tas till "Buy Tickets" sidan

    #Klickar på "Quantity" textboxen och fyller i massa nior och sedan trycker "Add to cart" knappen
    page.get_by_role("spinbutton", name="Quantity:").click()
    page.get_by_role("spinbutton", name="Quantity:").fill("99999999999999999999999999999999999999999999999")
    page.get_by_role("button", name="Add to Cart").click()

    #En dialog poppar upp som säger att man måste vara inloggad för att kunna köpa biljetter

    #Användaren tas till "Login" sidan automatiskt när de klickar på "OK" knappen i dialogen

    #Användaren klickar på "Register" knappen längst upp i sidan och
    #tas vidare till "Register" sidan och registrerar sig (med de angivna uppgifterna)
    username = "CuloConCaca"
    password = "CacaConCulo"

    page.get_by_role("link", name="Register").click()
    page.get_by_role("textbox", name="Username:").click()
    page.get_by_role("textbox", name="Username:").fill(username)
    page.get_by_role("textbox", name="Username:").press("Tab")
    page.get_by_role("textbox", name="Password:").fill(password)
    page.get_by_role("button", name="Register").click()
    expect(page.get_by_text("Registration successful! Redirecting to login")).to_be_visible()

    #Efter registrering blir man automatiskt omdirigerad till inloggningssidan

    #Ser till att knappen "Register" är gömd och "Login" rubriken synlig
    #Detta för att säkerhetsställa att sidan har ändrats
    expect(page.get_by_role("button", name="Register")).to_be_hidden()
    expect(page.get_by_role("heading", name="Login")).to_be_visible()

    #Loggar in med samma uppgifter som registrerades
    page.get_by_role("textbox", name="Username:").click()
    page.get_by_role("textbox", name="Username:").fill(username)
    page.get_by_role("textbox", name="Password:").click()
    page.get_by_role("textbox", name="Password:").fill(password)
    #Klickar på "Login" knappen (det finns mer än en knapp med texten "Login", därmed används XPath)
    page.locator('//*[@id="login-form"]/button').click()

    #Klickar "Buy Tickets" fliken
    page.locator('//*[@id="home-section"]/div/div[2]/a').click()
    # Klickar på "Quantity" textboxen, fyller i massa nior och sedan trycker "Add to cart" knappen
    page.get_by_role("spinbutton", name="Quantity:").click()
    page.get_by_role("spinbutton", name="Quantity:").fill("99999999999999999999999999999999999999999999999")
    page.get_by_role("button", name="Add to Cart").click()
    #Den här gången är användaren inloggad och därmed går det att lägga till i varukorgen

    #Går in på varukorgen och sedan trycker på "Proceed to Checkout" knappen och därmed slutför köpet
    page.get_by_role("link", name="Cart").click()
    page.get_by_role("button", name="Proceed to Checkout").click()

    #Ser till att användaren tas till huvudsidan genom att se till att rubriken
    #"Welcome to Jurasstina-Kalle Park!" är synlig
    expect(page.get_by_role("heading", name="Welcome to Jurasstina-Kalle Park!")).to_be_visible()


    # ---------------------
    context.close()
    browser.close()



with sync_playwright() as playwright:
        run(playwright)


