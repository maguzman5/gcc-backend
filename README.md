# gcc-backend

This repo consist in a simple backend that connects to a PostgreSQL database in AWS, and specify the models required for the pipelines about historical employee data for GCC.

These models are contained in `historic_data_db` app:
- **Department**:
    - `id``: default integer
    - `department``: string
- **Jobs**:
    - `id``: default integer
    - `job``: string
- **HiredEmployee**:
    - `id``: default integer
    - `name``: string
    - `datetime``: ISO datetime
    - `department``: string
    - `job``: string 

Note: The `HiredEmployee model` contains references to the Department and Jobs tables using their respective IDs.

This entire project must be executed in a EC2 instance with access to the database. For now, only controls the creation of the table using the models.

### Desired Features (WIP)
- Create a view to inspect/configure the tables schemas
- Create a view to check Cloudwatch logs about integration processes