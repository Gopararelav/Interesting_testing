import random
import tkinter as tk
window = tk.Tk()
window.title("game of dungeon")
window.geometry("100x120")
window.resizable(False, False)

file = open(r"C:\Users\Lenovo\OneDrive\Desktop\nothing_interesting\game results.txt", "w")
file.write("game started")
while True:
    game = tk.Frame(master=window)
    game.pack()
    you = tk.Frame(master=window)
    you.pack()
    monster_stat = tk.Frame(master=game, background='red')
    monster_stat.pack()
    monster_name = tk.Label(text="beginning", master=monster_stat, background='tomato')
    monster_name.pack()
    monster_life = tk.Label(text="0", master=monster_stat, background='red')
    monster_life.pack()
    life = tk.Label(text=10, master=you, background='green', foreground='white')
    life.pack()


    def koh():
        if monster_name["text"] == "game over":
            pass
        else:
            blocked = random.randint(0, 1)
            deal_damage = random.randint(1, 3)
            you_damage = random.randint(2, 4)
            healing = random.randint(5, 7)
            monster_life["text"] = int(monster_life["text"]) - int(deal_damage)
            file.write("\nmonster damage = " + str(deal_damage))
            if int(life["text"]) <= 0:
                life["text"] = 0
                life["foreground"] = "green"
                monster_name["text"] = "game over"
                monster_life["text"] = 0
                file.write("\ngame over")
            if int(monster_life["text"]) <= 0:
                monster_spawn()
                life["text"] = int(life["text"]) + healing
                file.write("\ndamage healing " + str(healing))
            if blocked == 0:
                life["text"] = int(life["text"]) - you_damage
                file.write("\ntake damage = " + str(you_damage))
            else:
                file.write("\ndamage blocked")


    def monster_spawn():
        if monster_name["text"] == "game over":
            pass
        else:
            go["text"] = "go"
            monster = random.randint(1, 3)
            you_damage = random.randint(2, 4)
            if monster == 2 or 3:
                life["text"] = int(life["text"]) - you_damage
            if monster == 1:
                monster_name["text"] = "nothing"
                monster_life["text"] = '0'
                file.write("\nmonster spawn " + monster_name["text"])
            elif monster == 2:
                monster_name["text"] = "slime"
                monster_life["text"] = "5"
                file.write("\nmonster spawn " + monster_name["text"])
            elif monster == 3:
                monster_name["text"] = "fallen knight"
                monster_life["text"] = "10"
                file.write("\nmonster spawn " + monster_name["text"])
            if int(life["text"]) <= 0:
                life["text"] = 0
                life["foreground"] = "green"
                monster_name["text"] = "game over"
                monster_life["text"] = 0
                file.write("\ngame over")
                file.close()


    go = tk.Button(text="start play", master=you, command=monster_spawn, background="cyan2")
    go.pack()
    attack = tk.Button(text="attack", command=koh, master=you, background='darkred')
    attack.pack()

    window.mainloop()
    file.close()
