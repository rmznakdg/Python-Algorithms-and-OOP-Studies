class TodoLogic:
    def __init__(self):
        self.todoList = []
        self.tamamlananlar = []

    def gorev_ekle(self, gorev):
        if gorev:
            self.todoList.append(gorev)
        
    def gorevi_tamamla(self, index):
        if 0 <= index < len(self.todoList):
            tamamlanan = self.todoList.pop(index)
            self.tamamlananlar.append(tamamlanan)
            
    def gorev_sil(self, index):
        if 0 <= index < len(self.todoList):
            self.todoList.pop(index)

    def get_todos(self):
        return self.todoList
        
    def get_completed(self):
        return self.tamamlananlar
