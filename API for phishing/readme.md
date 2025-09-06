This folder contains the api built using models that predict the google index and pagerank using urls and ultimately identifying whether the url belongs to a phishing website or not.

<p align="center">
   <img src="https://placehold.co/1200x300/transparent/0089fe?text=Phishing+Detection+API\nusing+Machine+Learning&font=Raleway&font-weight=700" />
</p>

This project implements a **phishing detection API** that analyzes URLs and predicts whether they are **legitimate** or **phishing** using machine learning models.

The system trains three models and integrates them into a FastAPI backend:

1. **Predicted PageRank** (Regression Model)
2. **Predicted Google Index** (Classification Model)
3. **Phishing Detection** (Classification using predicted PageRank & Google Index)



## 🪼 Features

* Extracts URL-based features (length, hostname, presence of `https`, `@`, `www`, etc.) without external API calls.
* Trains three separate models:

  * **Random Forest Regressor** → PageRank
  * **Random Forest Classifier** → Google Index
  * **Random Forest Classifier** → Phishing Detection
* FastAPI backend exposes a `/predict` endpoint for real-time predictions.
* Saves trained models as `.pkl` files using `joblib`.



## 🪼 Project Structure

```
├── dataset_phishing.csv         # Training dataset
├── phishing_training.ipynb      # Model training notebook
├── model_pagerank.pkl           # Trained PageRank model
├── model_googleindex.pkl        # Trained Google Index model
├── model_phishing.pkl           # Trained Phishing Detection model
├── app.py                       # FastAPI backend
├── README.md                    # Project documentation
```



## 🪼 Installation

Clone this repository and install dependencies:

```bash
git clone https://github.com/your-username/phishing-detection-api.git
cd phishing-detection-api

# Create virtual environment
python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)

# Install dependencies
pip install -r requirements.txt
```

### Required Python Packages

```
fastapi
uvicorn
pandas
scikit-learn
tldextract
joblib
```



## 🪼 Model Training

Run the provided Jupyter Notebook (`phishing_training.ipynb`) to:

1. Load dataset & preprocess URLs
2. Extract features using `tldextract`
3. Train three models:

   * PageRank Regressor → `model_pagerank.pkl`
   * Google Index Classifier → `model_googleindex.pkl`
   * Phishing Detector → `model_phishing.pkl`

The trained models will be saved as `.pkl` files.



## 🪼 Running the API

Start the FastAPI server:

```bash
uvicorn app:app --reload
```

## Example Request

### Endpoint:

`POST /predict`

### Request Body:

```json
{
  "url": "http://example-login.com/secure"
}
```

### Response:

```json
{
  "url": "http://example-login.com/secure",
  "predicted_page_rank": 2.34,
  "predicted_google_index": 0,
  "phishing_status": "phishing"
}
```



## 🪼 Output

* **predicted\_page\_rank** → Numeric score predicted by the regression model
* **predicted\_google\_index** → 0 (not indexed) or 1 (indexed)
* **phishing\_status** → `phishing` or `legitimate`



## 🪼 Author

**Ananya P S**
