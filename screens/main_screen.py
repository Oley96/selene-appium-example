import os

from selene import by, have
from selene.support.shared.jquery_style import s


class MainScreen:

    def __init__(self):

        if os.getenv('platform.name') == "IOS":
            self.header = s(by.id("h1Text"))
            self.comment_text = s(by.id("submittedComments"))
            self.comment_input = s(by.id("comments"))
            self.submit_button = s(by.id("submit"))

        elif os.getenv('platform.name') == "ANDROID":
            self.header = s(by.id("Heading1_1"))
            self.comment_text = s(by.id("your_comments"))
            self.comment_input = s(by.id("comments"))
            self.submit_button = s(by.id("submit"))

    def tap_and_type_text_to_comment_input(self, comment):
        self.comment_input.click()
        self.comment_input.type(comment)

    def tap_to_header(self):
        self.header.click()

    def tap_submit_button(self):
        self.submit_button.click()

    def verify_comment_adding(self, comment):
        self.comment_text.should(have.text(comment))
