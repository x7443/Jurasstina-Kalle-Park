import re

import pytest
from playwright.sync_api import Playwright, sync_playwright, expect

#Test-ID: TC-REG-05-NEG
@pytest.mark.VG_Almedin
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=700)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://127.0.0.1:8000/jurap.html") #Går till hemsidan

    page.get_by_role("link", name="Register").click() #man klickar på register
    page.get_by_role("textbox", name="Username:").click() #Man klickar på fältet användarnamn
    page.get_by_role("textbox", name="Username:").fill("User1") #man matar in fältet username med tecknen "User1"
    page.get_by_role("textbox", name="Username:").press("Tab")#Man tabbar till nästa fält: password
    page.get_by_role("textbox", name="Password:").fill("1234ABCD")#Man skriver in ett lösenord
    page.get_by_role("button", name="Register").click()#Man klickar på knappen "Register" för att registrera sig och vidarebefordras till "Login"

    #Efter registrering hoppar sidan automatiskt till Login sidan

    #Kollar efter "Login" rubriken (för att veta att man är på login sidan)
    expect(page.get_by_role("Heading", name="Login")).to_be_visible()

    ###HÄR BÖRJAR TESTET###

    #Klickar på "Register" fliken igen
    page.get_by_role("link", name="Register").click()# Resten av koden är upprepning av stegen innan
    page.get_by_role("textbox", name="Username:").click()
    page.get_by_role("textbox", name="Username:").fill("User1")
    page.get_by_role("textbox", name="Username:").press("Tab")
    page.get_by_role("textbox", name="Password:").fill("12345ABCDEF")
    page.get_by_role("button", name="Register").click()

    expect(page.get_by_text("Username already exists. Please choose another.")).to_be_visible()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
