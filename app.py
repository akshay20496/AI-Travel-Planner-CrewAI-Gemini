import streamlit as st  
from crewai import Crew, Process
import markdown
from agents import researcher, budget_planner, itinerary_planner
from tasks import research_task, budget_task, itinerary_task
import pdfkit
import os

# 🚀 Crew Setup: All agents working together!
crew = Crew(
    agents=[researcher, budget_planner, itinerary_planner],
    tasks=[research_task, budget_task, itinerary_task],
    process=Process.sequential
)

st.set_page_config(page_title="AI Travel Advisor", page_icon="🌍", layout="wide")

st.title("🌍 AI Travel Advisor")
st.markdown("Plan your trip with AI-powered research, budget planning, and itinerary creation.")

with st.form("travel_form"):
    origin = st.text_input("Starting Location (Origin)")
    destination = st.text_input("Destination")
    budget = st.text_input("Budget")
    days = st.number_input("Number of Days", min_value=1, max_value=30)
    people = st.number_input("Number of Travellers")
    submitted = st.form_submit_button("Plan My Trip")

if submitted:
    with st.spinner("Planning your trip... This may take a few moments."):
        result = crew.kickoff(
            inputs={
                "origin": origin,
                "destination": destination,
                "budget": budget,
                "days": days,
                "people": people
            }
        )

    # ✅ Extract outputs
    research_output = result.tasks_output[0].raw
    budget_output = result.tasks_output[1].raw
    itinerary_output = result.tasks_output[2].raw

    # 📄 Display outputs in Streamlit
    st.subheader("📌 Research & Travel Insights")
    st.markdown(research_output)

    st.subheader("💰 Budget Breakdown (in INR)")
    st.markdown(budget_output)

    st.subheader("🗓️ Final Itinerary")
    st.markdown(itinerary_output)

    st.success("✅ Trip Plan Generated!")
    st.subheader("📄 Trip Details")
    st.markdown(result.raw)

    # ------------------ PDF GENERATION ------------------ #
    # Convert all tasks into one big HTML string
    full_html = ""
    for task in result.tasks_output:
        html_text = markdown.markdown(task.raw, extensions=["tables"])
        full_html += html_text + "<br><br>"

    # ✅ Streamlit-like CSS
    css = """
    <style>
        body { font-family: 'DejaVu Sans', Arial, sans-serif; margin: 40px; color: #262730; }
        h1, h2, h3, h4 { color: #FF4B4B; margin-top: 20px; }
        h2 { border-bottom: 2px solid #ddd; padding-bottom: 5px; }
        ul { margin: 10px 0; padding-left: 25px; }
        li { margin-bottom: 6px; }
        table { border-collapse: collapse; width: 100%; margin: 15px 0; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f4f4f4; }
        p { margin: 8px 0; line-height: 1.5; }
    </style>
    """

    # Final HTML with styling
    styled_html = f"""
    <html>
    <head>{css}</head>
    <body>
    <h1>🌍 Trip Plan: {origin} → {destination}</h1>
    {full_html}
    </body>
    </html>
    """

    # 📄 Dynamic filename
    safe_origin = origin.strip().replace(" ", "_")
    safe_destination = destination.strip().replace(" ", "_")
    pdf_filename = f"trip_plan_{safe_origin}_to_{safe_destination}.pdf"

    # ✅ Path to wkhtmltopdf (adjust if installed elsewhere)
    path_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

    # ✅ Generate PDF in memory (no saving to disk)
    # ✅ Ensure UTF-8 encoding
    options = {
        "encoding": "UTF-8"
    }
    pdf_bytes = pdfkit.from_string(styled_html, False, configuration=config, options=options)

    # ✅ Serve file for download
    st.download_button(
        label=f"📥 Download Trip Plan ({origin} → {destination})",
        data=pdf_bytes,
        file_name=pdf_filename,
        mime="application/pdf"
    )
