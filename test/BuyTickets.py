import re
from time import sleep
from tkinter import dialog

import dialog
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:

    browser = playwright.chromium.launch(headless=False, slow_mo=700)
    context = browser.new_context()
    page = context.new_page()
    username = "CuloConCaca"
    password = "CacaConCulo"

    page.goto("http://127.0.0.1:8000/jurap.html")
    page.get_by_role("link", name="Login").click()
    page.get_by_role("link", name="Register").click()
    page.get_by_role("textbox", name="Username:").click()
    page.get_by_role("textbox", name="Username:").fill(username)
    page.get_by_role("textbox", name="Username:").press("Tab")
    page.get_by_role("textbox", name="Password:").fill(password)
    page.get_by_role("button", name="Register").click()

    expect(page.get_by_role("button", name="Register")).to_be_hidden()

    page.get_by_role("textbox", name="Username:").click()
    page.get_by_role("textbox", name="Username:").fill(username)
    page.get_by_role("textbox", name="Password:").click()
    page.get_by_role("textbox", name="Password:").fill(password)
    page.locator('//*[@id="login-form"]/button').click()

    expect(page.get_by_text("Welcome to Jurasstina-Kalle Park!")).to_be_visible()
    page.get_by_role("link", name="Buy Tickets", exact=True).click()
    page.get_by_role("spinbutton", name="Quantity:").click()
    page.get_by_role("spinbutton", name="Quantity:").fill("99999999999999999999999999999999999999999999999")
    page.get_by_role("button").click()
    page.wait_for_timeout(2000)
    #page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Add to Cart").click()
    page.get_by_role("link", name="Cart").click()
    #page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Proceed to Checkout").click()
    #sleep(4)

    # ---------------------
    context.close()
    browser.close()



with sync_playwright() as playwright:
        run(playwright)


