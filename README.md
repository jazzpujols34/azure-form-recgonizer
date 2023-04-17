# Form Recognizer App

This is a Python application that uses the Azure Form Recognizer service to recognize data from a receipt image and extract relevant information.

## Prerequisites

- Python 3.x
- Azure subscription (to access the Form Recognizer service)
- `.env` file (to store your Form Recognizer endpoint and key)

## Installation

1. Clone the repository:
git clone https://github.com/your-username/form-recognizer-app.git


2. Install the required packages:
pip install azure.ai.formrecognizer python-dotenv


3. Create a `.env` file in the root directory of your project and add the following lines to it:
FORM_RECOGNIZER_ENDPOINT=https://your-form-recognizer-endpoint.azure.com/
FORM_RECOGNIZER_KEY=your-form-recognizer-key


4. Replace the values with your actual Form Recognizer endpoint and key.

## Usage

To run the application, open a terminal in the root directory of your project and run the following command:
python app.py


The application will recognize data from a sample receipt image and extract the following information:

- Form type
- Merchant name
- Transaction date
- Receipt items (item name and price)
- Total

You can modify the code in `app.py` to recognize data from a different receipt image or to extract different types of information.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
