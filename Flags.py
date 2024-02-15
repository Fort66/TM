class Flags:
    def __init__(self):
        self.addRec = False
        self.delRec = False
        self.editRec = False

    def change_flags(self, flag):
        if flag == 'add':
            self.addRec = True if self.addRec == False else False
        elif flag == 'del':
            self.delRec = True if self.delRec == False else False
        elif flag == 'edit':
            self.editRec = True if self.editRec == False else False