# AI CRM System

## Overview
This project is an AI-powered CRM system for healthcare professionals.

It allows sales representatives to:
- Log doctor interactions
- Generate AI-based summaries
- Get recommended next actions

---

## Tech Stack
- Backend: FastAPI
- Frontend: React
- AI: LLM (LangChain / OpenAI)

---

## Features
- Doctor interaction logging
- AI-generated summary
- Smart next action suggestions
- Clean UI for user interaction

---

## How to Run

### Backend
cd backend  
pip install -r requirements.txt  
uvicorn main:app --reload  

### Frontend
cd frontend  
npm install  
npm start  

---

## Example Output
- Summary of doctor interaction
- Suggested next steps:
  - Follow-up meeting
  - Share resources
  - Provide samples

---

## Future Improvements
- Database integration (PostgreSQL)
- Authentication system
- Deployment (Render / Vercel)
