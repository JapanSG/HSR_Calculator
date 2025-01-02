# %%
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
def import_stats_as_list(path : str, column : int) -> list:
    '''import stats in specified column as list'''
    column -= 1
    lis = []
    with open(path,"r") as file:
        for _ in range(95):
            line = file.readline()
            i = 0
            num = ""
            for _ in range(column):
                while not line[i].isspace():
                    i += 1
                i += 1
            while not line[i].isspace():
                if line[i].isnumeric() or line[i] == ".":
                    num += line[i]
                i += 1
            lis.append(float(num))
    return lis

def create_graph(x, y, **kwargs) -> None:
    '''create subplot'''
    plt.title(kwargs.get("title", "No title"))
    plt.xlabel("level")
    plt.ylabel("stats")
    plt.plot(x,y,"-")

path = "C:\\Users\\japan\\Downloads\\Baryon stats.txt"
level = import_stats_as_list(path,1)
hp = import_stats_as_list(path, 2)
atk = import_stats_as_list(path,3)
defe = import_stats_as_list(path, 4)
spd = import_stats_as_list(path,5)
effect_hr = import_stats_as_list(path,6)
effect_res = import_stats_as_list(path,7)
create_graph(level,hp)

def fit_expo(x, a, b):
    return a *(np.exp(b*x))

# x = level
# y = hp
# params = curve_fit(fit_expo, x, y)
# new_x = np.linspace(0, 100, num = 500)
# a = params[0][0]
# b = params[0][1]
# print(a)
# print(b)
# print(np.exp(1.1*x))
# # new_y = (np.exp(b*x))
# # plt.plot(new_x ,new_y, "--")
# # plt.show()

#     #Don't use linear interpolation for hp and atk

# %%
