# LazyML: Machine Learning Dashboard

![LazyML Dashboard](https://github.com/sercangul/LazyML/blob/main/Lazy_ML.PNG "LazyML Dashboard")

LazyML is a powerful and user-friendly dashboard that leverages the LazyPredict library to perform machine learning regression and classification tasks with minimal effort.

## Features

- Easy-to-use web interface powered by Streamlit
- Support for both regression and classification tasks
- Automatic model selection and comparison
- Visual presentation of model performance
- Downloadable results for further analysis

## Installation

### Prerequisites

- Python 3.7+
- pip (Python package manager)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/sercangul/LazyML.git
   ```

2. Navigate to the project directory:
   ```bash
   cd LazyML
   ```

3. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Ensure you're in the project directory:
   ```bash
   cd LazyML
   ```

2. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

3. Open your web browser and go to `http://localhost:8501` (or the address provided in the terminal).

4. Upload your dataset and select whether you want to perform regression or classification.

5. Explore the results and download them for further analysis.

### Online Demo

You can also try the app online without installation: [LazyML on Heroku](http://LazyML.herokuapp.com/)

## Data Format

- Your input data should be in CSV format.
- The target variable should be in the last column of the dataset.
- Ensure your data is cleaned and preprocessed before uploading.

## Contributing

We welcome contributions to LazyML! Here's how you can help:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/AmazingFeature`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
5. Push to the branch (`git push origin feature/AmazingFeature`).
6. Open a Pull Request.

For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [LazyPredict](https://github.com/shankarpandala/lazypredict) library for automated machine learning
- [Streamlit](https://streamlit.io/) for the web interface

## Contact

Sercan Gul - [@sercangul](https://github.com/sercangul) - sercan.gul@gmail.com

Project Link: [https://github.com/sercangul/LazyML](https://github.com/sercangul/LazyML)

---

Made with ❤️ by Sercan Gul