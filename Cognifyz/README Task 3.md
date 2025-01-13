* Task Class:

	The Task class has attributes title, description, and completed (default is False).
	The __str__ method is overridden to provide a readable format for each task.

* TaskManager Class:

	Contains a list tasks to hold the task objects.
	create_task(): Takes user input to create a new task and adds it to the list.
	read_tasks(): Displays all tasks.
	update_task(): Allows the user to select a task and update its title and description.
	delete_task(): Allows the user to select and delete a task.

* Main Function:

	Displays a menu with options to create, read, update, or delete tasks, and runs in a loop until the user chooses to exit.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

* Create Task: Adds a new task.
* Read Tasks: Displays all tasks.
* Update Task: Updates the details of an existing task.
* Delete Task: Deletes a specific task.
* Exit: Exits the application.
