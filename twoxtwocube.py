class Moves:
    def u(state):
        ((u1, u2, u3, u4), (f1, f2, f3, f4), (l1, l2, l3, l4), (r1, r2, r3, r4), (b1, b2, b3, b4), (d1, d2, d3, d4)) = state
        return ((u3, u1, u4, u2), (r1, r2, f3, f4), (f1, f2, l3, l4), (b1, b2, r3, r4), (l1, l2, b3, b4), (d1, d2, d3, d4))
    u.__name__ = 'U'
    

    def f(state):
        ((u1, u2, u3, u4), (f1, f2, f3, f4), (l1, l2, l3, l4), (r1, r2, r3, r4), (b1, b2, b3, b4), (d1, d2, d3, d4)) = state
        return ((u1, u2, l4, l2), (f3, f1, f4, f2), (l1, d1, l3, d2), (u3, r2, u4, r4), (b1, b2, b3, b4), (r3, r1, d3, d4))
    f.__name__ = 'F'
    

    def l(state):
        ((u1, u2, u3, u4), (f1, f2, f3, f4), (l1, l2, l3, l4), (r1, r2, r3, r4), (b1, b2, b3, b4), (d1, d2, d3, d4)) = state
        return ((b4, u2, b2, u4), (u1, f2, u3, f4), (l3, l1, l4, l2), (r1, r2, r3, r4), (b1, d3, b3, d1), (f1, d2, f3, d4))
    l.__name__ = 'L'
    

    def r(state):
        ((u1, u2, u3, u4), (f1, f2, f3, f4), (l1, l2, l3, l4), (r1, r2, r3, r4), (b1, b2, b3, b4), (d1, d2, d3, d4)) = state
        return ((u1, f2, u3, f4), (f1, d2, f3, d4), (l1, l2, l3, l4), (r3, r1, r4, r2), (u4, b2, u2, b4), (d1, b3, d3, b1))
    r.__name__ = 'R'
    

    def b(state):
        ((u1, u2, u3, u4), (f1, f2, f3, f4), (l1, l2, l3, l4), (r1, r2, r3, r4), (b1, b2, b3, b4), (d1, d2, d3, d4)) = state
        return ((r2, r4, u3, u4), (f1, f2, f3, f4), (u2, l2, u1, l4), (r1, d4, r3, d3), (b3, b1, b4, b2), (d1, d2, l1, l3))
    b.__name__ = 'B'
    

    def d(state):
        ((u1, u2, u3, u4), (f1, f2, f3, f4), (l1, l2, l3, l4), (r1, r2, r3, r4), (b1, b2, b3, b4), (d1, d2, d3, d4)) = state
        return ((u1, u2, u3, u4), (f1, f2, l3, l4), (l1, l2, b3, b4), (r1, r2, f3, f4), (b1, b2, r3, r4), (d3, d1, d4, d2))
    d.__name__ = 'D'
    

    def uprime(state):
        return Moves.u(Moves.u(Moves.u(state)))
    uprime.__name__ = "Uprime"
    

    def fprime(state):
        return Moves.f(Moves.f(Moves.f(state)))
    fprime.__name__ = "Fprime"
    

    def lprime(state):
        return Moves.l(Moves.l(Moves.l(state)))
    lprime.__name__ = "Lprime"
    

    def rprime(state):
        return Moves.r(Moves.r(Moves.r(state)))
    rprime.__name__ = "Rprime"
    

    def bprime(state):
        return Moves.b(Moves.b(Moves.b(state)))
    bprime.__name__ = "Bprime"
    

    def dprime(state):
        return Moves.d(Moves.d(Moves.d(state)))
    dprime.__name__ = "Dprime"
    

    # TPerm = [R, U, Rprime, Uprime, Rprime, F, R, R, Uprime, Rprime, Uprime, R, U, Rprime, Fprime]
    def tperm(state):
        return Moves.fprime(Moves.rprime(Moves.u(Moves.r(Moves.uprime(Moves.rprime(Moves.uprime(Moves.r(Moves.r(Moves.f(Moves.rprime(Moves.uprime(Moves.rprime(Moves.u(Moves.r(state)))))))))))))))
    tperm.__name__ = "TPerm"


    # Sune = [R, U, Rprime, U, R, U, U, Rprime]
    def sune(state):
        return Moves.rprime(Moves.u(Moves.u(Moves.r(Moves.u(Moves.rprime(Moves.u(Moves.r(state))))))))
    sune.__name__ = "Sune"

    # SunePrime = [R, U, U, Rprime, Uprime, R, Uprime, Rprime]
    def sunePrime(state):
        return Moves.rprime(Moves.uprime(Moves.r(Moves.uprime(Moves.rprime(Moves.u(Moves.u(Moves.r(state))))))))
    sunePrime.__name__ = "SunePrime"
    

    def x(state):
        return Moves.r(Moves.lprime(state))
    x.__name__ = "X"
    

    def y(state):
        return Moves.u(Moves.dprime(state))
    y.__name__ = "Y"
    

    def z(state):
        return Moves.f(Moves.bprime(state))
    z.__name__ = "Z"
    

    def xprime(state):
        return Moves.x(Moves.x(Moves.x(state)))
    xprime.__name__ = "Xprime"
    

    def yprime(state):
        return Moves.y(Moves.y(Moves.y(state)))
    yprime.__name__ = "Yprime"
    

    def zprime(state):
        return Moves.z(Moves.z(Moves.z(state)))
    zprime.__name__ = "Zprime"
    

    moves = [u, f, l, r, b, d, uprime, fprime, lprime, rprime, bprime, dprime, tperm, sune, sunePrime, x, y, z, xprime, yprime, zprime]
    costs = {u:1, f:1, l:1, r:1, b:1, d:1, uprime:1, fprime:1, lprime:1, rprime:1, bprime:1, dprime:1, tperm:15, sune:8, sunePrime:8, x:1, y:1, z:1, xprime:1, yprime:1, zprime:1}


class Agent:
    def __init__(self):
        return

    def getActions(self, state):
        return
    

class Problem:
    def getStartState(self):
        return

    def isGoalState(self, state):
        return

    def getSuccessors(self, state):
        return

    def getCostOfActions(self, actions):
        return