class Vector(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __add__(self, v):
        self.x += v.x
        self.y += v.y
        return self

    def __sub__(self, v):
        self.x = self.x - v.x
        self.y = self.y - v.y
        return self
    
    def __mul__(self, v):
        return self.x * v.x + self.y * v.y

    def __rmul__(self, x):
        self.x *= x
        self.y *= x
        return self

    def __repr__(self):
        return "Vector x=%s y=%s" % (str(self.x), str(self.y))

    def norm(self):
        return (self.x**2 + self.y**2)**0.5

    def normalize(self):
        n = self.norm()
        self.x /= n
        self.y /= n
        return self

def problem244():
    last_two = [(0.0, 10.1), (1.4, -9.6)]
    x, y = last_two[1]
    i = 1
    while not (-0.01 <= x <= 0.01 and y > 9.):
        u = Vector(last_two[0][0] - x, last_two[0][1] - y)
        n = Vector(4.*x/y, 1.).normalize()
        v = (2.*(u*n))*n - u
        l = -(8.*x*n.x + 2.*y*n.y)/(4*n.x**2+n.y**2)
        x, y = x + l*n.x, y + l*n.y
        last_two.pop(0)
        last_two.append((x,y))
        i += 1
    return i-1

print problem244()
