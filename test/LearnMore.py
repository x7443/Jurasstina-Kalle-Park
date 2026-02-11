import asyncio
import re
from playwright.async_api import Playwright, async_playwright, expect


async def run(playwright: Playwright) -> None:

    browser = await playwright.chromium.launch(headless=True)
    context = await browser.new_context()
    page = await context.new_page()


    #Öppnar hemsidan
    await page.goto("http://127.0.0.1:8000/jurap.html")

    #Klickar på "Learn more" på "Unlock VIP perks"
    await page.locator('//*[@id="home-section"]/div/div[2]/a').click()

    #Användaren tas till "Buy Tickets" sidan

    #Klickar på "Quantity" textboxen och fyller i massa nior och sedan trycker "Add to cart" knappen
    await page.get_by_role("spinbutton", name="Quantity:").click()
    await page.get_by_role("spinbutton", name="Quantity:").fill("99999999999999999999999999999999999999999999999")
    await page.get_by_role("button", name="Add to Cart").click()

    #En dialog poppar upp som säger att man måste vara inloggad för att kunna köpa biljetter

    #Användaren tas till "Login" sidan automatiskt när de klickar på "OK" knappen i dialogen

    #Användaren klickar på "Register" knappen längst upp i sidan
    #Tas vidare till "Register" sidan och registrerar sig (med de angivna uppgifterna)
    username = "CuloConCaca"
    password = "CacaConCulo"

    await page.get_by_role("link", name="Register").click()
    await page.get_by_role("textbox", name="Username:").click()
    await page.get_by_role("textbox", name="Username:").fill(username)
    await page.get_by_role("textbox", name="Username:").press("Tab")
    await page.get_by_role("textbox", name="Password:").fill(password)
    await page.get_by_role("button", name="Register").click()
    await expect(page.get_by_text("Registration successful! Redirecting to login")).to_be_visible()

    #Efter registrering blir man automatiskt omdirigerad till inloggningssidan

    #Ser till att knappen "Register" är gömd och "Login" rubriken synlig
    #Detta för att säkerhetsställa att sidan har ändrats
    await expect(page.get_by_role("button", name="Register")).to_be_hidden()
    await expect(page.get_by_role("heading", name="Login")).to_be_visible()

    #Loggar in med samma uppgifter som registrerades
    await page.get_by_role("textbox", name="Username:").click()
    await page.get_by_role("textbox", name="Username:").fill(username)
    await page.get_by_role("textbox", name="Password:").click()
    await page.get_by_role("textbox", name="Password:").fill(password)
    #Klickar på "Login" knappen (det finns mer än en knapp med texten "Login", därmed används XPath)
    await page.locator('//*[@id="login-form"]/button').click()

    #Klickar "Buy Tickets" fliken
    await page.locator('//*[@id="home-section"]/div/div[2]/a').click()
    # Klickar på "Quantity" textboxen, fyller i massa nior och sedan trycker "Add to cart" knappen
    await page.get_by_role("spinbutton", name="Quantity:").click()
    await page.get_by_role("spinbutton", name="Quantity:").fill("99999999999999999999999999999999999999999999999")
    await page.get_by_role("button", name="Add to Cart").click()
    #Den här gången är användaren inloggad och därmed går det att lägga till i varukorgen

    #Går in på varukorgen och sedan trycker på "Proceed to Checkout" knappen och därmed slutför köpet
    await page.get_by_role("link", name="Cart").click()
    await page.get_by_role("button", name="Proceed to Checkout").click()

    #Ser till att användaren tas till huvudsidan genom att se till att rubriken
    #"Welcome to Jurasstina-Kalle Park!" är synlig
    await expect(page.get_by_role("heading", name="Welcome to Jurasstina-Kalle Park!")).to_be_visible()


    # ---------------------
    await context.close()
    await browser.close()


async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())
