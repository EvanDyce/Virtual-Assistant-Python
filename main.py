import tkinter as tk
from shell import Shell


def main():
    root = tk.Tk()
    root.title('Virtual Assistant')
    shell = Shell(root, width=150, height=100)
    shell.pack(fill=tk.BOTH, expand=1)
    root.mainloop()


if __name__ == '__main__':
    main()
