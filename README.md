# 📬 AI Email Subject Line Generator (IBM Granite)

Generate catchy and relevant email subject lines using IBM's Granite 3.3 8B Instruct model and a simple Gradio interface.

## 🚀 Demo

Paste your email content and get a compelling subject line instantly!

## 🧠 Powered By

- [IBM Watson Machine Learning](https://www.ibm.com/cloud/watson-machine-learning)
- Granite-3-3-8B-Instruct Foundation Model
- [Gradio](https://gradio.app/) for UI

## 📦 Installation

> **Requires Python 3.11 or 3.12**

1. Clone the repo:

```bash
git clone https://github.com/Krrish41/email-subject-generator.git
cd email-subject-generator
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set your IBM WML credentials in `app.py`:

```python
API_KEY = "your-api-key"
PROJECT_ID = "your-project-id"
REGION = "your-region"
```

4. Run the app:

```bash
python app.py
```

The app will open in your browser at `http://localhost:7860`.

## 📄 Example

**Input:**
```
Hi Arjun,

We noticed you haven’t stopped by in a while—and we miss you!

A lot has changed since your last visit. New arrivals, upgraded features,
and members-only offers are waiting for you. And just to make it sweeter,
here’s a 20% discount on your next purchase.

Use code WELCOME20 at checkout. But act fast—this offer expires in 72 hours.

Come back and rediscover what you’ve been missing.

See you soon,
The NovaStore Team
```

**Output:**
```
🎁 Arjun, Your Favorite Store Awaits with Exclusive Offers & 20% Discount! 🎁
```

## 🛡️ Disclaimer

Keep your IBM API Key private and avoid sharing it in public repos.

## 🧑‍💻 Author

Krrish Ranjan
