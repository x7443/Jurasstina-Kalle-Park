import asyncio
import re
from time import sleep
from tkinter import dialog

import dialog
import pytest
from playwright.async_api import Playwright, async_playwright, expect

async def run(playwright: Playwright) -> None:

    browser = await playwright.chromium.launch(headless=False, )
    context = await browser.new_context()
    page = await context.new_page()

    #Declarerar variablerna för inlogningsuppgifter
    username = "CuloConCaca"
    password = "CacaConCulo"

    #Öppnar hemsidan
    await page.goto("http://127.0.0.1:8000/jurap.html")

    #Användaren klickar på "Register" knappen längst upp i sidan
    await page.get_by_role("link", name="Register").click()

    #Användaren tas vidare till registreringssidan automatiskt

    #Användaren registrerar sig (med de angivna uppgifterna)
    await page.get_by_role("textbox", name="Username:").click()
    await page.get_by_role("textbox", name="Username:").fill(username)
    await page.get_by_role("textbox", name="Username:").press("Tab")
    await page.get_by_role("textbox", name="Password:").fill(password)
    await page.get_by_role("button", name="Register").click()

    #Användaren omdirigeras automatiskt till inloggningssidan

    #Väntar tills "Register" knappen är gömd (för att säkerhetsställa att har blivit omdirigerad)
    await expect(page.get_by_role("button", name="Register")).to_be_hidden()

    # ---------------------
    await context.close()
    await browser.close()


async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())
