# AI API Wrapper 🔗🤖

A minimal Flask-based API wrapper for OpenAI, with Swagger UI documentation support.

## 🚀 Features

- Simple `/generate` endpoint to send prompts to OpenAI's Chat API.
- Swagger UI at `/docs` for testing and visual documentation.
- Uses environment variables for security.
- Clean, professional folder structure.

---

## 📁 Folder Structure

```
AI-API-Wrapper/
│
├── app.py                  # Main Flask app
├── .env                   # Your OpenAI API Key
├── requirements.txt        # Dependencies
├── static/
│   └── swagger.json        # Swagger specification
├── templates/              # (Optional for HTML, not used here)
└── README.md
```

---

## 🔧 Setup Instructions

### 1. Clone & Navigate

```bash
git clone https://github.com/your-username/AI-API-Wrapper.git
cd AI-API-Wrapper
```

### 2. Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
venv\Scripts\activate   # For Windows
source venv/bin/activate  # For Linux/Mac
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Add Environment Variable

Create a `.env` file:

```
OPENAI_API_KEY=your_openai_key_here
```

### 5. Run the App

```bash
python app.py
```

Go to: `http://localhost:5000/docs` for Swagger UI  
or `POST` to `http://localhost:5000/generate` with JSON body.

---

## 🔍 Sample Request (cURL or Postman)

```json
POST /generate
{
  "provider": "openai",
  "prompt": "Tell me a joke",
  "model": "gpt-3.5-turbo"
}
```

---

## 📦 Deployment Options

- Railway
- Render
- EC2
- Fly.io
- Localhost

---

## 📘 License

MIT License. Use it freely.
