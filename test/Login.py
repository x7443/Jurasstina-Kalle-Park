import asyncio
import re
from playwright.async_api import Playwright, async_playwright, expect


async def run(playwright: Playwright) -> None:

    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()


    #Öppnar hemsidan
    await page.goto("http://127.0.0.1:8000/jurap.html")

    #Registrering (EJ DEL AV TESTET)
    username = "CuloConCaca"
    password = "CacaConCulo"

    await page.get_by_role("link", name="Register").click()
    await page.get_by_role("textbox", name="Username:").click()
    await page.get_by_role("textbox", name="Username:").fill(username)
    await page.get_by_role("textbox", name="Username:").press("Tab")
    await page.get_by_role("textbox", name="Password:").fill(password)
    await page.get_by_role("button", name="Register").click()
    await expect(page.get_by_text("Registration successful! Redirecting to login")).to_be_visible()

    #Kollar så att "Register" knappen är gömd (för att säkerhetsställa att användaren är inloggad)
    await expect(page.get_by_role("button", name="Register")).to_be_hidden()


    ###HÄR BÖRJAR TESTET###

    #Användaren klickar på "Login"
    await page.get_by_role("link", name="Login").click()
    #Kollar efter rubriken "Login" (för att säkerhetsställa att man är på inloggingssidan)
    await expect(page.get_by_role("heading", name="Login")).to_be_visible()

    #Loggar in med samma uppgifter som registrerades
    await page.get_by_role("textbox", name="Username:").click()
    await page.get_by_role("textbox", name="Username:").fill(username)
    await page.get_by_role("textbox", name="Password:").click()
    await page.get_by_role("textbox", name="Password:").fill(password)
    #Klickar på "Login" knappen (det finns mer än en knapp med texten "Login", därmed används XPath)
    await page.locator('//*[@id="login-form"]/button').click()

    await expect(page.get_by_role("heading", name="Welcome to Jurasstina-Kalle Park!")).to_be_visible()


    # ---------------------
    await context.close()
    await browser.close()


async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())
