# AI-API

# Sentiment Analysis API with Flask

This project demonstrates a simple Sentiment Analysis API using Flask, TensorFlow/Keras, and MySQL.

## Description

The Sentiment Analysis API allows users to predict the sentiment (positive or negative) of input text using a pre-trained deep learning model. The predictions are made using a Flask web application, and the results are stored in a MySQL database.

## Prerequisites

- Python 3.x
- TensorFlow/Keras
- Flask
- MySQL Connector

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/your-repo.git
    cd your-repo
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up MySQL:

    - Create a MySQL database named `datastore`.
    - Configure MySQL connection details in the code (`app.py`).

4. Run the application:

    ```bash
    python app.py
    ```

## Endpoints

1. **Predict Sentiment:**
   - **Endpoint:** `/predict/<pred_data>`
   - **Method:** GET
   - **Description:** Predicts sentiment for the given text.

2. **Accept Data:**
   - **Endpoint:** `/preddata`
   - **Method:** POST
   - **Description:** Accepts data in JSON format, predicts sentiment, and stores results in the database.

## Usage

- Predict sentiment for a text:
    ```bash
    curl http://localhost:5000/predict/This-is-a-text
    ```

- Submit data for prediction and storage:
    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"data": "This is a text."}' http://localhost:5000/preddata
    ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Mention any additional acknowledgments or credits.

