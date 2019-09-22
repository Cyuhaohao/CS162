class ClockIterator():
    def __init__(self):
        self.hour=0
        self.min=0

    def __getitem__(self, item):
        return self

    def __iter__(self):
        return self

    def __next__(self):
        timelist=[str(int(self.hour) % 24).zfill(2),":",str(int(self.min) % 60).zfill(2)]
        if self.min%60==59:
            self.hour+=1
        self.min+=1
        return ''.join(timelist)

    def __str__(self):
        return self



