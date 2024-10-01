from playwright.async_api import *
import asyncio

parameters = {
    "accept_downloads": True,
}


async def wiki_search():
    async with async_playwright() as p:
        browser = await p.chromium.launch(channel='chrome', headless=False)
        context = await browser.new_context(**parameters)
        page = await context.new_page()

        await page.goto("https://ru.wikipedia.org/")
        wiki_search = page.get_by_label("Искать в Википедии")
        await wiki_search.click()
        await wiki_search.clear()
        await wiki_search.fill("колобок")
        await page.keyboard.press('Enter')

        el = page.locator('.searchmatch').first
        await el.click()

        search_link = page.get_by_text("Весёлых картинок")
        await search_link.click()

        title = page.locator(".mw-page-title-main")
        text_title = await title.text_content()

        if 'журнал' in text_title:
            print(text_title)

        await browser.close()


asyncio.run(wiki_search())
