import datetime  as dt
# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
# Operators; we need this to write tasks!
from airflow.operators.bash_operator import BashOperator
# This makes scheduling easy
from airflow.utils.dates import days_ago


#defining DAG arguments

# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'Abanob Morgan',
    'start_date': days_ago(0),
    'email': ['abanob.k.morgan@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
}
# defining the DAG

# define the DAG
dag = DAG(
    'ETL-toll-data',
     schedule_interval=dt.timedelta(days=1),
     default_args=default_args,
    description='Apache Airflow Final Assignment',
   
)


# define the tasks
unzip_data = BashOperator(
    task_id='unzip_data',
    bash_command='tar -xvzf /home/project/airflow/tolldata.tgz \
    -C /home/project/airflow/dags/finalassignment/staging',
    dag=dag,
)
# extract_data_from_csv 

extract_data_from_csv = BashOperator(
    task_id='extract_data_from_csv',
    
bash_command='cut -d"," -f1-4 /home/project/airflow/dags/finalassignment/staging/vehicle-data.csv \
    > /home/project/airflow/dags/finalassignment/csv_data.csv',    dag=dag,
)

# extract_data_from_tsv 
extract_data_from_tsv = BashOperator(
    task_id='extract_data_from_tsv',
    bash_command='cut -f 5- -d"\t" /home/project/airflow/dags/finalassignment/staging/tollplaza-data.tsv \
        > /home/project/airflow/dags/finalassignment/tsv_data.csv',
    dag=dag,
)

# extract_data_from_fixed_width 
extract_data_from_fixed_width = BashOperator(
    task_id='extract_data_from_fixed_width',
    bash_command='cut -f 6- -d" " /home/project/airflow/dags/finalassignment/staging/payment-data.txt \
        > /home/project/airflow/dags/finalassignment/fixed_width_data.csv',
    dag=dag,
)

consolidate_data  = BashOperator(
task_id='consolidate_data',
bash_command='paste -d"\n" /home/project/airflow/dags/finalassignment/csv_data.csv\
           /home/project/airflow/dags/finalassignment/tsv_data.csv\
           /home/project/airflow/dags/finalassignment/fixed_width_data.csv \
          > /home/project/airflow/dags/finalassignment/staging/extracted_data.csv',
dag=dag,
)
# define the task 'transform'

transform_data = BashOperator(
    task_id='transform',
    bash_command="cat /home/project/extracted_data.csv|tr ' ' '#'\
    | awk -F',' '$4 = toupper($4)'|tr ' ' ','| tr '#' ' '\
     > /home/project/airflow/dags/finalassignment/staging/transformed_data.csv",
    dag=dag,
)

 
unzip_data >> [
    extract_data_from_csv,
    extract_data_from_tsv,
    extract_data_from_fixed_width
] >> consolidate_data>> transform_data 
