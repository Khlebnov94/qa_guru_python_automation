from selene import browser, be, have


#browser.open('https://duckduckgo.com/')
#.element('[name="q"]').should(be.blank).type('qa.guru').press_enter()
#browser.element('html').should(have.text('Курсы Тестировщиков - Обучение Тестированию'))

browser.open('https://search.yahoo.com/')
browser.element('[name="p"]').should(be.blank).type('13123123123123131232132123').press_enter()
browser.element('html').should(have.text('We did not find results'))