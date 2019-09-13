import numpy as np
import visdom

def plot_wlln(n, expect=0.25):
    exper = []
    num_exper = 10000
    for i in range(num_exper):
        rvs = []
        for j in range(n):
            rv = np.random.binomial(1, 0.25)
            rvs.append(rv)
        s_n = np.sum(rvs)
        exper.append((s_n - n * expect) / n)
    
    exper = np.asarray(exper)
    indicies = []
    cdf = []
    for i in range(n):
        x = -0.25 + i * (1 / n)
        if i > 0:
            indicies.append(indicies[-1])
            cdf.append(np.sum(exper < x) / num_exper)
        indicies.append(x)
        cdf.append(np.sum(exper < x) / num_exper)
    indicies.append(indicies[-1])
    x = 0.6
    indicies.append(x)
    cdf.append(np.sum(exper < x) / num_exper)
    cdf.append(np.sum(exper < x) / num_exper)


    return indicies, cdf

def plot_clt(n, x_list, expect=0.25):
    exper = []
    num_exper = 10000
    for i in range(num_exper):
        rvs = []
        for j in range(n):
            rv = np.random.binomial(1, 0.25)
            rvs.append(rv)
        s_n = np.sum(rvs)
        exper.append((s_n - n * expect) / np.sqrt(n))
    
    exper = np.asarray(exper)
    indicies = []
    cdf = []
    for i, x in enumerate(x_list):
        if i > 0:
            indicies.append(indicies[-1])
            cdf.append(np.sum(exper < x) / num_exper)
        indicies.append(x)
        cdf.append(np.sum(exper < x) / num_exper)
    #indicies.append(indicies[-1])

    return indicies, cdf

if __name__ == '__main__':
    vis = visdom.Visdom(env="SP_Plot1")
    n_lsit = [4, 20, 50]
    for n in n_lsit:
        indicies, cdf = plot_wlln(n)
        vis.line(cdf, indicies, name='n={}'.format(n), win='WLLN', opts=dict(showlegend=True, xlabel='Y_n=[S_n-E(S_n)]/n', ylabel='F_(Y_n)', xtickmin=-0.4, xtickmax=0.6, ytickmin=0.0, ytickmax=1.0,ytickstep=0.1), update='append')

    vis.close()

    vis = visdom.Visdom(env='SP_Plot2')
    x_4 = [-0.5, 0, 0.5, 1, 1.5]
    x_20 = [-1.2 + i * 0.24 for i in range(12)]
    x_50 = [-1.5 + i * 0.15 for i in range(20)]
    x_lists = [x_4, x_20, x_50]
    for n, x_list in zip(n_lsit, x_lists):
        indicies, cdf = plot_clt(n, x_list)
        vis.line(cdf, indicies, name='n={}'.format(n), win='CLT', opts=dict(showlegend=True, xlabel='Z_n=[S_n-E(S_n)]/sqrt(n)', ylabel='F_(Z_n)', xtickmin=-1.5, xtickmax=1.5, ytickstep=0.1), update='append')
    
    vis.close()
    
    