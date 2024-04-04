from selene import browser, command, have
import resource

class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, first_name):
        browser.element('#firstName').type(first_name)

    def fill_last_name(self, last_name):
        browser.element('#lastName').type(last_name)

    def fill_email(self, email):
        browser.element('#userEmail').type(email)

    def fill_number(self, number):
        browser.element('#userNumber').type(number)

    def fill_gender(self):
        browser.element('[for="gender-radio-2"]').click()

    def fill_date_birth(self, month, year, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(f'.react-datepicker__day--00{day}').click()

    def fill_subjects(self, value):
        browser.element('#subjectsInput').type(value).press_enter()

    def fill_hobbies(self):
        browser.element('[for="hobbies-checkbox-3"]').click()

    def upload_photo(self, path):
        browser.element('#uploadPicture').send_keys(resource.path(path))

    def fill_address(self, value):
        browser.element('#currentAddress').type(value)

    def fill_state_and_city(self, state, city):
        browser.element('#react-select-3-input').type(state).press_enter()
        browser.element('#react-select-4-input').type(city).press_enter()

    def click_submit(self):
        browser.element('#submit').perform(command.js.scroll_into_view).click()

    def should_have_registered(self, full_name, email, gender, number, date_birth, subjects, hobbies, photo, address,
                               state_city):
        browser.element('.table').all('tr td:nth-child(2)').should(have.texts
            (
            full_name,
            email,
            gender,
            number,
            date_birth,
            subjects,
            hobbies,
            photo,
            address,
            state_city
        ))
