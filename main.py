import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types

from call_function import available_functions, call_function
from prompts import system_prompt


def main():
    load_dotenv()

    verbose = "--verbose" in sys.argv
    args = []
    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)

    if not args:
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]

    counter = 1
    while counter < 20:
        try:
            response = client.models.generate_content(
                model='gemini-2.0-flash-001',
                contents=messages,
                config=types.GenerateContentConfig(
                    tools=[available_functions],
                    system_instruction=system_prompt
                )
            )

            # print("HELLO PLEASE LOOK HERE")

            if response.candidates:
                for candidate in response.candidates:
                    messages.append(candidate.content)


            # prompt_tokens = response.usage_metadata.prompt_token_count
            # response_tokens = response.usage_metadata.candidates_token_count

            if not response.function_calls:
                if response.text != "":
                    print(response.text)
                    break
                    counter += 1
                else:
                    raise Exception("Unexpected error!")

            else:
                function_call_results = []

                for function_call in response.function_calls:
                    result = call_function(function_call, verbose=verbose)
                    parts = result.parts
                    if not parts or not parts[0].function_response:
                        raise Exception("Function call result missing function_response")
                    if verbose:
                        print(f"-> {parts[0].function_response.response}")

                    function_call_results.append(parts[0])
                function_response = types.Content(role="user", parts=function_call_results)
                messages.append(function_response)
                counter += 1
        except Exception as e:
            return f"Error with generating response {e}"

if __name__ == "__main__":
    main()
