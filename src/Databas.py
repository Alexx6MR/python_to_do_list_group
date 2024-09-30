import sqlite3



class DatabasManager:
    def __init__(self) -> None:
        self.to_do_connection = sqlite3.connect('todo.db')
        self.to_do_connection.row_factory = sqlite3.Row # Fixar hur man får information från databasen.
        self.cursor = self.to_do_connection.cursor()
        self.create_list()


    def create_list(self) -> None:
        #* Create the task_list Table if not exits
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS task_list(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            task TEXT NOT NULL,
            status BOOLEAN DEFAULT 0,
            FOREIGN KEY (user_id) REFERENCES user(id)
        )
        ''')
        
        
        #* Create the User Table if not exits
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS user(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
        )''')
        self.to_do_connection.commit()

 

    #* USERS FUNKTIONS
    
    
    #* Register a new user
    def register_user(self, username:str, password:str)->int:
        self.cursor.execute('''SELECT * FROM user WHERE username=? AND password=?''', (username, password,))
        existing_user = self.cursor.fetchone()
        
        if(existing_user):
            print()
            print("****Server Response: User already exists***")
            print()
            return 403
        else:
            self.cursor.execute('''INSERT INTO user (username, password) VALUES (?, ?)''', (username, password,))
            self.to_do_connection.commit()
            print(f"user '{username}' successfully registered.")
            return 201
            
            
    #* Login system
    def login_user(self, username:str, password:str)->dict:
        self.cursor.execute('''SELECT * FROM user WHERE username=? AND password=?''', (username, password,))
        existing_user: dict = self.cursor.fetchone()
        
        if existing_user:
            self.to_do_connection.commit()
            return existing_user
        else:
            print()
            print("****Server Response: User don't exists***")
            print()
            return
        
        
        
    
    #* TASK_LIST FUNKTIONS
    
    
      # Choose one task to show
    def get_one_task(self, task_id, user_id) -> dict:
        self.cursor.execute('''SELECT * FROM task_list WHERE id=? AND user_id=?''',(task_id,user_id,))
        task_object: dict = self.cursor.fetchone()
        return task_object

    # returnerar alla tasks som finns i listan och modifierar listan för läsarna så att det blir lättare att läsa
    def get_tasks(self, user_id): 
        self.cursor.execute('''SELECT * from task_list WHERE user_id=?''', (user_id,))
        return self.cursor.fetchall()
    
    
    # Adds a task to current list
    def add_tasks(self, user_id: int, task: str) -> None:
        self.cursor.execute('''INSERT INTO task_list (user_id, task) VALUES (?, ?)''',(user_id, task,)) 
        self.to_do_connection.commit()
        return self.cursor.lastrowid
    
    #* Remove One task
    def remove_task(self, task_id:int, user_id:int) -> None:
        self.cursor.execute('''DELETE FROM task_list WHERE id=? AND user_id=?''',(task_id,user_id,))
        self.to_do_connection.commit()
    
    
    # Pick a task(ID) and update it
    def update_task(self, task_id: int, task: str) -> None:
        self.cursor.execute('''UPDATE task_list SET task=? WHERE id=?''',(task, task_id,))
        self.to_do_connection.commit()

  
    # Update status of the selected task. True/False
    def update_status(self, status: int, task_id: int):
        self.cursor.execute('''UPDATE task_list SET status=? WHERE id=?''',(status, task_id,))
        self.to_do_connection.commit()
        # return self.cursor.lastrowid
        
                
            # Remove a task
    
