# Digits Recognition App
The Digits Recognition App is a web-based tool that allows users to upload an image of a handwritten digit and get an accurate prediction of what digit it represents. The app is built using machine learning and Streamlit, a Python library for building interactive web applications.

The machine learning model used in the app is trained on the digits recognition dataset, a popular dataset of 8x8 pixel images of handwritten digits. The model is a logistic regression classifier that is trained on a subset of the dataset and achieves high accuracy on the testing set.

The app itself is simple and intuitive to use. Users can upload an image of a digit and the app will display the image and predict what digit it represents. The app also provides instructions for the user and examples of images that can be uploaded.

The Digits Recognition App is a useful tool for anyone who needs to recognize handwritten digits, whether for personal or professional use. The app is also a great example of how machine learning and Streamlit can be used together to create powerful and interactive web applications.

# Installation
## To install and run this application, follow these steps:

### Clone the repository to your local machine.
    https://github.com/actuaryhafeez/handwritten-digits-classification.git
### Create a new virtual environment in the project directory.
    python3 -m venv venv
### Activate the virtual environment. 
    source venv/bin/activate
### Jupyter Notebook has also been installed in the virtual environment. Install the necessary dependencies by running the command
    pip install -r requirements.txt.
### Run Jupyter Notebook using the following command to open notebook.ipynb
    jupyter notebook
### Start the Flask server by running the command python app.py in the terminal.
    streamlit run app
### Open a web browser and navigate to http://localhost:8501 to access the home page of the application.
### Upload digit image from data directory and click "Predict" to see the predicted species.
![digit](https://user-images.githubusercontent.com/55107467/233194039-ecc980dc-8203-470b-84cd-44c32c3a8761.png)

## Project Structure 

    Digits Recognition App/
        ├── data/
        │   └── testSample
        │   └── testSet
        │   └── trainingSample
        │   └── trainingSet
        
        ├── model/
        │   └── digits_model.pkl
        ├── app.py/
        │  
        ├── notebook.ipynb/
        ├── requirements.txt/
        ├── README.md/

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

This project adheres to the [Open Source Initiative's](https://opensource.org) definition of open source software and the [Open Source Initiative's Approved License List](https://opensource.org/licenses/alphabetical).

