# Task manager API
1. Django
2. Django Rest

## Plan for the API
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
    - User authentication
        - Methods
            1. POST (register)
            2. POST (LOGIN)
    - Task management
        - Methods
            1. POST
            2. GET
            3. PUT
            4. DELETE