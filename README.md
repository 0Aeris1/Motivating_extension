
## Spark the Motivator

## Overview

Spark is a lightweight Chrome extension designed to combat procrastination by delivering short, AI-generated motivational messages on click. An optional input field allows users to interact directly with Spark for more personalized encouragement.

The extension communicates with a Python FastAPI backend that securely interfaces with the OpenAI API.

---
### ✨ Features

- Generates AI motivational quotes

- Optional user input

- Hosted FastAPI backend

- OpenAI integration

- Deployed on Render

---
## Installation

1. Clone the repository:

```sh
git clone https://github.com/0Aeris1/Motivating_extension.git

```

2. Open Chrome -> Extensions

3. Enable Developer Mode

4. Load unpacked and select /extension directory

Once loaded, clicking the Spark icon will generate a motivational response 

> Note: The backend is hosted on Render’s free tier. After prolonged inactivity, the service may take up to ~60 seconds to spin back up. Spark is also rate-limited to 5 messages per day to control costs.

---
### Optional: Run the Backend Locally

If desired, one can host Spark locally using your own OpenAI API key.

1. Install dependencies

```bash
pip install -r requirements.txt

```

2. Set your OpenAI API key

```bash
export OPENAI_API_KEY="your key here"

```

3. Update the extension backend URL
In popup.js, change the backend URL to:

```js
http://127.0.0.1:8000

```

4. Start the backend
Make sure to run this from the project root:

```bash
uvicorn backend.engine.app:app --reload

```
Spark will now use your local backend and API key.

You can optionally change or remove rate limiting completely, to do so modify app.py:

```python
@limiter.limit("5/day") #Adjust as needed

```
This will boost your productivity better than coffee.

---
## Security

Security was an important consideration in this project. While the backend endpoint is publicly accessible, usage is controlled via rate limiting to prevent abuse and manage costs.

The OpenAI API key is stored only on the backend as an environment variable.

No secrets are exposed in the extension or frontend code.

Rate limiting provides sufficient protection for the scope of this project.

This approach balances simplicity, cost control, and responsible API usage.

---
### Things Learned

- Integrating third-party APIs.
- Building and deploying a FastAPI backend.
- Chrome extension architecture and lifecycle
- Client-server separation concerns
- Practical tradeoffs between security, cost and complexity



