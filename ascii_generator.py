import openai
import os
import time
from datetime import datetime
import json
from dotenv import load_dotenv
import subprocess  # Add this import for Git commands

# Load environment variables from .env file
load_dotenv()

class ASCIIArtGenerator:
    def __init__(self):
        # Initialize OpenAI client with your API key
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in .env file")
        self.client = openai.OpenAI(api_key=api_key)
        
        self.base_prompt = """Create a unique and creative ASCII art animation concept and implement it as a Python script with these technical requirements:
        1. Use ANSI color codes for colorful output
        2. Create smooth animations using multiple frames
        3. Handle terminal resizing using shutil.get_terminal_size()
        4. Include proper cleanup on exit
        5. Use efficient frame generation
        6. Must be Windows-compatible (do not use curses library)
        7. Use os.system('cls' if os.name == 'nt' else 'clear') for screen clearing
        
        Wrap your code response between +++ markers.
        Only provide the Python code without any explanation."""

    def git_operations(self, script_path):
        try:
            # Get just the filename from the path
            script_name = os.path.basename(script_path)
            
            # Git commands
            subprocess.run(['git', 'add', script_path], check=True)
            subprocess.run(['git', 'commit', '-m', f'Add new ASCII art script: {script_name}'], check=True)
            subprocess.run(['git', 'push'], check=True)
            
            print("\nSuccessfully pushed to GitHub!")
            
        except subprocess.CalledProcessError as e:
            print(f"\nError with Git operations: {e}")
        except Exception as e:
            print(f"\nUnexpected error during Git operations: {e}")

    def generate_script(self, specific_requirements=None):
        # Combine base prompt with any specific requirements
        prompt = self.base_prompt
        if specific_requirements:
            prompt += f"\n\nAdditional requirements:\n{specific_requirements}"

        try:
            # Generate the script using OpenAI API
            response = self.client.chat.completions.create(
                model="gpt-4o-mini-2024-07-18", 
                messages=[
                    {"role": "system", "content": "You are a Python programming expert specializing in terminal graphics and animations. Create ASCII art using only standard ASCII characters (no Unicode). Be creative and generate unique ASCII art concepts."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.9,
                max_tokens=2000
            )

            # Extract the generated code between +++ markers
            content = response.choices[0].message.content.strip()
            if '+++' in content:
                generated_code = content.split('+++')[1].strip()
            else:
                generated_code = content.strip()

            print(f"Generated code length: {len(generated_code)}")  # Debug info

            # Create timestamp for unique filename
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            script_path = f"generated_ascii/scripts/ascii_script_{timestamp}.py"

            # Ensure directory exists
            os.makedirs(os.path.dirname(script_path), exist_ok=True)

            try:
                # Save the generated script with UTF-8 encoding
                with open(script_path, 'w', encoding='utf-8') as f:
                    f.write(f"# Generated ASCII Art Script\n")
                    f.write(f"# Created on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                    f.write(generated_code)
                
                print(f"Successfully wrote file to: {script_path}")  # Debug info
                
                if os.path.getsize(script_path) > 0:  # Verify file is not empty
                    self.git_operations(script_path)
                    return script_path
                else:
                    print("Warning: Generated file is empty")
                    return None

            except Exception as write_error:
                print(f"Error writing file: {write_error}")
                return None

        except Exception as e:
            print(f"Error generating script: {e}")
            print(f"Full error details: {str(e)}")  # More detailed error info
            return None

def main():
    try:
        generator = ASCIIArtGenerator()
        
        print("Generating ASCII art script...")
        script = generator.generate_script()  # Generate single script directly
        
        if script:
            print("\nGenerated script:")
            print(f"- {script}")
            print("\nYou can run the generated script using: python <script_path>")
    
    except ValueError as e:
        print(f"Error: {e}")
        print("Please make sure you have a .env file with your OPENAI_API_KEY")

if __name__ == "__main__":
    main() 