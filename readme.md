# Bank Customer Churn Prediction

A machine learning initiative aimed at predicting whether a bank customer is likely to churn (i.e., leave the bank).

## Overview

The **Bank Customer Churn Prediction** project leverages historical customer data to build and deploy a predictive model that can help banks identify at-risk customers, allowing them to implement targeted retention strategies. The project also features a live API endpoint, making the prediction model accessible for integration into other applications.

## Features

### 🎯 Churn Prediction Model
A robust machine learning model capable of predicting customer churn with high accuracy.

### 🔧 Data Preprocessing
Includes comprehensive steps for cleaning and preparing raw customer data for model training.

### 📊 Model Training & Evaluation
Demonstrates the complete process of training the model and evaluating its performance using various metrics.

### 🌐 Live API Endpoint
Provides a deployed API for real-time churn predictions, accessible from anywhere.

## Technologies Used

This project is primarily built using Python and its powerful data science libraries:

- **Python**: The core programming language for the entire project
- **Scikit-learn**: For machine learning model building, training, and evaluation
- **Pandas**: For data manipulation and analysis
- **NumPy**: For numerical operations
- **Flask/FastAPI**: For creating the web API to serve predictions
- **Render.com**: Platform used for deploying the live API

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8+**: [Download Python](https://www.python.org/downloads/)

## Installation

### 1. Clone the Repository

First, clone the GitHub repository to your local machine using Git:

```bash
git clone https://github.com/mann-rana29/Bank-Customer-Churn-Prediction.git
cd Bank-Customer-Churn-Prediction
```

### 2. Set Up Python Environment

It's highly recommended to use a virtual environment to manage dependencies:

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt
```

> **Note**: If `requirements.txt` is not present, you might need to manually install `scikit-learn`, `pandas`, `numpy`, and `flask` (or `fastapi`) using `pip install <package-name>`.

## Usage

### Running the Prediction API Locally

1. **Start the Backend Server**

From the root directory of the project, run the Python application. The main application file is typically `app.py` or `main.py`:

```bash
# Assuming the main application file is app.py
python app.py
```

This will start the API server, usually on `http://127.0.0.1:5000` or a similar address. You can then send POST requests to the prediction endpoint with customer data to get churn predictions.

### Using the Live API

The API is deployed and live at: **https://bank-customer-churn-prediction-4s9d.onrender.com**

You can send POST requests to this URL with your customer data (in JSON format) to receive churn predictions. Refer to the API documentation (if available in the repository) for specific endpoint details and expected data format.

#### Example API Usage

```bash
curl -X POST https://bank-customer-churn-prediction-4s9d.onrender.com/predict \
  -H "Content-Type: application/json" \
  -d '{
    "customer_data": {
      "age": 35,
      "balance": 50000,
      "products_number": 2,
      "credit_score": 700
    }
  }'
```

## Model Performance

The model has been trained and evaluated on historical bank customer data, achieving:
- **Accuracy**: [Add your model's accuracy]
- **Precision**: [Add your model's precision]
- **Recall**: [Add your model's recall]
- **F1-Score**: [Add your model's F1-score]

## API Documentation

### Endpoints

#### `POST /predict`
Predicts whether a customer is likely to churn.

**Request Body:**
```json
{
  "customer_data": {
    "age": 35,
    "balance": 50000,
    "products_number": 2,
    "credit_score": 700
  }
}
```

**Response:**
```json
{
  "prediction": 0,
  "probability": 0.23,
  "status": "success"
}
```

## Contributing

Contributions are welcome! If you'd like to contribute to the Bank Customer Churn Prediction project, please follow these steps:

1. **Fork the repository**
2. **Create a new branch** (`git checkout -b feature/your-feature-name`)
3. **Make your changes**
4. **Commit your changes** (`git commit -m 'Add some feature'`)
5. **Push to the branch** (`git push origin feature/your-feature-name`)
6. **Open a Pull Request**

Please ensure your code adheres to the existing style and includes appropriate tests if applicable.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Support

If you encounter any issues or have questions, please feel free to [open an issue](https://github.com/mann-rana29/Bank-Customer-Churn-Prediction/issues) on GitHub.

## Acknowledgments

- Thanks to the open-source community for providing excellent machine learning libraries
- Special thanks to Render.com for providing a reliable deployment platform

---

*Made with ❤️ for better customer retention strategies*