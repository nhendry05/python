class Underscore:
    def map(self, iterable, callback):
        y = []
        for x in iterable:
            y.append(callback(x))
        return y
    def find(self, iterable, callback):
        for x in iterable:
            if callback(x):
                return x
    def filter(self, iterable, callback):
        y = []
        for x in iterable:
            if callback(x):
                y.append(x)
        return(y)
    def reject(self, iterable, callback):
        y = []
        for x in iterable:
            if callback(x) == 0:
                y.append(x)
        return(y)

_ = Underscore()
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print(evens)
