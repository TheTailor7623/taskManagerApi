# API practice project for improving productivity

## Task manager API
1. Django
2. Django Rest

### Plan for the API
- Models
    - User
        - Fields
            1. ID
            2. Email
            3. Name
            4. Surname
            5. Password
        - Relationships
            - one to many with the task model (a user can have many tasks)
    - Task
        - Fields
            1. ID
            2. Title
            3. Description
            4. Tags
        - Relationships
            - One to one (a task can only have one user)

- Endpoints
    - Root
        - Displays the API endpoints available for use
    - User authentication
        - Methods
            1. POST api/register (register)
            2. POST api/login (LOGIN)
    - Task management
        - Methods
            1. POST api/tasks (create a new task and list tasks for the logged in user)
            2. GET api/tasks/id (retirieve a task by its id)
            3. PUT api/tasks/id (update a task by its id)
            4. DELETE api/tasks/id (delete a task by its id)

## Life management framework API
1. Django
2. Django Rest

### Plan for the API
- Models
    - Areas
    - Goals
    - Projects
    - Tasks
    - Sub-tasks
- Serializers
    * Areas
    * Goals
    * Projects
    * Tasks
    * Sub-tasks
- Views
    * Areas
    * Goals
    * Projects
    * Tasks
    * Sub-tasks
- Endpoints
    * lifeManager/Areas
    * lifeManager/Areas/area
    * lifeManager/Goals
    * lifeManager/Goals/goal
    * lifeManager/Projects
    * lifeManager/Projects/project
    * lifeManager/Tasks
    * lifeManager/Tasks/task
    * lifeManager/Sub-tasks
    * lifeManager/Sub-tasks/sub-task