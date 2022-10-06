class Time():

    def __init__(self,time):
        self.time = time

    def  convert_to_minutes(self):
        minutes = self.time//60
        seconds = self.time%60
        return ("{}:{}".format(minutes,seconds)) if minutes!=0 else (seconds)

    def convert_to_hours(self):
        hours = self.time//3600
        minutes = (self.time//60)%60
        seconds = self.time%60
        if hours!=0:
            return "{}:{}:{}".format(hours,minutes,seconds)
        else:
            if minutes!=0:
                return ("{}:{}".format(minutes,seconds))
            else:
                return seconds

t1 = Time(7137)

print(t1.convert_to_minutes())
print(t1.convert_to_hours())