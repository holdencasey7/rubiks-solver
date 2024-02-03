class Moves:
    U = 'u'
    F = 'f'
    L = 'l'
    R = 'r'
    B = 'b'
    D = 'd'
    Uprime = 'up'
    Fprime = 'fp'
    Lprime = 'lp'
    Rprime = 'rp'
    Bprime = 'bp'
    Dprime = 'dp'
    X = 'x'
    Y = 'y'
    Z = 'z'
    Xprime = 'xp'
    Yprime = 'yp'
    Zprime = 'zp'

    TPerm = [R, U, Rprime, Uprime, Rprime, F, R, R, Uprime, Rprime, Uprime, R, U, Rprime, Fprime]
    Sune = [R, U, Rprime, U, R, U, U, Rprime]

    def u(self, state):
        ((u1, u2, u3, u4), (f1, f2, f3, f4), (l1, l2, l3, l4), (r1, r2, r3, r4), (b1, b2, b3, b4), (d1, d2, d3, d4)) = state
        return ((u3, u1, u4, u2), (r1, r2, f3, f4), (f1, f2, l3, l4), (b1, b2, r3, r4), (l1, l2, b3, b4), (d1, d2, d3, d4))
    

    def f(state):
        ((u1, u2, u3, u4), (f1, f2, f3, f4), (l1, l2, l3, l4), (r1, r2, r3, r4), (b1, b2, b3, b4), (d1, d2, d3, d4)) = state
        return ((u1, u2, l4, l2), (f3, f1, f4, f2), (l1, d1, l3, d2), (u3, r2, u4, r4), (b1, b2, b3, b4), (r3, r1, d3, d4))
    

    def l(state):
        ((u1, u2, u3, u4), (f1, f2, f3, f4), (l1, l2, l3, l4), (r1, r2, r3, r4), (b1, b2, b3, b4), (d1, d2, d3, d4)) = state
        return ((b4, u2, b2, u4), (u1, f2, u3, f4), (l3, l1, l4, l2), (r1, r2, r3, r4), (b1, d3, b3, d1), (f1, d2, f3, d4))
    

    def r(state):
        ((u1, u2, u3, u4), (f1, f2, f3, f4), (l1, l2, l3, l4), (r1, r2, r3, r4), (b1, b2, b3, b4), (d1, d2, d3, d4)) = state
        return ((u1, f2, u3, f4), (f1, d2, f3, d4), (l1, l2, l3, l4), (r3, r1, r4, r2), (u4, b2, u2, b4), (d1, b3, d3, b1))
    

    def b(state):
        ((u1, u2, u3, u4), (f1, f2, f3, f4), (l1, l2, l3, l4), (r1, r2, r3, r4), (b1, b2, b3, b4), (d1, d2, d3, d4)) = state
        return ((r2, r4, u3, u4), (f1, f2, f3, f4), (u2, l2, u1, l4), (r1, d4, r3, d3), (b3, b1, b4, b2), (d1, d2, l1, l3))
    

    def d(state):
        ((u1, u2, u3, u4), (f1, f2, f3, f4), (l1, l2, l3, l4), (r1, r2, r3, r4), (b1, b2, b3, b4), (d1, d2, d3, d4)) = state
        return ((u1, u2, u3, u4), (f1, f2, l3, l4), (l1, l2, b3, b4), (r1, r2, f3, f4), (b1, b2, r3, r4), (d3, d1, d4, d2))
    

    def uprime(state):
        return Moves.u(Moves.u(Moves.u(state)))
    

    def fprime(state):
        return Moves.f(Moves.f(Moves.f(state)))
    

    def lprime(state):
        return Moves.l(Moves.l(Moves.l(state)))
    

    def rprime(state):
        return Moves.r(Moves.r(Moves.r(state)))
    

    def bprime(state):
        return Moves.b(Moves.b(Moves.b(state)))
    

    def dprime(state):
        return Moves.d(Moves.d(Moves.d(state)))
    

    # TPerm = [R, U, Rprime, Uprime, Rprime, F, R, R, Uprime, Rprime, Uprime, R, U, Rprime, Fprime]
    def tperm(state):
        return Moves.fprime(Moves.rprime(Moves.u(Moves.r(Moves.uprime(Moves.rprime(Moves.uprime(Moves.r(Moves.r(Moves.f(Moves.rprime(Moves.uprime(Moves.rprime(Moves.u(Moves.r(state)))))))))))))))
    

    # Sune = [R, U, Rprime, U, R, U, U, Rprime]
    def sune(state):
        return Moves.rprime(Moves.u(Moves.u(Moves.r(Moves.u(Moves.rprime(Moves.u(Moves.r(state))))))))
    

    moves = [u, f, l, r, b, d, uprime, fprime, lprime, rprime, bprime, dprime, tperm, sune]
