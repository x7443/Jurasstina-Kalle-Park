import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("file:///C:/WebTesting/Jurasstina-Kalle-Park/site/jurap.html")
    page.get_by_role("link", name="Home").click()
    page.get_by_role("link", name="Register").click()
    page.get_by_role("link", name="Home").click()
    page.get_by_role("link", name="Register").click()
    page.get_by_role("textbox", name="Username:").click()
    page.get_by_role("textbox", name="Username:").fill("Paco Javi")
    page.get_by_role("textbox", name="Password:").click()
    page.get_by_role("textbox", name="Password:").fill("11111111")
    page.get_by_role("button", name="Register").click()
    page.get_by_role("link", name="Login").click()
    page.get_by_role("textbox", name="Username:").click()
    page.get_by_role("textbox", name="Username:").fill("Paco Javi")
    page.get_by_role("textbox", name="Password:").click()
    page.get_by_role("textbox", name="Password:").fill("11111111")
    page.get_by_role("button", name="Login").click()
