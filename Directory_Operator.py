from groq import Groq
import os
import subprocess

class LLMBot:
    def __init__(self) -> None:
        # Initialize Groq client with your API key
        self.client = Groq(api_key='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')
        
        # Initialize chat history with system instructions
        self.chat_history = [
            {"role": "system", "content": "You are an assistant capable of managing files and directories. You can create, delete, rename, and list files or directories. Convert the user's input into corresponding file system operations or system commands on Windows. For example, if the user says 'create a folder called Test', just generate the code or CLI command for the operation as your responses are directed towards CLI. Pretend everything is in the current directory. Never use extra formatting like backticks (`)."}
        ]
    
    def generate(self, message):
        # Add the user message to the chat history
        self.chat_history.append({"role": "user", "content": message})

        # Send the chat history to the Groq model for generating a response
        chat_completion = self.client.chat.completions.create(
            messages=self.chat_history,
            model="llama3-8b-8192",  # You can change the model if needed
        )

        # Retrieve the model's response
        response = chat_completion.choices[0].message.content

        # Add assistant's response to the chat history
        self.chat_history.append({"role": "assistant", "content": response})

        return response
    
    def execute_command(self, command):
        """
        Executes the command, either as Python os commands or system commands.
        """
        try:
            # Clean the command to ensure no backticks or malicious formatting
            command = command.strip("`").strip()

            # Check if it's a valid system command or Python code
            if "os." in command or "subprocess." in command:
                exec(command)  # Caution: Executing Python commands, but avoid dangerous code
                return "Python command executed successfully."
            
            # Execute system commands via subprocess
            if os.name == 'nt':  # Windows system
                result = subprocess.run(command, shell=True, capture_output=True, text=True)
            else:  # Linux/MacOS
                result = subprocess.run(command, shell=True, capture_output=True, text=True)
            
            # Return command execution result
            return result.stdout or result.stderr

        except Exception as e:
            return f"Error during command execution: {e}"

    def process_command(self, user_input):
        """
        Process the user input and generate the appropriate system command or Python code.
        """
        # Generate the command using Groq's response
        generated_command = self.generate(user_input)
        print(f"Generated Command: {generated_command}")

        # Execute the generated command
        return self.execute_command(generated_command)


# Test the LLMBot class
if __name__ == "__main__":
    bot = LLMBot()
    
    print("LLM Bot is ready to control your directories! Type 'exit' to quit.")
    
    while True:
        user_input = input("Enter your command: ").strip()

        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        if user_input:
            result = bot.process_command(user_input)
            print("\nResult:")
            print(result)
        else:
            print("Please enter a valid command.")
