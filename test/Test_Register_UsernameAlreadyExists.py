import re

import pytest
from playwright.sync_api import Playwright, sync_playwright, expect

@pytest.mark.VG_Almedin
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://127.0.0.1:8000/jurap.html") #Går till hemsidan
    page.get_by_role("link", name="Register").click() #man klickar på register
    page.get_by_role("textbox", name="Username:").click() #Man klickar på fältet användarnamn
    page.get_by_role("textbox", name="Username:").fill("User1") #man matar in fältet username med tecknen "User1"
    page.get_by_role("textbox", name="Username:").press("Tab")#Man tabbar till nästa fält: password
    page.get_by_role("textbox", name="Password:").fill("1234ABCD")#Man skriver in ett lösenord
    page.get_by_role("button", name="Register").click()#Man klickar på knappen "Register" för att registrera sig och vidarebefordras till "Login"
    page.get_by_role("link", name="Register").click()# Resten av koden är upprepning av stegen innan
    page.get_by_role("textbox", name="Username:").click()
    page.get_by_role("textbox", name="Username:").fill("User1")
    page.get_by_role("textbox", name="Username:").press("Tab")
    page.get_by_role("textbox", name="Password:").fill("12345ABCDEF")
    page.get_by_role("button", name="Register").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
