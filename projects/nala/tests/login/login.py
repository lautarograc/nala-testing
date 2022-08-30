
description = 'Login into the website'


def test(data):
    navigate(data.URL)
    send_keys(('div[data-testid="input-text-controller"]>div[class="MuiInputBase-root MuiOutlinedInput-root MuiInputBase-fullWidth MuiInputBase-formControl"]>input'), data.email_value)
    send_keys(('div[data-testid="password-input-controller"]>input'), data.password_value)
    wait(2)
    click('button[class="MuiButtonBase-root MuiButton-root MuiButton-text sc-bdvvtL dfZNzl submit general sc-eEvSnX YjAsf MuiButton-fullWidth"]')
    wait(5)
    verify_element_displayed('p[class="MuiButtonBase-root MuiButton-root MuiButton-text sc-bdvvtL dfZNzl submit general sc-eEvSnX YjAsf MuiButton-fullWidth"]')
    verify_element_text('p[class="MuiButtonBase-root MuiButton-root MuiButton-text sc-bdvvtL dfZNzl submit general sc-eEvSnX YjAsf MuiButton-fullWidth', data.verify_text)
