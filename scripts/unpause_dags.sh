#!/bin/bash
set -ex
# Airflow API base URL
base_url="http://localhost:8080/api/v1"  # Replace with your Airflow instance URL

# Authentication (if needed)
username="airflow"
password="airflow"  # Replace with your Airflow credentials


# Loop through the list and unpause each DAG
for i in {1..1000}
do
    echo "Unpausing DAG: $dag_id"

    # API endpoint to unpause the DAG
    endpoint="${base_url}/dags/loop_atifs_dag$i"

    # Unpause the DAG using the PATCH method
    curl -X PATCH "${endpoint}" \
        -u "${username}:${password}" \
        -H "Content-Type: application/json" \
        -d '{"is_paused": false}'

    echo "DAG ${dag_id} unpaused."
done

echo "All specified DAGs have been unpaused."
