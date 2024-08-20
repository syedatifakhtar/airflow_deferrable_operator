from airflow.decorators import dag, task
from datetime import datetime
from atifspackage.customOperators.DeferrableHelloOperator import  DeferrableHelloOperator
import asyncio

def create_dag(dag_id, schedule, dag_number, default_args):
    @dag(dag_id=dag_id, schedule=schedule, default_args=default_args, catchup=False)
    def hello_world_dag():
        DeferrableHelloOperator(task_id="helloworld_task")
    generated_dag = hello_world_dag()

    return generated_dag

# Build a DAG for each number in range(1, 4)
for n in range(1, 1000):
    dag_id = "loop_atifs_dag{}".format(str(n))

    default_args = {"owner": "airflow", "start_date": datetime(2023, 7, 1)}

    schedule = "@daily"

    dag_number = n

    globals()[dag_id] = create_dag(dag_id, schedule, dag_number, default_args)
