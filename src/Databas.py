import sqlite3

# Saker att fixa:
# Skapa funktion kontrollera om det finns en databas. om finns koppla. om inte finns, skapa en ny. KLAR
# Boolean complete task. skapa en variabel som kontrollerar om tasken är true/false.
# Skriv en funktion för att uppdatera en task. Kunna välj en task och sen uppdatera den. KLAR
# Skapa en funktion Get_one_task genom ID. Funktionen ska returnera en task_object. KLAR
# Typa alla funktioner. KLAR

    # Create connection to database called todo.db
class databasmanager:
    def __init__(self) -> None:
        self.to_do_connection = sqlite3.connect('todo.db')
        self.to_do_connection.row_factory = sqlite3.Row # Fixar hur man får information från databasen.
        self.cursor = self.to_do_connection.cursor()
        self.create_list()

    # Create a task list if there is none.
    # Creates a table with ID, task and status.
    def create_list(self) -> None:
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS task_list(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL,
        status BOOLEAN DEFAULT 0
        );''')
        self.to_do_connection.commit()

    # Adds a task to current list
    def add_tasks(self,task: str) -> None:
        self.cursor.execute("INSERT INTO task_list (task) VALUES (?)",(task,)) 
        self.to_do_connection.commit() # commit så att ändringen spara i databasen.

    
    # Remove a task
    def remove_task(self, task_id) -> None:
        self.cursor.execute('''DELETE FROM task_list WHERE id=?;
        ''',(task_id,))
        self.to_do_connection.commit()

    # Pick a task(ID) and update it
    def update_task(self, task_id: int, task: str) -> None:
        self.cursor.execute('''UPDATE task_list SET task=? WHERE id=?;
        ''',(task, task_id))
        self.to_do_connection.commit()

    # Choose one task to show
    def get_one_task(self, task_id) -> dict:
        self.cursor.execute('''SELECT * FROM task_list WHERE id=?;
        ''',(task_id,))
        task_object: dict = self.cursor.fetchone()
        return task_object

    def get_tasks(self): # returnerar alla tasks som finns i listan och modifierar listan för läsarna så att det blir lättare att läsa
        self.cursor.execute("SELECT * from task_list")
        return self.cursor.fetchall()
    
    # Update status of the selected task. True/False
    def update_status(self, status: int, task_id: int):
        self.cursor.execute('''UPDATE task_list SET status=? WHERE id=?;
        ''',(status, task_id))
        self.to_do_connection.commit()


    # Show all the current tasks
    def show_tasks(self, task_list: list) -> None:
        for task in task_list:
            print(f"Id: {task["id"]}, Uppgift: {task["task"]}, Status: {bool(task["status"])}")
        

todo_manager = databasmanager()
#todo_manager.add_tasks('Hejhejhej')

# print out all data from task_list
# new_task = input("Task: ")
# todo_manager.add_tasks(new_task)

#todo_manager.show_tasks()
    
#todo_manager.update_task(task_id =2 , task = "Alexei")
#todo_manager.remove_task(task_id=1)
#todo_manager.show_tasks()
#new_task = todo_manager.get_one_task(task_id=8)
#todo_manager.show_tasks(task_list=[todo_manager.get_one_task(task_id=1)])
#todo_manager.update_status(task_id=1, status=0)
#todo_manager.show_tasks(task_list=[todo_manager.get_one_task(task_id=1)])