# 🧠 AI API Wrapper

A lightweight, pluggable REST API that acts as a unified interface for multiple AI models like OpenAI, Cohere, etc. Built with simplicity, containerization, and developer usability in mind.

---

## 🚀 Features

- Unified `/generate` endpoint for multiple AI providers
- Modular design using internal provider handlers
- Swagger UI documentation
- Docker-ready and deployable on Railway/Render
- Environment-based configuration

---

## 🧱 Tech Stack

| Layer       | Technology           |
|-------------|----------------------|
| Backend     | Flask (Python) or Express (Node.js) |
| Docs        | Swagger/OpenAPI      |
| CI/CD       | GitHub Actions (optional) |
| Deployment  | Railway / Render / Fly.io |
| Container   | Docker               |

---

## 🔧 API Usage Example

**POST** `/generate`

```json
{
  "provider": "openai",
  "prompt": "Write a tweet about AI",
  "model": "gpt-3.5-turbo"
}
