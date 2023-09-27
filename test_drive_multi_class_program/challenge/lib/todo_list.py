class TodoList:
    def __init__(self):
        self.todos=[]

    def add(self, todo):
        self.todo=todo
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        self.todos.append(todo)
        return self.todos
    
    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        
        return [todo for todo in self.todos if not self.todo.complete]

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        return [todo for todo in self.todos if self.todo.mark_complete]

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        for todo in self.todos:
            return todo.mark_complete()
        
        