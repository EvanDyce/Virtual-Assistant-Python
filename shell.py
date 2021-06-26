import tkinter as tk

from utils import Utils


class Shell(tk.Text):
    def __init__(self, parent, **kwargs):
        tk.Text.__init__(self)
        # when a key is pressed on_key_pressed is called with the key
        self.bind('<Key>', self.on_key_pressed)
        # tracks the last command entered
        self.cmd = None
        # inits the local classes
        self.input = Input(self)
        self.show_prompt()

    def show_prompt(self):
        """ inserts >> on a new line and updates the insert mark to the new EOF """
        # inserts the >> at start of line
        self.insert_text('>> ', end='')
        # updates the insert constant to the end of the prompt
        self.mark_set(tk.INSERT, tk.END)
        # sets the cursor at the insert insert constant
        self.cursor = self.index(tk.INSERT)

    def insert_text(self, txt='', end='\n'):
        """ inserts the txt param at the bottom of the shell """
        # inserts the text input to the end (bottom) of the text box
        self.insert(tk.END, txt + end)
        # makes sure that the end is visible, not out of text box view
        self.see(tk.END)

    def on_key_pressed(self, event):
        """ determines what happens when keys are pressed"""
        key_symbol = event.keysym

        if key_symbol == 'Up':
            # if the previous command exists
            if self.cmd:
                # delete the whole thing? and rewrite the old one?
                self.delete(self.cursor, tk.END)
                self.insert(self.cursor, self.cmd)
            return "break"

        if key_symbol == 'Down':
            return "break"

        if key_symbol in ('Left', 'BackSpace'):
            current = self.index(tk.INSERT)
            if self.compare(current, '==', self.cursor):
                return 'break'

        if key_symbol == 'Return':
            cmd = self.get(self.cursor, tk.END).strip()
            self.input.raw_input(cmd)
            self.insert_text()
            self.show_prompt()
            self.cmd = cmd
            return 'break'

        if key_symbol == 'Escape':
            self.master.destroy()


class Input:
    def __init__(self, shell):
        self.shell = shell
        self.base = None

    def raw_input(self, raw_command):
        if len(raw_command) == 0 or raw_command.isspace():
            #TODO add utils error message default
            return

        # splits the input into a list
        with_whitespace = raw_command.strip().split(' ')
        # removes the extra whitespace in the list
        inputs_list = [word for word in with_whitespace if word != '']
        # gets the base command
        self.base = inputs_list[0]

        if self.base == 'help':
            Utils.help(self.shell)
            return

        # checks if the base function is a valid one by iterating through the function list
        for i in range(len(Utils.FUNCTION_LIST)):
            if self.base in Utils.FUNCTION_LIST[i]:
                # instantiates the new object of whatever type matches the command put in
                # passes the shell, the base, and the rest of the parameters if there are any
                Utils.CLASS_STRING_TO_CLASS_OBJECT[Utils.CLASS_LIST[i]](self.shell, self.base, inputs_list[1:])
                return

        Utils.error_message(self.shell, f'{self.base} is not a valid command. To view a list of commands type "help"')


