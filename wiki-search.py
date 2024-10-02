from playwright.sync_api import Page

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
