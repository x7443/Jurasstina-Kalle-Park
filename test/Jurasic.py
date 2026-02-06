import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("http://127.0.0.1:8000/jurap.html")
    page.get_by_role("link", name="Register").click()
    page.get_by_role("textbox", name="Username:").click()
    page.get_by_role("textbox", name="Username:").fill("culoconcaca")
    page.get_by_role("textbox", name="Password:").click()
    page.get_by_role("textbox", name="Password:").fill("abc1234567")
    page.get_by_role("button", name="Register").click()
    page.get_by_role("link", name="Login").click()
    page.get_by_role("textbox", name="Username:").click()
    page.get_by_role("textbox", name="Username:").fill("culoconcaca")
    page.get_by_role("textbox", name="Password:").click()
    page.get_by_role("textbox", name="Password:").fill("abc1234567")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("link", name="Buy Tickets", exact=True).click()
    page.get_by_role("spinbutton", name="Quantity:").click()
    page.get_by_role("spinbutton", name="Quantity:").fill("9999999999")
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Add to Cart").click()
    page.get_by_role("link", name="Cart").click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Proceed to Checkout").click()
