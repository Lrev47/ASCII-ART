# Daily ASCII Art Generator

A Python script that automatically generates unique ASCII art using OpenAI's GPT-4, saves it to a file, and pushes it to GitHub. The script runs daily, creating a growing collection of AI-generated ASCII art.

## Features

- 🎨 Generates random ASCII art using OpenAI's GPT-4
- 📅 Runs automatically once per day
- 💾 Saves each creation with timestamp
- 🔄 Automatically commits and pushes to GitHub
- 🔐 Secure API key handling using environment variables

## Prerequisites

- Python 3.8+
- OpenAI API key
- Git installed and configured
- GitHub repository

## Installation

1. Clone this repository:
   ```bash
   git clone <your-repo-url>
   cd <repo-name>
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Create and configure your `.env` file:
   ```bash
   cp .env.example .env
   ```
   Then edit `.env` and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

4. Make the run script executable:
   ```bash
   chmod +x run_ascii_generator.sh
   ```

## Usage

### Manual Run

To generate ASCII art manually:


```bash
./run_ascii_generator.sh
```


### Automated Daily Run

To set up automatic daily generation, add a cron job:

1. Open your crontab:
   ```bash
   crontab -e
   ```

2. Add the following line to run it daily at midnight:
   ```
   0 0 * * * /path/to/your/run_ascii_generator.sh
   ```

## Project Structure

- `ascii_generator.py`: Main script for generating ASCII art
- `requirements.txt`: List of dependencies
- `run_ascii_generator.sh`: Shell script for running the generator
- `.env.example`: Example environment variables file
- `.gitignore`: List of files to ignore in version control


## How It Works

1. The script uses OpenAI's GPT-4 to generate random ASCII art
2. Each piece is saved in the `generated_ascii` directory with a timestamp
3. The new file is automatically committed and pushed to GitHub
4. The process repeats daily via cron job

## Contributing

Feel free to submit issues and enhancement requests!

## License

[MIT License](LICENSE)

## Acknowledgments

- OpenAI for providing the GPT-4 API
- Python community for the excellent libraries used in this project

## Note

Make sure to keep your OpenAI API key secure and never commit it to the repository. The `.env` file is included in `.gitignore` for this reason. dgf

