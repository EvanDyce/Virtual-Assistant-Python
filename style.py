import random
import time

import utils


class Style:
    def __init__(self, shell, base_func, params):
        self.shell = shell
        self.base = base_func
        self.params = params
        self.func_dict = {
            'colours': self.list_colours,
            'colors': self.list_colours,
            'background': self.change_background,
            'bg': self.change_background,
            'text': self.change_text,
            'cls': self.clear,
            'clear': self.clear
        }

        self.func_dict[self.base]()

    def change_background(self):
        colour = ''
        for thing in self.params:
            colour += thing + ' '
        colour = colour.strip()

        if colour == 'random':
            index = random.randint(0, len(utils.Utils.COLOURS))
            self.shell['bg'] = utils.Utils.COLOURS[index]

        elif colour in utils.Utils.COLOURS:
            self.shell['bg'] = colour

        elif self.is_hex(colour):
            self.shell['bg'] = colour

        else:
            utils.Utils.error_message(self.shell, 'Please enter a valid colour or hexcode. To view colors try "colours"')

    def is_hex(self, colour):
        letters = '0123456789abcdefABCDEF'
        if colour[0] == '#' and len(colour) == 7:
            for char in colour[1:]:
                if char not in letters:
                    return False
            return True
        return False

    def change_text(self):
        colour = ''
        for thing in self.params:
            colour += thing + ' '
        colour = colour.strip()

        if colour == 'random':
            index = random.randint(0, len(utils.Utils.COLOURS))
            self.shell['fg'] = utils.Utils.COLOURS[index]

        elif colour in utils.Utils.COLOURS:
            self.shell['fg'] = colour

        elif self.is_hex(colour):
            self.shell['fg'] = colour

        else:
            utils.Utils.error_message(self.shell, 'Please enter a valid colour or hexcode. To view colors try "colours"')

    def list_colours(self):
        for colour in utils.Utils.COLOURS:
            self.shell.insert_text(colour)
            self.shell.show_prompt()

    def clear(self):
        self.shell.delete('1.0', 'end')
        self.shell.show_prompt()