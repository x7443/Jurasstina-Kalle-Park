import asyncio
import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:

    browser =  playwright.chromium.launch(headless=False)
    context =  browser.new_context()
    page =  context.new_page()


    #Öppnar hemsidan
    page.goto("http://127.0.0.1:8000/jurap.html")

    #Registrering (EJ DEL AV TESTET)
    username = "CuloConCaca"
    password = "CacaConCulo"

    page.get_by_role("link", name="Register").click()
    page.get_by_role("textbox", name="Username:").click()
    page.get_by_role("textbox", name="Username:").fill(username)
    page.get_by_role("textbox", name="Username:").press("Tab")
    page.get_by_role("textbox", name="Password:").fill(password)
    page.get_by_role("button", name="Register").click()
    expect(page.get_by_text("Registration successful! Redirecting to login")).to_be_visible()

    #Kollar så att "Register" knappen är gömd (för att säkerhetsställa att användaren är inloggad)
    expect(page.get_by_role("button", name="Register")).to_be_hidden()


    ###HÄR BÖRJAR TESTET###

    #Användaren klickar på "Login"
    page.get_by_role("link", name="Login").click()
    #Kollar efter rubriken "Login" (för att säkerhetsställa att man är på inloggingssidan)
    expect(page.get_by_role("heading", name="Login")).to_be_visible()

    #Loggar in med samma uppgifter som registrerades
    page.get_by_role("textbox", name="Username:").click()
    page.get_by_role("textbox", name="Username:").fill(username)
    page.get_by_role("textbox", name="Password:").click()
    page.get_by_role("textbox", name="Password:").fill(password)
    #Klickar på "Login" knappen (det finns mer än en knapp med texten "Login", därmed används XPath)
    page.locator('//*[@id="login-form"]/button').click()

    #Efter inlogg omdirigeras användaren till huvudsidan

    #Kollar efter rubriken "Welcome to Jurasstina-Kalle Park!" (för att säkerhetsställa att man är på huvudsidan)
    expect(page.get_by_role("heading", name="Welcome to Jurasstina-Kalle Park!")).to_be_visible()


    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
         run(playwright)


