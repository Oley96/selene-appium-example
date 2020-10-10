from selene import by
from selene.support.shared.jquery_style import s


def test_appium_open_app(mobile_driver):
    comment = "Allure Rules!!!"

    s(by.id("comments")).click()
    s(by.id("comments")).set_value(comment)
    s(by.id("h1Text")).click()
    s(by.id("submit")).click()
    s(by.id("submittedComments")).click()
