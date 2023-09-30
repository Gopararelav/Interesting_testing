import numpy as np


def f(x):
    return 2/(1 + np.exp(-x)) - 1


def df(x):
    return 0.5*(1 + x)*(1 - x)


W1 = np.array(([[-0.2, 0.3, -0.4], [0.1, -0.3, -0.4]]))
W2 = np.array([0.2, 0.3])


def rep(inp):
    sum = np.dot(W1, inp)
    out = np.array([f(x) for x in sum])
    sum = np.dot(W2, out)
    y = f(sum)
    return (y, out)


def tr(epoch):
    global W2, W1
    lmd = 0.01

    N = 10000

    count = len(epoch)

    for k in range(N):
        x = epoch[np.random.randint(0, count)]
        y, out = rep(x[0:3])
        e = y - x[-1]
        delt = e*df(y)
        W2[0] = W2[0] - lmd * delt * out[0]
        W2[1] = W2[1] - lmd * delt * out[1]

        delt2 = W2*delt*df(out)

        W1[0, :] = W1[0, :] - np.array(x[0:3]) * delt2[0] * lmd
        W1[1, :] = W1[1, :] - np.array(x[0:3]) * delt2[1] * lmd


epoch = [(-1, -1, -1, -1),
         (-1, -1, 1, 1),
         (-1, 1, -1, -1),
         (1, -1, -1, -1),
         (1, -1, 1, 1),
         (1, -1, 1, 1),
         (1, 1, -1, -1),
         (1, 1, 1, -1)]

tr(epoch)

for x in epoch:
    y, out = rep(x[0:3])
    print(f"exit НС: {y} => {x[-1]}")
