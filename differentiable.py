# numerical differentiation for any variable
class differentiable:
    def __init__(self, value=0, backup=3) -> None:
        self._value = value
        if backup:
            self.diffrentiability = True
            self.prev_value = differentiable(0, backup=(backup-1))
        else:
            self.diffrentiability = False
    def diff(self,dt):
        return (self._value - self.prev_value._value)/dt
    def ddiff(self,dt):
        return (self.diff(dt) - self.prev_value.diff(dt))/dt
    def dddiff(self,dt):
        return (self.ddiff(dt) - self.prev_value.ddiff(dt))/dt
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, value):
        self.prev_value._value = self._value
        self._value = value

if __name__=="__main__":
    print("differntialbe class example")
    a = differentiable(0)
    a.value = 1
    print(a.value)
    print(a.diff(1))
    a.value = 2
    print(a.value)
    print(a.diff(1))
    print(a.ddiff(1))
    a.value = 4
    print(a.value)
    print(a.diff(1))
    print(a.ddiff(1))
    print(a.dddiff(1))

