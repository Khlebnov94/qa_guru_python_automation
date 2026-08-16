from selene import browser, be, have


def test_search():
    browser.open('https://search.brave.com/')

    browser.element('[name="q"]').should(be.blank).type('qa.guru').press_enter()

    browser.element('body').should(
        have.text('qa.guru')
    )


def test_search_no_results():
    browser.open('https://search.brave.com/')

    browser.element('[name="q"]').should(be.blank).type(
        'No results found'
    ).press_enter()

    browser.element('body').should(
        have.text('No results found')
    )