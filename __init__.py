from mycroft import MycroftSkill, intent_file_handler


class EndListeningSound(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('sound.listening.end.intent')
    def handle_sound_listening_end(self, message):
        self.speak_dialog('sound.listening.end')


def create_skill():
    return EndListeningSound()

