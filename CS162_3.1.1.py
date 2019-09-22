class User():
    def __init__(self,name,tag="Student"):
        self.username=name
        self.inclass=False
        self.microphone=False
        self.tag=tag

    def __repr__(self):
        return ("%s is a %s" % (self.username,self.tag))

    def enter_class(self):
        if ~self.inclass:
            self.inclass=True

    def exit_class(self):
        if self.inclass:
            self.inclass=False

    def talk(self):
        if ~self.microphone:
            self.microphone=True


class Teacher(User):
    def __init__(self,name,tag="Teacher"):
        super().__init__(name,tag)

    def start_breakout(self):
        print("You have started a breakout discussion.")


Sterne=Teacher("Sterne")
print(Sterne)
Sterne.start_breakout()

Sterne=User("Sterne")
print(Sterne)
Sterne.start_breakout()