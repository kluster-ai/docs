import os

import litellm.exceptions
from litellm import completion

# Set environment variables for kluster.ai
os.environ["OPENAI_API_KEY"] = "INSERT_API_KEY"  # Replace with your key
os.environ["OPENAI_API_BASE"] = "https://api.kluster.ai/v1"

def main():
    model = "openai/klusterai/Meta-Llama-3.3-70B-Instruct-Turbo"

    messages = [
        {"role": "system", "content": "You are a helpful AI assistant."},
        {"role": "user",   "content": "Explain the significance of the California Gold Rush."},
    ]

    # --- 1) STREAMING CALL: Only print chunk text --------------------------------
    try:
        response_stream = completion(
            model=model,
            messages=messages,
            max_tokens=300,
            temperature=0.3,
            stream=True,  # streaming enabled
        )
    except Exception as err:
        print(f"Error calling model: {err}")
        return

    print("\n--------- STREAMING RESPONSE (text only) ---------")
    streamed_text = []

    # Iterate over each chunk from the streaming generator
    for chunk in response_stream:
        if hasattr(chunk, "choices") and chunk.choices:
            # If the content is None, we replace it with "" (empty string)
            partial_text = getattr(chunk.choices[0].delta, "content", "") or ""
            streamed_text.append(partial_text)
            print(partial_text, end="", flush=True)

    print("\n")  # new line after streaming ends

    # Combine the partial chunks into one string
    complete_first_answer = "".join(streamed_text)

    # Append the entire first answer to the conversation for multi-turn context
    messages.append({"role": "assistant", "content": complete_first_answer})

    # --- 2) SECOND CALL (non-streamed): Print just the text ---------------------
    messages.append({
        "role": "user",
        "content": (
            "Thanks for that. Can you propose a short, 3-minute presentation outline "
            "about the Gold Rush, focusing on its broader implications?"
        ),
    })

    try:
        response_2 = completion(
            model=model,
            messages=messages,
            max_tokens=300,
            temperature=0.6,
            stream=False  # non-streamed
        )
    except Exception as err:
        print(f"Error calling model: {err}")
        return

    print("--------- RESPONSE 2 (non-streamed, text only) ---------")
    second_answer_text = ""
    if response_2.choices and hasattr(response_2.choices[0], "message"):
        second_answer_text = response_2.choices[0].message.get("content", "") or ""

    print(second_answer_text)

if __name__ == "__main__":
    main()
