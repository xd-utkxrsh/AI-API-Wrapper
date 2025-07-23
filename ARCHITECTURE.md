# AI API Wrapper – Architecture

## 🔧 Stack

- **Backend**: Flask (Python) or Express (Node.js)
- **Containerized**: Docker
- **Documentation**: Swagger UI via OpenAPI spec
- **CI/CD**: GitHub Actions (optional)
- **Deployment**: Railway / Render / Fly.io

## 📊 Flow

1. User sends a POST request to `/generate` with:
   - provider: e.g., "openai"
   - prompt: user input
   - model: optional, e.g., "gpt-3.5-turbo"

2. The API reads the request, selects the correct internal handler (like OpenAI or Cohere).

3. The handler makes the actual API call to the provider.

4. Response is formatted and sent back to the user.

## 📁 Directory Layout (Conceptual)

