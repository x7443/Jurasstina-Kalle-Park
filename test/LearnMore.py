import asyncio
import re
from playwright.async_api import Playwright, async_playwright, expect


async def run(playwright: Playwright) -> None:

    browser = await playwright.chromium.launch(headless=False, )
    context = await browser.new_context()
    page = await context.new_page()
    username = "CuloConCaca"
    password = "CacaConCulo"

    await page.goto("http://127.0.0.1:8000/jurap.html")
    await page.get_by_role("link", name="Learn More").click()
    sleep(4)

    # ---------------------
    await context.close()
    await browser.close()


async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())
