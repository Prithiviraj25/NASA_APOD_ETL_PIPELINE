# needed to make DAG
from airflow import DAG 
#used to hit a api using airflow we need this  below operator
from airflow.providers.http.operators.http import SimpleHttpOperator 
# we need airflow decorator
from airflow.decorators import task
# in order to connect to postgres airflow provides hook
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.utils.dates import days_ago
import json


## Defining the DAG
with DAG(
    dag_id='NASA_apod_data_postgres',
    start_date=days_ago(1),
    schedule_interval='@daily',
    catchup=False
) as dag:
    
    ## task to create the table if it does not exists
    ## we will be using postgres for this purpose
    @task
    def create_table():
        ## initialize the postgreshook
        postgres_hook=PostgresHook(postgres_conn_id="my_postgres_connection")
        
        ## SQL query to create the table
        create_table_query="""
        CREATE TABLE IF NOT EXISTS apod_data(
        id SERIAL PRIMARY KEY,
        title VARCHAR(255),
        explanation TEXT,
        url TEXT,
        date DATE,
        media_type VARCHAR(50)
        );
        """

        ## execute the query 
        postgres_hook.run(create_table_query)

    ## task to extract data from NASA api
    ## basically we will setting up a connection for this 
    ## the connection will be providing the api_key without need for hardcode
    extract_data=SimpleHttpOperator(
        task_id="Extracting_data",
        http_conn_id="nasa_api_connection", ## connection id we will define for NASA API
        endpoint="planetary/apod", ## NASA API endpoint
        method='GET',
        data={"api_key": "{{ conn.nasa_api_connection.extra_dejson.api_key }}"},## using this we dont need to hardcode the apikey
        response_filter= lambda response:response.json(),
    )

    ## task to transforme the response into required form for us
    @task
    def transform_data(response):
        data={
            'title': response.get('title', ''),
            'explanation': response.get('explanation', ''),
            'url': response.get('url', ''),
            'date': response.get('date',''),
            'media_type': response.get ('media_type',' '),
        }
        return data
    
    ## task to load the Data in the Postgres Database

    @task
    def load_data(data):
        ## we will initialze the postgreshook
        ## the connection id must same as that in the create table 
        postgres_hook=PostgresHook(postgres_conn_id='my_postgres_connection')

        ## SQL query to insert the value the value to DB
        insert_query="""
        INSERT INTO apod_data(title,explanation,url,date,media_type)
        VALUES (%s,%s,%s,%s,%s);
        """
        ## we will run the query 
        postgres_hook.run(insert_query,parameters=(
            data['title'],
            data['explanation'],
            data['url'],
            data['date'],
            data['media_type']
        ))

        ## we will define the task dependencies
    create_table() >> extract_data
    api_response=extract_data.output
    transformed_data=transform_data(api_response)
    load_data(transformed_data)
