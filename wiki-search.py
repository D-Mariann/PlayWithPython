from playwright.async_api import *
import asyncio

from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://ru.wikipedia.org/")
    wiki_search = page.get_by_label("Искать в Википедии")
    wiki_search.click()
    wiki_search.clear()
    wiki_search.fill("колобок")
    page.keyboard.press('Enter')

    el = page.locator('.searchmatch').first
    el.click()

    search_link = page.get_by_text("Весёлых картинок")
    search_link.click()

    title = page.locator(".mw-page-title-main")
    text_title = title.text_content()

    assert 'журнал' in text_title

    page.close()



# parameters = {
#     "accept_downloads": True,
# }
#
# def test_wiki_search():
#     # with async_playwright() as p:
#         browser = chromium.launch(channel='chrome',headless=False)
#         context = browser.new_context(**parameters)
#         page = context.new_page()
#
#         page.goto("https://ru.wikipedia.org/")
#         wiki_search = page.get_by_label("Искать в Википедии")
#         wiki_search.click()
#         wiki_search.clear()
#         wiki_search.fill("колобок")
#         page.keyboard.press('Enter')
#
#         el = page.locator('.searchmatch').first
#         el.click()
#
#         search_link = page.get_by_text("Весёлых картинок")
#         search_link.click()
#
#         title = page.locator(".mw-page-title-main")
#         text_title = title.text_content()
#
#         # if 'журнал' in text_title:
#         #     print(text_title)
#         assert 'журнал' in text_title
#         # await expect(page.locator(".mw-page-title-main")).to_have_text("Весёлые картинки (журнал)")
#         browser.close()