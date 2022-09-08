
description = 'Login into the website'

pages = ['keys',
         'home',
         'buttons']


def test(data):
    navigate(data.URL)
    send_keys(keys.email_key, data.email_value)
    send_keys(keys.password_key, data.password_value)
    wait(2)
    click(buttons.submit_sign_in)
    wait(15)
    verify_element_displayed('/html/body/div/div[1]/main/div/div/div[1]/div/div[3]/div[2]/div/div/div[9]/table/tr[2]/td[5]')
    verify_element_text(('//*[@id="root"]/div[1]/main/div/p'), data.verify_text)
