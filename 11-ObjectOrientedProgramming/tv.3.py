from tv import TV
def __init__(self):
    self.is_on = False       
    self.channel_no = 1      

def turn_on(self):
    self.is_on = True

    # Metoda do wyłączania TV
def turn_off(self):
    self.is_on = False

    # Metoda do ustawiania kanału (Krok 3)
def set_channel(self, new_channel_no):
    self.channel_no = new_channel_no
    print(f"Kanał zmieniony na {self.channel_no}.")

def show_status(self):
    if self.is_on:
        print(f"TV is on, channel {self.channel_no}")
    else:
        print("TV is off")