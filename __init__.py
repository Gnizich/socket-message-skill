from mycroft import MycroftSkill, intent_file_handler


class SocketMessage(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('message.socket.intent')
    def handle_message_socket(self, message):
        self.speak_dialog('message.socket')


def create_skill():
    return SocketMessage()

