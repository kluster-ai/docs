from getpass import getpass

from openai import OpenAI

api_key = getpass("Enter your kluster.ai API key: ")

# Set up the client
client = OpenAI(
    base_url="https://api.kluster.ai/v1",
    api_key=api_key
)

# Upload fine-tuning file (for files under 100MB)
with open('training_data.jsonl', 'rb') as file:
    upload_response = client.files.create(
        file=file,
        purpose="fine-tune"  # Important: specify "fine-tune" as the purpose
    )
    
    # Get the file ID
    file_id = upload_response.id
    print(f"File uploaded successfully. File ID: {file_id}")

# Model
model = "klusterai/Meta-Llama-3.1-8B-Instruct-Turbo"

# Create fine-tune job
fine_tuning_job = client.fine_tuning.jobs.create(
    training_file=file_id,
    model=model,
    # Optional hyperparameters
    # hyperparameters={
    #   "batch_size": 3,
    #   "n_epochs": 2,
    #   "learning_rate_multiplier": 0.08
    # }
)

# Retrieve job status
job_status = client.fine_tuning.jobs.retrieve(fine_tuning_job.id)
print(f"Job status: {job_status.status}")

# Get the fine-tuned model name
finished_job = client.fine_tuning.jobs.retrieve(fine_tuning_job.id)
fine_tuned_model = finished_job.fine_tuned_model

# Use the fine-tuned model for inference
response = client.chat.completions.create(
    model=fine_tuned_model,
    messages=[
        {"role": "system", "content": "You are a JSON Generation Specialist. Convert user requests into properly formatted JSON."},
        {"role": "user", "content": "Create a configuration for a web application with name 'TaskMaster', version 1.2.0, and environment set to development."}
    ]
)
