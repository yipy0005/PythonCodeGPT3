import os
import sys

import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


def main():
    while True:
        prompt = input("\nType your prompt here (Type 'exit' to exit the program): ")

        if "exit" in prompt.lower():
            print("Goodbye!")
            sys.exit()

        else:
            try:
                number_of_tokens = input("\nNo. of tokens to use (Default: 200): ")
                if number_of_tokens == "":
                    number_of_tokens = 200
                tokens = int(number_of_tokens)

                temperature = input(
                    (
                        "\nHow creative do you want the AI to be (Default, 0: Low Creativity "
                        "to 1: High Creativity): "
                    )
                )
                if temperature == "":
                    temperature = 0
                temperature = float(temperature)

                result = openai.Completion.create(  # type: ignore
                    model="code-davinci-002",
                    prompt=f"# {prompt}\nimport",
                    max_tokens=tokens,
                    temperature=temperature,
                )

                result_text: str = f"\nOutput:\n\nimport{result['choices'][0]['text']}"  # type: ignore

                print(result_text)  # type: ignore

            except ValueError:
                print("Invalid token number!")


if __name__ == "__main__":
    main()
