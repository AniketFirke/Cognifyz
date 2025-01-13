* File Storage:

    The tasks will be stored in a text file (e.g., tasks.txt), where each task is saved on a new line.
    When the program starts, it will load tasks from the file, and when a task is added, updated, or deleted, the file will be updated accordingly.

* Error Handling:

    Proper error handling will be added for file operations to prevent crashes (e.g., handling cases where the file doesn’t exist or is unreadable).

* Testing Persistence:

    The program will read from the file at startup and write to it after any modification

-----------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------

* File I/O Operations:

    load_tasks(): Reads the tasks from the tasks.txt file and creates Task objects from each line.
    save_tasks(): Writes the current list of tasks to the file, ensuring that any modifications (like adding, updating, or deleting a task) are saved.

* Error Handling:

    Handles cases where the task file doesn't exist (FileNotFoundError).
    Catches any other general errors during file reading or writing.
    Task Object Conversion for File:

* The Task class has two methods:
    to_file_string() that converts the task to a string that can be saved to the file.
    from_file_string() that converts a string from the file back into a Task object.

* Persistent Storage:

    On startup, the program loads tasks from the file.
    After any task modification, the program saves the updated tasks back to the file.
  
-----------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------

Example Workflow:
* Initial Startup:
    If no tasks.txt file exists, the program starts with an empty task list.

* Create Task:
    After creating a task, the task is saved to tasks.txt.
  
* Read Tasks:
    The tasks are read from tasks.txt and displayed on the console.
  
* Update and Delete Tasks:
    Modifications to tasks are saved back to tasks.txt.

*Testing the Program:
    Run the program, create, update, and delete tasks. Check the contents of the tasks.txt file to confirm tasks are stored persistently.
    Test with closing and reopening the program to verify that tasks are correctly loaded from the file.
