import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False 


def plot_dice(n, epoch, figure):
    plt.figure(figure)
    for i in range(epoch):
        S=[0]
        N=[0]
        X=[]
        for j in range(n):
            val = np.random.randint(low=1, high=7)
            S.append(np.sum(X) + val)
            N.append(N[-1] + 1)
            X.append(val)
        plt.subplot(3, 2, i + 1)
        plt.step(S, N, where='post')
    plt.suptitle('renewal processes under the case of dices')
    plt.show()

def plot_uniform(n, epoch, figure):
    plt.figure(figure)
    for i in range(epoch):
        S=[0.0]
        N=[0] 
        X=[]
        for j in range(n):
            val = np.random.uniform(low=0, high=1.0)
            S.append(np.sum(X) + val)
            N.append(N[-1] + 1)
            X.append(val)
        plt.subplot(3, 2, i + 1)
        plt.step(S, N, where='post')
    
    plt.suptitle('renewal processes under the case of uniform')
    plt.show()

def plot_possion(n, epoch, figure):
    plt.figure(figure)
    for i in range(epoch):
        S=[0.0]
        N=[0]
        X=[]
        for j in range(n):
            val = np.random.exponential(scale=1.0)
            S.append(np.sum(X) + val)
            N.append(N[-1] + 1)
            X.append(val)
        plt.subplot(3, 2, i + 1)
        plt.step(S, N, where='post')
    plt.suptitle('poisson processes')
    plt.show()


if __name__ == "__main__":
    epoch = 5
    n = 10

    plot_dice(n, epoch, figure=1)
    plot_uniform(n, epoch, figure=2)
    plot_possion(n, epoch, figure=3)
    