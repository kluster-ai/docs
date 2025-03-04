# Check if the Batch completed successfully
if batch_status.status.lower() == "completed":
    # Retrieve the results
    result_file_id = batch_status.output_file_id
    results = client.files.content(result_file_id).content

    # Save results to a file
    result_file_name = "batch_results.jsonl"
    with open(result_file_name, "wb") as file:
        file.write(results)
    print(f"Results saved to {result_file_name}")
else:
    print(f"Batch failed with status: {batch_status.status}")