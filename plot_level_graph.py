import matplotlib.pyplot as plt
import numpy as np

def import_stats_as_list(path : str, column : int) -> list:
    '''import stats in specified column as list'''
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
    plt.plot(x,y)
    plt.show()

def main():
    path = "C:\\Users\\japan\\Downloads\\Baryon stats.txt"
    level = import_stats_as_list(path,0)
    hp = import_stats_as_list(path, 1)
    atk = import_stats_as_list(path,2)
    defe = import_stats_as_list(path, 3)
    spd = import_stats_as_list(path,4)
    effect_hr = import_stats_as_list(path,5)
    effect_res = import_stats_as_list(path,6)

    run = True
    while run:
        command = input("Enter command ->").lower()
        if command in "q":
            print("Program End")
            run = False
        elif command == "hp":
            create_graph(level,hp,title = "hp")
        elif command == "atk":
            create_graph(level,atk,title = "atk")
        elif command == "def":
            create_graph(level,defe,title = "def")
        elif command == "spd":
            create_graph(level,spd,title = "spd")
        elif command == "effhr":
            create_graph(level,effect_hr,title = "effect hit rate")
        elif command == "effres":
            create_graph(level,effect_res,title = "effect res")
        elif command == "help":
            print(f"-"*50)
            print(f"list of commands")
            print(f"q : Quit program")
            print(f"hp : View graph of hp stats")
            print(f"atk : View graph of atk stats")
            print(f"def : View graph of def stats")
            print(f"spd : View graph of spd stats")
            print(f"effhr : View graph of effect hit rate stats")
            print(f"effres : View graph of effect res stats")
            print(f"all : View graph of all stats")
            print(f"-"*50)
        elif command == "all":
            x = level
            plt.title("all stats")
            plt.xlabel("level")
            plt.ylabel("stats")
            plt.plot(x,hp, label = "hp")
            plt.plot(x,atk, label = "atk")
            plt.plot(x,defe, label = "def")
            plt.plot(x,spd, label = "spd")
            plt.plot(x,effect_hr, label = "effhr")
            plt.plot(x,effect_res, label = "effres")
            plt.show()
        else:
            print("unknown command")

    #Conclusion Use linear interpolation for unknown stats for specific levels
if __name__ == "__main__":
    main()
