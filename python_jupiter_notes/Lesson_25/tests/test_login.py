def test_incorrect_login(customer_login_page):
    customer_login_page.open_page()
    customer_login_page.fill_login_form('notexistingemail@gmail.com', 'totvac@gmail.com')
    customer_login_page.check_error_message(
        'The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.'
    )


def test_correct_email_with_incorrect_password(customer_login_page):
    customer_login_page.open_page()
    customer_login_page.fill_login_form('totvac@gmail.com', 'totvac@gmail.com')
    customer_login_page.check_error_message(
        'The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.'
    )

# luma1234!
