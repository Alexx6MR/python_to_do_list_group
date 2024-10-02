import sqlite3
from src.log import FileLogger


class DatabasManager:
    def __init__(self) -> None:
        self.to_do_connection = sqlite3.connect('todo.db')
        self.to_do_connection.row_factory = sqlite3.Row # Fixar hur man får information från databasen.
        self.cursor = self.to_do_connection.cursor()
        self.logger = FileLogger('db.log')
        self.initialDB()

    def do_query_data(self, sql, data) -> None:
        try:
            if data is None:
                self.cursor.execute(sql)
                self.logger.log_db_query(sql)
            else:
                self.cursor.execute(sql, data)
                self.logger.log_db_query_data(sql, data)
        except Exception as e:
            print(f'DB Error: {e}')
            self.logger.log_error(f'DB Error: {e}')
            # self.to_do_connection.rollback()
            raise e


    def do_query(self, sql) -> None:
        self.do_query_data(sql, None)

    #* This function will create the database and tables as soon as the database object is used.
    def initialDB(self) -> None:
        #* Create the User Table if not exits
        self.do_query('''CREATE TABLE IF NOT EXISTS user(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )''')

        #* Create the task_list Table if not exits
        self.do_query('''CREATE TABLE IF NOT EXISTS task_list(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            task_number INTEGER,
            task TEXT NOT NULL,
            status BOOLEAN DEFAULT 0,
            FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE CASCADE
        )
        ''')
        
        self.to_do_connection.commit()
 

    #* USERS FUNKTIONS
    
    
    #* Register a new user
    def register_user(self, username:str, password:str)->int:
        self.do_query_data('''SELECT * FROM user WHERE username=? AND password=?''', (username, password,))
        existing_user = self.cursor.fetchone()
        
        if(existing_user):
            print()
            print("****Server Response: User already exist***")
            print()
            return None
        else:
            self.do_query_data('''INSERT INTO user (username, password) VALUES (?, ?)''', (username, password,))
            self.to_do_connection.commit()
            print(f"user {username} successfully registered.")
            return existing_user
            
            
    #* Login system
    def login_user(self, username:str, password:str)->dict:
        self.do_query_data('''SELECT * FROM user WHERE username=? AND password=?''', (username, password,))
        existing_user: dict = self.cursor.fetchone()
        
        if existing_user:
            self.to_do_connection.commit()
            return existing_user
        else:
            print()
            print("****Server Response: User doesn't exist***")
            print()
            return None
        
        
        
    
    #* TASK_LIST FUNKTIONS
    

    #* Gets a task by id and returns it to the user
    def get_one_task(self, task_id, user_id) -> dict:
        self.do_query_data('''SELECT * FROM task_list WHERE task_number=? AND user_id=?''',(task_id,user_id,))
        task_object: dict = self.cursor.fetchone()
        return task_object

    #* Gets all tasks by id and returns it to the user
    def get_tasks(self, user_id): 
        self.do_query_data('''SELECT * from task_list WHERE user_id=?''', (user_id,))
        return self.cursor.fetchall()
    
    
    #* Add a task to the database.
    def add_tasks(self, user_id: int, task: str) -> None:
        self.do_query_data('''SELECT MAX(task_number) FROM task_list WHERE user_id=?''', (user_id,))
        last_task_number = self.cursor.fetchone()[0] or 0
        new_task_number = last_task_number + 1
        
        self.do_query_data('''INSERT INTO task_list (user_id, task, task_number) VALUES (?, ?, ?)''', (user_id, task, new_task_number))
        
        self.to_do_connection.commit()
        return self.cursor.lastrowid
    
    #* Remove One task to the database.
    def remove_task(self, task_id:int, user_id:int) -> None:
        self.do_query_data('''DELETE FROM task_list WHERE task_number=? AND user_id=?''',(task_id, user_id,))
        self.to_do_connection.commit()
    
    
    #* Pick a task by id and update it
    def update_task(self, task_id: int, task: str, user_id:int ) -> None:
        self.do_query_data('''UPDATE task_list SET task=? WHERE task_number=? AND user_id=?''',(task, task_id, user_id))
        self.to_do_connection.commit()

  
    #* Update status of the selected task. True/False
    def update_status(self, status: int, task_id: int, user_id:int):
        self.do_query_data('''UPDATE task_list SET status=? WHERE task_number=? AND user_id=?''',(status, task_id, user_id))
        self.to_do_connection.commit()
    
