class Tv:

    def __init__(self):
        self.setChannal = 0
        self.volume = 0

    def setcanal(self, new_channal):
        self.setChannal = new_channal
        if 100 >= new_channal > 0:
            return self.setChannal

    def turn_up(self, up_volume):
        self.volume = up_volume
        if up_volume < 100:
            up_volume += 1
        else:
            print('\033[31mMaximum volume - 100\033[m')

    def turn_down(self, down_volume):
        if down_volume > 0:
            self.volume -= down_volume
        else:
            print('\033[31mMinimum volume - 0\033[m')

    def show_mood(self):
        print(f'Channel: {self.setChannal} \nVolume: {self.volume}')


tv = Tv()
tv.show_mood()
print()

tv.setcanal(50)
tv.show_mood()
print()

tv.turn_up(60)
tv.show_mood()
print()

tv.turn_down(10)
tv.show_mood()
