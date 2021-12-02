from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

def print_message():
    return 'Just another DAG!'

dag = DAG('another_dag', description='Another DAG',
          schedule_interval='0 12 * * *',
          start_date=datetime(2017, 3, 20), catchup=False)

another_operator = PythonOperator(task_id='another_dag', python_callable=print_message, dag=dag)

another_operator
