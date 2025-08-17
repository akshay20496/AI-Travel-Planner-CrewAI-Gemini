from crewai import Task
from tools import search_tool
from agents import researcher, budget_planner, itinerary_planner

# 📝 Travel Research Task
research_task = Task(
    description=(
        "Research travel from {origin} to {destination} for exactly {days} days and {days} nights "
        "for {people} people. Collect realistic information on:\n"
        "1. Transport options (flights, trains, buses) with **accurate travel times and costs**.\n"
        "2. Key attractions with timings and entry fees.\n"
        "3. Accommodation options with nightly rates.\n"
        "4. Local transportation methods and approximate fares.\n"
        "5. Local food options with **average daily meal cost per person**.\n"
        "6. Current weather at the destination.\n\n"
        "⚠️ Ensure that travel durations are realistic and consistent (e.g., a 24-hour train cannot arrive the next morning).\n"
        "Do not include plans for any more or fewer days than specified."
    ),
    expected_output=(
        "A structured research report for {people} people covering exactly {days} days from {origin} to {destination}, "
        "with transport (time + cost), attractions, accommodations, food cost estimates, and weather."
    ),
    tools=[search_tool], # Uses live search tool for accurate data
    agent=researcher
)

# 💲 Budget Estimation Task
budget_task = Task(
    description=(
        "Using the research, calculate a complete budget for {people} people within {budget}.\n"
        "Include:\n"
        "1. Transport (round trip).\n"
        "2. Accommodation ({days} nights × per-night rate).\n"
        "3. Meals (daily meal cost × {days} × {people}).\n"
        "4. Activities and attraction fees.\n"
        "5. Local transportation.\n\n"
        "⚠️ Make sure the total stays within {budget} and specify trade-offs if necessary (e.g., budget hotel vs. premium stay)."
    ),
    expected_output=(
        "A detailed cost breakdown for {people} people including transport, stay, meals, activities, "
        "local transport, and total estimate compared against {budget}."
    ),
    tools=[search_tool], # Uses live search tool for budget options
    agent=budget_planner
)

# 📅 Itinerary Planning Task
itinerary_task = Task(
    description=(
        "Using the research and budget, create a realistic {days}-day itinerary for {people} people "
        "from {origin} to {destination}.\n\n"
        "The itinerary must include:\n"
        "1. Travel times and modes of transport with accurate, realistic durations.\n"
        "2. Arrival times = departure time + travel duration (no early arrivals).\n"
        "3. Activities per day with start and end times that fit the day’s timeline.\n"
        "4. Meal breaks with estimated food costs (breakfast, lunch, dinner).\n"
        "5. Adequate rest/sleep periods to prevent overpacked schedules.\n"
        "6. Daily and total cost summary.\n\n"
        "⚠️ Constraints:\n"
        "- If a journey takes overnight or longer, reflect this properly in the next day’s schedule.\n"
        "- Do not allow overlapping activities or impossible travel timings.\n"
        "- Ensure the entire plan is feasible for {people} people within the {budget}."
    ),
    expected_output=(
        "A detailed, realistic {days}-day itinerary for {people} people traveling from {origin} to {destination}. "
        "The output must include:\n"
        "- Transport details with accurate departure, arrival times, and realistic durations.\n"
        "- Day-wise schedule of activities with proper start and end times (no overlaps).\n"
        "- Meal breaks (breakfast, lunch, dinner) with estimated costs.\n"
        "- Adequate rest periods and overnight stays when needed.\n"
        "- Daily cost breakdown and total trip cost summary within the {budget}."
    ),
    tools=[search_tool], # Uses live search tool for itinerary details
    agent=itinerary_planner
)
