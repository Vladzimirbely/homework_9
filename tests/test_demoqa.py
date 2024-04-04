from pages.registration_page import RegistrationPage

def test_enter_data():
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.fill_first_name('first name')
    registration_page.fill_last_name('last name')
    registration_page.fill_email('test@test.test')
    registration_page.fill_number('1234567890')
    registration_page.fill_gender()
    registration_page.fill_date_birth('March', 1998, 2)
    registration_page.fill_subjects('Computer Science')
    registration_page.fill_hobbies()
    registration_page.upload_photo('Screenshot_1.png')
    registration_page.fill_address('Address')
    registration_page.fill_state_and_city('Haryana', 'Karnal')
    registration_page.click_submit()

    registration_page.should_have_registered(
        'first name last name',
        'test@test.test',
        'Female',
        '1234567890',
        '02 March,1998',
        'Computer Science',
        'Music',
        'Screenshot_1.png',
        'Address',
        'Haryana Karnal'
    )
