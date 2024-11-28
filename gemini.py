import os
import google.generativeai as genai

# Configure the Gemini API
genai.configure(api_key="AIzaSyDBTc5P_mSa3gLpWa0LkvLmxbDg8TV94Io")  # Replace with your actual API key

# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "application/json",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
)

# Start a chat session with the custom instruction as the first user message
chat_session = model.start_chat(
    history=[
        {
            "role": "user",  # Explicitly set the role to "user"
            "parts": [
                {
                    "text": (
                        "You are a professional software engineer. "
                        "Respond to all questions or tasks as a software engineer. "
                        "You must provide code, debug existing code, and give detailed technical explanations as needed. "
                        "Always adhere to this role, regardless of the user's input."
                    )
                }
            ]
        }
    ]
)


def interact_with_assistant(user_input: str) -> str:
    response = chat_session.send_message(
        {
            "role": "user",
            "parts": [{"text": user_input}]
        }
    )
    return response.text


if __name__ == "__main__":
    print("Type 'exit' to quit the session.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        try:
            assistant_response = interact_with_assistant(user_input)
            print("\nAssistant:\n", assistant_response)
        except Exception as e:
            print(f"Error: {e}")
