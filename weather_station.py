class Observer:
    def update(self, temperature):
        pass

class WeatherStation:
    def __init__(self):
        self.observers = []
        self.temperature = None

    def add_observer(self, observer):
        self.observers.append(observer)

    def set_temperature(self, temperature):
        self.temperature = temperature
        self.notify_observers()

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperature)

class PhoneDisplay(Observer):
    def update(self, temperature):
        print(f"Phone display updated: {temperature}°C")

class DesktopDisplay(Observer):
    def update(self, temperature):
        print(f"Desktop display updated: {temperature}°C")

# Usage
weather_station = WeatherStation()
phone_display = PhoneDisplay()
desktop_display = DesktopDisplay()

weather_station.add_observer(phone_display)
weather_station.add_observer(desktop_display)

weather_station.set_temperature(25)
