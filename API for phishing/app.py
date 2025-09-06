from fastapi import FastAPI, Query
from pydantic import BaseModel
import tldextract
import joblib

# Load models
model_pagerank = joblib.load('model_pagerank.pkl')
model_googleindex = joblib.load('model_googleindex.pkl')
model_phishing = joblib.load('model_phishing.pkl')

app = FastAPI()

def extract_features(url: str):
    ext = tldextract.extract(url)
    features = {
        "length_url": len(url),
        "length_hostname": len(ext.domain + '.' + ext.suffix),
        "nb_dots": url.count('.'),
        "nb_hyphens": url.count('-'),
        "nb_slash": url.count('/'),
        "nb_www": int('www' in url),
        "has_https": int('https' in url),
        "nb_at": url.count('@'),
        "nb_qm": url.count('?'),
        "nb_and": url.count('&'),
        "nb_eq": url.count('='),
        "prefix_suffix": int('-' in ext.domain),
    }
    return list(features.values())

class URLInput(BaseModel):
    url: str

@app.post("/predict")
def predict_url(data: URLInput):
    features = extract_features(data.url)
    
    page_rank_pred = model_pagerank.predict([features])[0]
    google_index_pred = model_googleindex.predict([features])[0]

    phishing_pred = model_phishing.predict([[page_rank_pred, google_index_pred]])[0]

    return {
        "url": data.url,
        "predicted_page_rank": round(float(page_rank_pred), 2),
        "predicted_google_index": int(google_index_pred),
        "phishing_status": "phishing" if phishing_pred == 1 else "legitimate"
    }
