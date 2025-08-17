from crewai import Agent
from tools import search_tool
from llm import llm

# 🧭 Travel Researcher Agent (Finds transport, attractions, food, weather)
researcher = Agent(
    role="Travel Researcher",
    goal=(
        "Gather accurate and realistic information about destinations for {people} travelers, "
        "including transportation options (with correct durations and costs), key attractions, "
        "accommodation choices, local food cost per person per day, local transportation, and weather."
    ),
    verbose=True,
    memory=True,
    backstory=(
        "You are a knowledgeable travel researcher who specializes in gathering reliable, "
        "up-to-date details to help travelers make informed decisions. "
        "You carefully validate transport durations (e.g., no 24-hour train arriving the next morning), "
        "provide average food costs, and adjust all findings for the total group size."
    ),
    llm=llm,
    tools=[search_tool],  # Uses live search tool
    allow_delegation=True
)       

# 💰 Budget Planner Agent (Ensures costs stay within budget)
budget_planner = Agent(
    role="Budget Planner",
    goal=(
        "Create cost-effective plans for {people} travelers, ensuring all transportation, "
        "accommodation, meals, and activities stay within the set {budget}."
    ),
    verbose=True,
    memory=True,
    backstory=(
        "You are an experienced budget planner who ensures every trip provides great value "
        "without exceeding financial limits. You calculate total meal costs as "
        "(daily meal cost × number of days × number of travelers), and factor in transport, stay, and activities. "
        "If the budget is tight, you suggest trade-offs (e.g., budget hotels, cheaper transport)."
    ),
    llm=llm,  
    tools=[search_tool],  # Uses live search tool for cost verification
    allow_delegation=False
)

# 🗺️ Itinerary Planner Agent (Creates realistic day plans)
itinerary_planner = Agent(
    role="Itinerary Planner",
    goal=(
        "Design a balanced, {days}-day itinerary for {people} travelers from {origin} to {destination}, "
        "including realistic travel times, daily activities, meal breaks with costs, and rest periods — "
        "all while staying within the budget."
    ),
    verbose=True,
    memory=True,
    backstory=(
            "You are an expert in crafting enjoyable, organized travel plans that maximize "
            "experience while keeping schedules realistic. "
            "You strictly validate time consistency: no trip should arrive earlier than possible "
            "based on departure time and travel duration."
    ),
    llm=llm,  
    tools=[search_tool],
    allow_delegation=False
)
