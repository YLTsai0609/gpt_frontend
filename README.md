# GPT Frontend Project

This project is a simple web application that allows users to interact with OpenAI's GPT models through a web interface. The application is built using Flask for the backend and HTML/JavaScript for the frontend.

## Features

- Send text messages to OpenAI's GPT models and receive responses.
- Display text and image responses from the model.
- Environment variable management using `.env` files.

## Prerequisites

- Python 3.8 or higher
- Poetry for dependency management
- OpenAI API key

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/gpt-frontend.git
   cd gpt-frontend
   ```

2. **Install dependencies using Poetry:**

   ```bash
   poetry install
   ```

3. **Set up environment variables:**

   Create a `.env` file in the project root directory and add your OpenAI API key:

   ```plaintext
   OPENAI_API_KEY=your_api_key
   ```

## Usage

1. **Run the Flask application:**

   ```bash
   poetry run python app.py
   ```

2. **Access the application:**

   Open your web browser and go to `http://localhost:5000`.

## Project Structure

- `app.py`: The main Flask application file.
- `templates/index.html`: The HTML template for the frontend.
- `static/`: Directory for static files like CSS and JavaScript.

## Troubleshooting

- **Port 5000 is in use:** Use `lsof -i :5000` to find and terminate the process using the port.
- **Invalid API key:** Ensure your `.env` file contains the correct OpenAI API key.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## TODO

- [ ] - hello world for openai chats
- [ ] - chatgpt response with async text message
- [ ] - deployment to andoird app (PWA)
- [ ] - chatgpt response with image
