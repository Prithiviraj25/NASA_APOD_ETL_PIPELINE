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
[flowchart](https://github.com/Prithiviraj25/NASA_APOD_ETL_PIPELINE/blob/main/images/flowchart.png)
 