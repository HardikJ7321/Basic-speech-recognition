import os
import pyttsx3


class commander:
    def __init__(self):
        self.confirm=["yes", "affirm","si","sure","do it","yeah","confirm"]
        self.cancel=["no","cancel","stop","negative","dont","wait"]

    def discover(self,text):
        if "what" in text and "name" in text:
            if "my" in text:
                self.respond("you havent told me your name yet")
            else:
                self.respond("my name is python commander. How are you ?")

        if "open" or "launch" or "start " in text:
            app = text.split(" ")[-1]
            self.respond("opening "+ app)
            os.system("start "+ app)

    def respond(self,response):
        e = pyttsx3.init()
        e.say(response)
        e.runAndWait()


