import poplib
import email
import time


class MailHelper:

    def __init__(self, app):
        self.app = app

    def get_mail(self, username, password, subject):
        for i in range(5):
            pop = poplib.POP3(self.app.config['james']['host'])
            pop.user(username)
            pop.pass_(password)
            num = pop.stat()[0]
            if num > 0:
                for n in range(num):
                    message_lines = pop.retr(n+1)[1]
                    message_text = "\n".join(map(lambda x: x.decode('utf8'), message_lines))
                    message = email.message_from_string(message_text)
                    if message.get("Subject") == subject:
                        pop.dele(n+1)
                        pop.quit()
                        return message.get_payload()
            pop.close()
            time.sleep(10)
        return None

