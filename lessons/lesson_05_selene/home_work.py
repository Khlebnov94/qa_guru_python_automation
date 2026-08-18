from selene import *

browser.config.driver_name = "firefox"
browser.config.window_width = 1400
browser.config.window_height = 900
browser.open("https://demoqa.com/automation-practice-form")

browser.element("[id=firstName]").should(be.blank).type("Aleksandr")
browser.element("[id=lastName]").should(be.blank).type("Khlebnov")
browser.element("[id=userEmail]").should(be.blank).type("test@mail.ru")
browser.element("[id=gender-radio-1]").click()
browser.element("[id=userNumber]").should(be.blank).type("89055553535")
browser.element("[id=dateOfBirthInput]").click()
browser.element("[class*='month-select']").click()
browser.element('[class$="month-select"]').type('October').click()
browser.element("[class*='year-select']").click()
browser.element('[class$="year-select"]').type('1994').click()
browser.element('[aria-label*="October 19th"]').click()
browser.element('#subjectsInput').type('Maths')
browser.element('[role="option"]').should(have.text('Maths')).click()
browser.element("[id=hobbies-checkbox-3]").click()
browser.element("[id=currentAddress]").should(be.blank).type("Mama City")
browser.element('#state').perform(command.js.scroll_into_view)
browser.element('#state').click()
browser.element('#react-select-3-input').type('Haryana')
browser.element('[role="option"]').should(have.text('Haryana')).click()
browser.element('#react-select-4-input').click()
browser.element('#react-select-4-input').type('Karnal')
browser.element('[role="option"]').should(have.exact_text('Karnal')).click()
browser.element('[id=submit]').click()

browser.element('.table-responsive').should(be.visible)

browser.element('.table-responsive').should(have.text('Aleksandr Khlebnov'))
browser.element('.table-responsive').should(have.text('test@mail.ru'))
browser.element('.table-responsive').should(have.text('Male'))
browser.element('.table-responsive').should(have.text('8905555353'))
browser.element('.table-responsive').should(have.text('19 October,1994'))
browser.element('.table-responsive').should(have.text('Maths'))
browser.element('.table-responsive').should(have.text('Music'))
browser.element('.table-responsive').should(have.text('Mama City'))
browser.element('.table-responsive').should(have.text('Haryana Karnal'))

#breakpoint()