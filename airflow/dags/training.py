from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.standard.operators.bash import BashOperator

# Default arguments for all tasks
default_args = {
    'owner': 'data_engineer',
    'depends_on_past': False,
    'start_date': datetime(2024, 8, 23),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=3),
    'max_active_runs': 1,
}

# Define the DAG using the new @dag decorator (Airflow 3.x preferred method)
# But we'll use the traditional way for clarity

dag = DAG(
    dag_id='my_airflow3_dag',  # Use dag_id parameter explicitly
    default_args=default_args,
    description='A DAG built for Airflow 3.0.3',
    schedule=timedelta(days=1),  # Use 'schedule' instead of 'schedule_interval' (new in Airflow 2.4+)
    start_date=datetime(2024, 8, 23),
    catchup=False,
    tags=['airflow3', 'tutorial', 'example'],
    max_active_runs=1,  # Limit concurrent DAG runs
    doc_md="""
    # My First Airflow 3.0.3 DAG
    
    This DAG demonstrates basic functionality in Airflow 3.0.3:
    - Python tasks
    - Bash tasks
    - Task dependencies
    - Modern Airflow 3.x features
    """,
)

# Python functions for tasks
def print_context(**context):
    """Print task context information"""
    print("="*50)
    print("🚀 Hello from Airflow 3.0.3!")
    print(f"📅 Execution Date: {context['ds']}")
    print(f"⏰ Current Time: {datetime.now()}")
    print(f"🏷️  Task ID: {context['task'].task_id}")
    print(f"📊 DAG ID: {context['dag'].dag_id}")
    print("="*50)
    return {"status": "success", "message": "Hello task completed"}

def process_data(**context):
    """Simulate data processing"""
    import random
    import time
    
    print("🔄 Starting data processing...")
    
    # Simulate some work
    processing_time = random.uniform(1, 3)
    time.sleep(processing_time)
    
    # Generate fake data
    data = {
        'records_processed': random.randint(1000, 5000),
        'processing_time': round(processing_time, 2),
        'timestamp': datetime.now().isoformat(),
        'status': 'completed'
    }
    
    print(f"📊 Processed {data['records_processed']} records in {data['processing_time']} seconds")
    
    # In Airflow 3.x, you can return data that gets stored in XCom
    return data

def send_notification(**context):
    """Send completion notification"""
    # Get data from previous task using XCom
    data_result = context['task_instance'].xcom_pull(task_ids='process_data_task')
    
    print("📧 Sending notification...")
    print(f"✅ Processing completed successfully!")
    
    if data_result:
        print(f"📈 Summary: {data_result['records_processed']} records processed")
        print(f"⏱️  Time taken: {data_result['processing_time']} seconds")
    
    print("📨 Notification sent!")
    return "notification_sent"

# Task 1: Welcome task with context
welcome_task = PythonOperator(
    task_id='welcome_task',
    python_callable=print_context,
    dag=dag,
    doc_md="Welcome task that prints context information",
)

# Task 2: System information bash task
system_info_task = BashOperator(
    task_id='system_info_task',
    bash_command='''
    echo "🖥️  System Information:"
    echo "📅 Date: $(date)"
    echo "👤 User: $(whoami)"
    echo "📁 Working Directory: $(pwd)"
    echo "🐍 Python Version: $(python3 --version)"
    echo "💾 Disk Usage:"
    df -h | head -5
    echo "🧠 Memory Usage:"
    free -h 2>/dev/null || echo "Memory info not available"
    echo "✅ System check completed!"
    ''',
    dag=dag,
    doc_md="System information and health check task",
)

# Task 3: Data processing task
process_data_task = PythonOperator(
    task_id='process_data_task',
    python_callable=process_data,
    dag=dag,
    doc_md="Simulates data processing and returns results via XCom",
)

# Task 4: Cleanup bash task
cleanup_task = BashOperator(
    task_id='cleanup_task',
    bash_command='''
    echo "🧹 Starting cleanup process..."
    echo "🗑️  Cleaning temporary files..."
    # Create and then clean temp files for demo
    touch /tmp/airflow_demo_file_$$.tmp
    echo "📄 Created temp file: /tmp/airflow_demo_file_$$.tmp"
    rm -f /tmp/airflow_demo_file_$$.tmp
    echo "🧽 Temp file cleaned"
    echo "✨ Cleanup completed!"
    ''',
    dag=dag,
    doc_md="Cleanup temporary files and resources",
)

# Task 5: Final notification task
notification_task = PythonOperator(
    task_id='notification_task',
    python_callable=send_notification,
    dag=dag,
    doc_md="Sends completion notification with processing summary",
)

# Define task dependencies using modern Airflow 3.x syntax
# Method 1: Chain notation (sequential)
welcome_task >> system_info_task >> process_data_task

# Method 2: Multiple downstream tasks (parallel)
process_data_task >> [cleanup_task, notification_task]

# Alternative dependency syntax (all equivalent):
# welcome_task.set_downstream(system_info_task)
# system_info_task.set_downstream(process_data_task)
# process_data_task.set_downstream([cleanup_task, notification_task])

# Or using chain from airflow.models.baseoperator import chain
# from airflow.models.baseoperator import chain
# chain(welcome_task, system_info_task, process_data_task, [cleanup_task, notification_task])