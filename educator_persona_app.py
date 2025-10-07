
import streamlit as st

st.set_page_config(page_title="Educator Persona Profiler", layout="centered")

st.title("🔮 Educator Persona Profiler")
st.write("Answer the questions below to discover your educator persona and receive a personalized message of affirmation.")

# Mapping for multiple-choice options to personae
persona_map = {
    "A": "Inquisitus – The Curious Researcher",
    "B": "Evaluon – The Systematic Assessor",
    "C": "Counselix – The Guiding Listener",
    "D": "Wellcara – The Wellness Guardian",
    "E": "Inspiria – The Passionate Educator",
    "F": "Politexis – The Policy Architect",
    "G": "Equitus – The Justice Seeker",
    "H": "Transformyx – The Change Catalyst",
    "I": "Globalis – The Cultural Connector",
    "J": "Strategon – The Institutional Builder",
    "K": "Technova – The Digital Innovator",
    "L": "Reflectes – The Philosophical Dreamer"
}

# Multiple-choice questions
st.header("🧠 Personality Questions")

questions = [
    ("What motivates you most in your work or studies?", list(persona_map.keys())),
    ("What’s your ideal work environment?", list(persona_map.keys())),
    ("How do you approach challenges?", list(persona_map.keys())),
    ("What’s your superpower in education?", list(persona_map.keys())),
    ("What kind of legacy do you want to leave?", list(persona_map.keys()))
]

responses = []
for q, options in questions:
    choice = st.radio(q, options, key=q)
    responses.append(choice)

# Determine dominant persona
from collections import Counter
persona_counts = Counter(responses)
dominant_letter = persona_counts.most_common(1)[0][0]
dominant_persona = persona_map[dominant_letter]

# Sliding-scale questions
st.header("🌡️ Mood & Focus Sliders")

focus = st.slider("How would you define your professional focus?", 0, 100, 50, format="Research ↔ Practice")
workload = st.slider("What is your current workload like?", 0, 100, 50, format="Lax ↔ Slammed")
morale = st.slider("How would you characterize your morale?", 0, 100, 50, format="Unappreciated ↔ Well-rewarded")
disposition = st.slider("What is your current disposition?", 0, 100, 50, format="Reflection ↔ Engagement")
impact = st.slider("Do you feel that you are making a difference?", 0, 100, 50, format="No ↔ Yes")

# Generate horoscope-style message
def generate_message(persona, focus, workload, morale, disposition, impact):
    base_messages = {
        "Inquisitus – The Curious Researcher": "Your curiosity fuels discovery. You ask the questions that others overlook, and your insights shape the future of learning.",
        "Evaluon – The Systematic Assessor": "You bring clarity through data. Your precision and analysis help schools understand what works and why.",
        "Counselix – The Guiding Listener": "You listen deeply and guide with care. Your presence creates safe spaces for growth and healing.",
        "Wellcara – The Wellness Guardian": "You protect balance and well-being. Your calm and compassion help others thrive.",
        "Inspiria – The Passionate Educator": "You ignite minds and hearts. Your energy inspires learners to reach their full potential.",
        "Politexis – The Policy Architect": "You shape systems with foresight. Your work builds the structures that support equitable education.",
        "Equitus – The Justice Seeker": "You champion fairness and inclusion. Your advocacy opens doors and transforms lives.",
        "Transformyx – The Change Catalyst": "You lead transformation. Your bold ideas and actions drive progress.",
        "Globalis – The Cultural Connector": "You bridge worlds. Your global perspective enriches every classroom and conversation.",
        "Strategon – The Institutional Builder": "You build strong foundations. Your leadership strengthens schools and communities.",
        "Technova – The Digital Innovator": "You create the future. Your tech-savvy solutions expand possibilities for learning.",
        "Reflectes – The Philosophical Dreamer": "You ponder the deeper truths. Your reflections bring wisdom to education’s purpose."
    }

    tone = ""
    if workload > 70:
        tone += "Even under pressure, "
    elif workload < 30:
        tone += "With space to breathe, "

    if morale < 40:
        tone += "remember your worth and impact. "
    elif morale > 70:
        tone += "your efforts are seen and appreciated. "

    if impact < 40:
        tone += "Even when change feels distant, your work matters. "
    elif impact > 70:
        tone += "You're making a real difference—keep going. "

    if disposition < 50:
        tone += "Take time to reflect and recharge. "
    else:
        tone += "Stay engaged—your momentum is powerful. "

    if focus < 50:
        tone += "Your thoughtful approach brings depth to practice."
    else:
        tone += "Your hands-on work brings ideas to life."

    return base_messages[persona] + "\n\n" + tone

# Display results
st.header("✨ Your Educator Persona")
st.subheader(dominant_persona)

message = generate_message(dominant_persona, focus, workload, morale, disposition, impact)
st.write(message)
