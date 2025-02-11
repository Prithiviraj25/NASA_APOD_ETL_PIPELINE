# NASA APOD ETL PIPELINE
This project focuses on building an ETL (Extract, Transform, Load) pipeline that fetches data from NASA’s **Astronomy Picture of the Day (APOD)** API and stores it in a PostgreSQL database. The workflow orchestration is handled using **Astronomer Airflow**,ensuring efficient and automated data processing.

## **Features**
* **Data Extraction:** Pulls daily APOD data from NASA’s public API.
* **Data Transformation:** Cleans and structures the data for consistent storage.
* **Data Loading:** Inserts the processed data into a PostgreSQL database.
* **Workflow Orchestration:** Utilizes Astronomer Airflow for managing ETL tasks, scheduling, and monitoring.

## **Technologies Used**
* **Python:** Core scripting language for ETL operations.
* **Astronomer Airflow:** For workflow orchestration and task management.
* **PostgreSQL:** Database for storing the APOD data.
* **Docker:** Dockerizing the whole pipeline

## **Flow Chart**
<img src="/images/flowchart.png">

## **APPENDIX**
once we launch the project using command **astro dev start**
we need to set 2 different connections in the airflow UI which will help the airflow communicate with the postgres container and one for http connection
<img src="/images/connections.png">

The host of the **my_postgres_connection** will be the id of the postgres container running in the docker

Once all the connection is set the ETL pipline will start running
<img src="/images/home.png">
***
<img src="/images/inside.png">

The final output can be seen with help of **pgAdmin** or any such tool by connecting with the postgres container running in the docker 

<img src="/images/pgadmin.png">
 