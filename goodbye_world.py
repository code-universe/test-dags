from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

def print_goodbye():
    return 'Goodbye world from first Airflow DAG!'

dag = DAG('goodbye_world', description='Goodbye World DAG',
          schedule_interval='0 12 * * *',
          start_date=datetime(2017, 3, 20), catchup=False)

goodbye_operator = PythonOperator(task_id='goodbye_task', python_callable=print_goodbye, dag=dag)

goodbye_operator
