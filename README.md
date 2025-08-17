# 🌍 AI Travel Advisor

> ✈️ Your **AI-powered travel planner** — research destinations, calculate budgets, and generate realistic itineraries in **one click**.  
Built with [CrewAI](https://github.com/joaomdmoura/crewai), **Gemini LLM**, and **Streamlit**.  

---

## ✨ Features
- 🧭 **Smart Research** – Accurate transport, attractions, accommodations, food, and weather.  
- 💰 **Budget Planner** – Full trip cost breakdown, with trade-offs if over budget.  
- 🗓️ **Itinerary Generator** – Realistic day-by-day plans with times, meals, and rest.  
- 📄 **One-Click PDF Export** – Styled, professional trip plan downloads.  
- 🌐 **Live Search Integration** – Powered by SerperDevTool.  
- 🎥 **Demo Included** – Video walkthrough + sample PDF in `trip_plan/`.  

---

## 🛠️ Tech Stack
![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.38-ff4b4b?logo=streamlit)
![CrewAI](https://img.shields.io/badge/CrewAI-Agents-green)
![Gemini](https://img.shields.io/badge/Gemini-LLM-orange)
![Serper](https://img.shields.io/badge/SerperDevTool-Live%20Search-purple)

- **CrewAI** – Multi-agent orchestration  
- **CrewAI-Tools** – External tool integrations (SerperDevTool)  
- **Gemini LLM** – Google’s language model  
- **Streamlit** – UI for interaction  
- **python-dotenv** – Manage environment variables securely  
- **Markdown + pdfkit** – Trip plan formatting & export  

---

## ⚡ Quickstart

```bash
# 1️⃣ Clone the repo
git clone <your-repo-url>
cd <your-repo-folder>

# 2️⃣ Create environment (Conda recommended)
conda create -p venv python==3.10
conda activate venv

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Add API keys in .env (create this file yourself!)
echo "gemini_api=YOUR_GEMINI_KEY" >> .env
echo "serper_key=YOUR_SERPER_KEY" >> .env

# 5️⃣ Run the app
python -m streamlit run crewai_app.py
```

---

## 📂 Project Structure

```
├── agents.py          # AI agents for research, budgeting, and itinerary
├── tasks.py           # Task definitions for each agent
├── llm.py             # Gemini LLM initialization
├── tools.py           # Search tool integration (SerperDevTool)
├── crewai_app.py      # Streamlit application
├── requirements.txt   # Project dependencies
├── trip_plan/         # Sample PDF and demo video
│   ├── trip_plan_Pune_to_Maldives.pdf   # Sample trip plan (auto-generated)
│   └── AI_travel_advisor.mp4            # Demo video of the app in action
├── README.md          # Project documentation
```

---

## 📊 Demo

- 📄 **Sample PDF:** [trip_plan_Pune_to_Maldives.pdf](trip_plan/trip_plan_Pune_to_Maldives.pdf)  
- 🎥 **Demo Video:** [AI_travel_advisor.mp4](trip_plan/AI_travel_advisor.mp4)  

---

## 🚀 Roadmap
- [ ] Add support for multi-city trips  
- [ ] Export in additional formats (DOCX, XLSX)  
- [ ] Improve cost optimization with real-time APIs  

---

## ⚖️ License
MIT License — free to use, modify, and share.  

---

💡 *Built for travelers, by AI enthusiasts. Let AI do the planning while you enjoy the journey.* 🌴
