from state import State
class HardwareMenu(State):
    def on_event(self, event):
        if event == 'up':
            :e    #return UnlockedState()
        elif event == 'down':

        elif event == 'left':

        elif event == 'right':
        return self

class LockedState(State):
    def on_event(self, event):
        if event == 'pin_entered':
            return UnlockedState()
        return self
class UnlockedState(State):
    def on_event(self, event):
        if event == 'device_locked':
            return LockedState()
        return self
