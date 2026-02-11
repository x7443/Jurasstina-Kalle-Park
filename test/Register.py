import re
from time import sleep
from tkinter import dialog

import dialog
import pytest
from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:

    browser = playwright.chromium.launch(headless=False, )
    context = browser.new_context()
    page = context.new_page()

    #Declarerar variablerna för inlogningsuppgifter
    username = "CuloConCaca"
    password = "CacaConCulo"

    #Öppnar hemsidan
    page.goto("http://127.0.0.1:8000/jurap.html")

    #Användaren klickar på "Register" knappen längst upp i sidan
    page.get_by_role("link", name="Register").click()

    #Användaren tas vidare till registreringssidan automatiskt

    #Användaren registrerar sig (med de angivna uppgifterna)
    page.get_by_role("textbox", name="Username:").click()
    page.get_by_role("textbox", name="Username:").fill(username)
    page.get_by_role("textbox", name="Username:").press("Tab")
    page.get_by_role("textbox", name="Password:").fill(password)
    page.get_by_role("button", name="Register").click()

    #Användaren omdirigeras automatiskt till inloggningssidan

    #Väntar tills "Register" knappen är gömd (för att säkerhetsställa att har blivit omdirigerad)
    expect(page.get_by_role("button", name="Register")).to_be_hidden()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
        run(playwright)


