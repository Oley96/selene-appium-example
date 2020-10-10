from screens.main_screen import MainScreen


def test_should_add_comment(mobile_driver):
    comment = "Allure Rules!!!"

    MainScreen().tap_and_type_text_to_comment_input(comment)
    MainScreen().tap_to_header()
    MainScreen().tap_submit_button()
    MainScreen().verify_comment_adding(comment)
