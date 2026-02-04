import asyncio
import re
from time import sleep
from tkinter import dialog

import dialog
from playwright.async_api import Playwright, async_playwright, expect


async def run(playwright: Playwright) -> None:

    browser = await playwright.chromium.launch(headless=False, )
    context = await browser.new_context()
    page = await context.new_page()
    username = "CuloConCaca"
    password = "CacaConCulo"

    await page.goto("http://127.0.0.1:8000/jurap.html")
    await page.get_by_role("link", name="Login").click()
    await page.get_by_role("link", name="Register").click()
    await page.get_by_role("textbox", name="Username:").click()
    await page.get_by_role("textbox", name="Username:").fill(username)
    await page.get_by_role("textbox", name="Username:").press("Tab")
    await page.get_by_role("textbox", name="Password:").fill(password)
    await page.get_by_role("button", name="Register").click()

    await expect(page.get_by_role("button", name="Register")).to_be_hidden()

    await page.get_by_role("textbox", name="Username:").click()
    await page.get_by_role("textbox", name="Username:").fill(username)
    await page.get_by_role("textbox", name="Password:").click()
    await page.get_by_role("textbox", name="Password:").fill(password)
    await page.locator('//*[@id="login-form"]/button').click()

    await expect(page.get_by_text("Welcome to Jurasstina-Kalle Park!")).to_be_visible()
    await page.get_by_role("link", name="Buy Tickets", exact=True).click()
    await page.get_by_role("spinbutton", name="Quantity:").click()
    await page.get_by_role("spinbutton", name="Quantity:").fill("99999999999999999999999999999999999999999999999")
    await page.get_by_role("button").click()
    await page.wait_for_timeout(2000)
    #page.once("dialog", lambda dialog: dialog.dismiss())
    await page.get_by_role("button", name="Add to Cart").click()
    await page.get_by_role("link", name="Cart").click()
    #page.once("dialog", lambda dialog: dialog.dismiss())
    await page.get_by_role("button", name="Proceed to Checkout").click()
    #sleep(4)

    # ---------------------
    await context.close()
    await browser.close()


async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())
