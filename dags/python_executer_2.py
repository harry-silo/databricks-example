#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
"""
This is an example DAG which uses the DatabricksSubmitRunOperator.
In this example, we create two tasks which execute sequentially.
The first task is to run a notebook at the workspace path "/test"
and the second task is to run a JAR uploaded to DBFS. Both,
tasks use new clusters.
Because we have set a downstream dependency on the notebook task,
the spark jar task will NOT run until the notebook task completes
successfully.
The definition of a successful run is if the run has a result_state of "SUCCESS".
For more information about the state of a run refer to
https://docs.databricks.com/api/latest/jobs.html#runstate
"""

from datetime import datetime

from airflow import DAG
from airflow.providers.databricks.operators.databricks import DatabricksSubmitRunOperator

with DAG(
    dag_id='harry_python_dag_no_py_ending',
    schedule_interval='@daily',
    start_date=datetime(2021, 1, 1),
    tags=['example'],
    catchup=False,
) as dag:

    new_cluster = {
        'spark_version': '9.1.x-cpu-ml-scala2.12',
        'node_type_id': 'i3.xlarge',
        'aws_attributes': {'availability': 'ON_DEMAND'},
        'num_workers': 2,
    }

   
# wrong 
    # Example of using the JSON parameter to initialize the operator.
    preprocess = DatabricksSubmitRunOperator(task_id='spark_python_task_preprocess', 
                                                new_cluster= new_cluster,
                                                spark_python_task={
                                                    'python_file' :'/Shared/cicd_harry/jobs/preprocess/preprocess'
                                                    }
                                                )
    # [START howto_operator_databricks_json]

    train = DatabricksSubmitRunOperator(task_id='spark_python_task_train', 
                                                new_cluster= new_cluster,
                                                spark_python_task={
                                                    'python_file' :'/Shared/cicd_harry/jobs/train/train'
                                                    }
                                                )
    
    preprocess >> train  