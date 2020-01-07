from mycroft import MycroftSkill, intent_file_handler
from mycroft.util import play_audio_file, resolve_resource_file


class EndListeningSound(MycroftSkill):
    def initialize(self):
        self.sound = resolve_resource_file(
            self.config_core.get("sounds").get("end_listening")
        )
        self.log.info(self.sound)
        self.add_event("recognizer_loop:record_end", self.handle_record_end)

    def handle_record_end(self, message):
        try:
            play_audio_file(self.sound)
        except:
            play_audio_file(resolve_resource_file("snd/acknowledge.mp3"))


def create_skill():
    return EndListeningSound()
