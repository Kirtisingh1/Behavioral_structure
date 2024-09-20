class TV:
    def turn_on(self):
        print("TV is now ON.")

    def turn_off(self):
        print("TV is now OFF.")

class Command:
    def execute(self):
        pass

class TurnOnCommand(Command):
    def __init__(self, tv):
        self.tv = tv

    def execute(self):
        self.tv.turn_on()

class TurnOffCommand(Command):
    def __init__(self, tv):
        self.tv = tv

    def execute(self):
        self.tv.turn_off()

class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        self.command.execute()

# Usage
tv = TV()
remote = RemoteControl()

turn_on = TurnOnCommand(tv)
turn_off = TurnOffCommand(tv)

remote.set_command(turn_on)
remote.press_button()

remote.set_command(turn_off)
remote.press_button()

