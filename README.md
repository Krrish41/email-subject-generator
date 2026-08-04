---
title: Email Subject Line Generator
emoji: 📬
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: 5.0.1
app_file: app.py
pinned: false
license: mit
---

# Email Subject Line Generator

A simple tool that generates email subject lines using IBM's Granite 3.3 8B model via Watson Machine Learning, wrapped in a Gradio interface.

## What it does

Paste your email content, get a subject line back. That's it.

## Powered by

- IBM Watson Machine Learning
- Granite-3-3-8B-Instruct
- Gradio for the UI

## Getting started

You'll need Python 3.11 or 3.12 and an IBM WML account.

1. Clone and install:
   ```bash
   git clone https://github.com/Krrish41/email-subject-generator.git
   cd email-subject-generator
   pip install -r requirements.txt
   ```

2. Add your credentials to `app.py`:
   ```python
   API_KEY = "your-api-key"
   PROJECT_ID = "your-project-id"
   REGION = "your-region"  # e.g., us-south
   ```

3. Run it:
   ```bash
   python app.py
   ```

   Opens at `http://localhost:7860`.

## Example

**Input:**
```
Hi Arjun,

We noticed you haven't stopped by in a while—and we miss you!

A lot has changed since your last visit. New arrivals, upgraded features,
and members-only offers are waiting for you. And just to make it sweeter,
here's a 20% discount on your next purchase.

Use code WELCOME20 at checkout. But act fast—this offer expires in 72 hours.

Come back and rediscover what you've been missing.

See you soon,
The NovaStore Team
```

**Output:**
```
🎁 Arjun, Your Favorite Store Awaits with Exclusive Offers & 20% Discount! 🎁
```

## Note

Keep your IBM API key private. Don't commit it to public repos.

## Author

Krrish Ranjan