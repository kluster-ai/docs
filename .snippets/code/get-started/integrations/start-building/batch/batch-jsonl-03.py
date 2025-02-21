import time

# Poll the Batch status until it's complete
while True:
    batch_status = client.batches.retrieve(batch_request.id)
    print("Batch status: {}".format(batch_status.status))
    print(
        f"Completed tasks: {batch_status.request_counts.completed} / {batch_status.request_counts.total}"
    )

    if batch_status.status.lower() in ["completed", "failed", "cancelled"]:
        break

    time.sleep(10)  # Wait for 10 seconds before checking again