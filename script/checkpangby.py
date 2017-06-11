# encoding: utf-8
# Belarusian pangram checker by LexArt (http://paet.by), v0.3, oct. 2015

from sys import version_info

py_version = int(version_info[0])
if py_version <= 2:
    from Tkinter import *
else:
    from tkinter import *

class pangcheck():
    def __init__(self):
        example = 'Хоць віжуй, дзе яшчэ быў ёлуп-гусар з німфеткаю!'
        self.charset = 'абвгдеёжзійклмнопрстуўфхцчшыьэюя'
        
        root = Tk()
        root.title('checkpangby')
        root.geometry('390x105+200+200')
        
        line_label = Label(root, text = 'Ваш радок: ')
        line_label.grid(row = 0, column = 0, padx = 5, pady = 5)

        self.line = Entry(root)
        self.line.grid(row = 0, column = 1, padx = 2, sticky = 'ew')
        self.line.insert(0, example)

        scroll = Scrollbar(root, orient = HORIZONTAL)
        scroll.grid(row = 1, column = 1, sticky = 'ew')
        scroll['command'] = self.line.xview
        self.line['xscrollcommand'] = scroll.set

        sender = Button(text = 'Праверыць')
        sender.grid(row = 0, column = 2, padx = 8)

        self.results_label = Label(root, text = 'Вынік: ')
        self.results_label.grid(row = 2, column = 0, columnspan = 3, 
                                padx = 5, pady = 5, sticky = 'ew')

        root.columnconfigure(1, weight = 1)
        sender.bind('<Button-1>', self.pang)
        mainloop()

    def prepare_inp(self):
        if py_version <= 2: 
            userinp = self.line.get().lower().encode('utf-8')
        else: 
            userinp = self.line.get().lower()
        userstring = ''.join(ch for ch in userinp if ch in self.charset)
        if py_version <= 2:
            self.lenstr = len(userstring)/2
            nodup = ''.join([b for a,b in enumerate(userstring.decode('utf-8'))
                              if b not in userstring.decode('utf-8')[:a]])
            sortkey = list(self.charset.decode('utf-8'))
        else:
            self.lenstr = len(userstring)
            nodup = ''.join([b for a,b in enumerate(userstring)
                           if b not in userstring[:a]])
            sortkey = list(self.charset)
        string = ''.join(sorted(nodup, key = sortkey.index))
        return string

    def getdiff(self, charset, mystring):
        diff = [ch for ch in charset if ch not in mystring]
        diffstr = ' '.join(diff)
        lendiff = len(diffstr.replace(' ',''))
        return lendiff, diffstr

    def ispang(self):
        try:
            userstr = self.prepare_inp()
        except:
            return [-1]
        if py_version <= 2:
            lendiff, diffstr = self.getdiff(self.charset.decode('utf-8'), 
                                            userstr)
        else:
            lendiff, diffstr = self.getdiff(self.charset, userstr)
        return [self.lenstr, lendiff, diffstr]

    def pang(self, event):
        checkres = self.ispang()
        if checkres[0] == -1:
            lentext = 'Недапушчальныя сімвалы ў радку'
        else:
            lentext = 'Вынік: у радку '+str(checkres[0])+' літ.\n'
            if checkres[1] == 0:
                lentext += 'Гэта панграма!'
            else:
                lentext += 'Не панграма, няма '+ str(checkres[1])+' літ.\n'
                if py_version <= 2:
                    lentext += checkres[2].encode('utf-8')
                else:
                    lentext += checkres[2]
        self.results_label['text'] = lentext

pangcheck()