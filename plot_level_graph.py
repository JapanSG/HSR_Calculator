# %%
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np


# def import_stats_as_list(path: str, column: int) -> list:
#     """import stats in specified column as list"""
#     column -= 1
#     lis = []
#     with open(path, "r") as file:
#         for _ in range(95):
#             line = file.readline()
#             i = 0
#             num = ""
#             for _ in range(column):
#                 while not line[i].isspace():
#                     i += 1
#                 i += 1
#             while not line[i].isspace():
#                 if line[i].isnumeric() or line[i] == ".":
#                     num += line[i]
#                 i += 1
#             lis.append(float(num))
#     return lis

# I tried to use this function instead
extracted_data = np.loadtxt(
    "/Users/warissripatoomrak/Downloads/Baryon_stats.txt",
    delimiter="\t",
    usecols=(0, 1),
)

level = extracted_data[:, 0]
hp = extracted_data[:, 1]


# path = "C:\\Users\\japan\\Downloads\\Baryon stats.txt"
# # path = "/Users/warissripatoomrak/Downloads/Baryon_stats.txt"
# level = import_stats_as_list(path, 1)
# hp = import_stats_as_list(path, 2)
# atk = import_stats_as_list(path, 3)
# defe = import_stats_as_list(path, 4)
# spd = import_stats_as_list(path, 5)
# effect_hr = import_stats_as_list(path, 6)
# effect_res = import_stats_as_list(path, 7)


def fit_expo(x, a, b, c):
    # return a * (np.exp(b * x))
    return a * x**b + c


x = level
y = hp

"""
`curve_fit` minimizes the difference between the given data and
the function by adjusting the parameters; it returns 2 values by
default,i.e., `full_output = False`:
    - `popt` (optimized parameters, 1D array)
    - `pcov` (parameter covariance, 2D array)
"""
popt, pcov = curve_fit(fit_expo, x, y)
# new_x = np.linspace(0, 100, num=500)  # No idea what this is

new_y = fit_expo(level, *popt)

# From the fitting function:
a = popt[0]
b = popt[1]
c = popt[2]


# def create_graph(x, y, **kwargs) -> None:
def create_graph(x, y) -> None:
    """create subplot"""
    # plt.title(kwargs.get("title", "Baryon Stats"))
    plt.title("Curve Fitting")
    plt.xlabel("Level")
    plt.ylabel("Stats (HP)")
    plt.scatter(x, y, label="Original", color="black", s=5)
    plt.plot(
        x,
        new_y,  # fitted values of `hp` (y); no need to fit `level` (x)
        label=f"Fitted: y = {popt[0]:.3f}x^2 + {popt[1]:.3f}x + {popt[2]:.3f}",
        color="orange",
    )
    plt.legend()
    plt.grid(True)
    plt.show()


create_graph(level, hp)
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
print("pcov:\n", pcov)
# print(np.exp(1.1 * x))
# # new_y = (np.exp(b*x))
# # plt.plot(new_x ,new_y, "--")
# plt.plot(a, b, ".")

#     #Don't use linear interpolation for hp and atk

# %%
