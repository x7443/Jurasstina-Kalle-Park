import re

from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://127.0.0.1:8000/jurap.html")

    page.get_by_role("link", name="Register").click() #Användare klickar på Register
    page.get_by_role("textbox", name="Username:").click() # Användare klickar på fältet "Username"
    page.get_by_role("textbox", name="Username:").fill("User2")# Användare skriver matar in användarnamn
    page.get_by_role("textbox", name="Username:").press("Tab")#Användare tabbar till nästa fält "Password
    page.get_by_role("textbox", name="Password:").fill(">XC>;Ö12")# Användare skapar unikt lösenord
    page.get_by_role("textbox", name="Username:").press("Enter")

    expect(page.get_by_role("heading", name="Login")).to_be_visible()

    page.get_by_role("textbox", name="Username:").click()# Användare klickar på fältet "Username"
    page.get_by_role("textbox", name="Username:").fill("User2") # Användare matar in sitt unikt skapade användarnamn
    page.get_by_role("textbox", name="Password:").click() #Användare klickar på fältet lösenord
    page.get_by_role("textbox", name="Password:").fill("kasmd67896")# Användare matar in fel lösenord
    page.get_by_role("button", name="Login").click()# Användare trycker på knapp "Login"

    expect(page.get_by_text("Invalid username or password.")).to_be_visible()


    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)