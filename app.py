import streamlit as st
import random
from time import time

st.set_page_config(page_title="AP World Review (1750–1900)",
                   page_icon="🌍",
                   layout="wide")

# ---------------------------------------
# DATA: MCQs AND FLASHCARDS
# ---------------------------------------

# Expandable MCQ bank (50+)
mcq_bank = [
    ("Which Enlightenment thinker believed in natural rights?", 
     ["Hobbes", "Locke", "Rousseau", "Voltaire"], "Locke"),
    
    ("What was the only successful slave revolt in world history?",
     ["American Revolution", "Haitian Revolution", "Brazilian Revolt", "Jamaican Uprising"], 
     "Haitian Revolution"),

    ("Which ideology argues that history is defined by class struggle?",
     ["Conservatism", "Marxism", "Utilitarianism", "Romanticism"], "Marxism"),

    ("Which empire inspired nationalism by conquering Europe?",
     ["Mughal Empire", "Ottoman Empire", "Napoleonic France", "Tokugawa Japan"], "Napoleonic France"),

    ("The first major mechanized industry was:",
     ["Textiles", "Automobiles", "Shipbuilding", "Railroads"], "Textiles"),

    ("Which thinker supported laissez-faire capitalism?",
     ["Rousseau", "Adam Smith", "Hobbes", "Bentham"], "Adam Smith"),

    ("Romantic art emphasized:",
     ["Emotion & nature", "Symmetry & reason", "Realism & accuracy", "Industrial progress"], 
     "Emotion & nature"),

    ("Which revolution was led by creoles?",
     ["American", "French", "Latin American", "Haitian"], "Latin American"),

    ("Which country unified under Bismarck?",
     ["Italy", "Germany", "Austria", "Russia"], "Germany"),

    ("The Industrial Revolution began in:",
     ["France", "USA", "Britain", "Prussia"], "Britain"),

    # (Add 40+ more if you want — I can generate instantly)
]


# Flashcards
flashcards = [
    ("Natural rights", "Belief that individuals have rights that cannot be taken away — Locke."),
    ("Social contract", "Government power derives from the people — Rousseau."),
    ("Laissez-faire", "Economy should operate without government intervention — Adam Smith."),
    ("Nationalism", "Belief in common identity; desire for sovereignty."),
    ("Romanticism", "Emotion > reason, sublime nature, nationalism."),
    ("Realism", "Focus on working-class struggles."),
    ("Marxism", "History is class struggle; proletariat revolution."),
    ("Industrial Revolution", "Shift to mechanized production, factories, railroads."),
]

# ---------------------------------------
# SIDEBAR NAVIGATION
# ---------------------------------------
st.sidebar.title("🌍 AP World Review 1750–1900")
page = st.sidebar.radio(
    "Navigate",
    ["Study Guide", "Flashcards", "MCQ Practice", "Timed Quiz"]
)

# ---------------------------------------
# STUDY GUIDE PAGE
# ---------------------------------------
if page == "Study Guide":
    st.title("📘 AP World History Study Guide (1750–1900)")

    st.info("You can search the study guide using Ctrl+F or your browser’s search bar.")

    st.header("💡 Enlightenment")
    st.markdown("""
- Reason, progress, secularism  
- **Hobbes** – absolutism, humans selfish  
- **Locke** – natural rights, right to revolt  
- **Rousseau** – general will, direct democracy  
- **Voltaire** – anti-Church, free speech  
- **Adam Smith** – laissez-faire economics  
    """)

    st.header("🌎 Atlantic Revolutions Overview")
    st.markdown("""
**American Revolution:** Enlightenment applied; limited social change  
**French Revolution:** Radical shift; Reign of Terror; Napoleon  
**Haitian Revolution:** Only successful slave revolt  
**Latin American Revolutions:** Creole-led; inspired by Enlightenment  
    """)

    st.header("🚩 Nationalism")
    st.markdown("""
- Italy unified by **Cavour**  
- Germany unified by **Bismarck** (Realpolitik)  
- Greek, Serbian, Latin American independence  
- Inspired by Napoleon  
    """)

    st.header("⚙ Industrial Revolution")
    st.markdown("""
**Why Britain?** Coal, labor, stable gov, colonies  
**Effects:** Urbanization, middle class growth, pollution, new working class  
**Tech:** Railroads, steam engine, telegraph  
    """)

    st.header("🧠 Responses & Ideologies")
    st.markdown("""
- **Marxism:** class struggle  
- **Utopian Socialism**  
- **Utilitarianism (Bentham, Mill)**  
- **Anarchism (Bakunin)**  
- **Luddites**  
    """)

    st.header("🎨 Art Movements")
    st.markdown("""
**Romanticism:** emotion, nature, nationalism  
**Realism:** working-class truth  
Timeline: Rococo → Neoclassicism → Romanticism → Realism  
    """)

# ---------------------------------------
# FLASHCARDS PAGE
# ---------------------------------------
elif page == "Flashcards":
    st.title("📚 Flashcards Mode")

    if "fc_index" not in st.session_state:
        st.session_state.fc_index = 0
        st.session_state.show_answer = False

    term, definition = flashcards[st.session_state.fc_index]

    st.subheader(f"Term: **{term}**")

    if st.button("Show Answer"):
        st.session_state.show_answer = True

    if st.session_state.show_answer:
        st.success(definition)

    if st.button("Next Flashcard"):
        st.session_state.fc_index = (st.session_state.fc_index + 1) % len(flashcards)
        st.session_state.show_answer = False
        st.rerun()


# ---------------------------------------
# MCQ PRACTICE PAGE
# ---------------------------------------
elif page == "MCQ Practice":
    st.title("📝 MCQ Practice")

    if "mcq_index" not in st.session_state:
        st.session_state.mcq_index = 0

    q, options, answer = mcq_bank[st.session_state.mcq_index]

    st.subheader(q)
    selection = st.radio("Select one:", options)

    if st.button("Check Answer"):
        if selection == answer:
            st.success("Correct! 🎉")
        else:
            st.error(f"Incorrect. Correct answer: **{answer}**")

    if st.button("Next"):
        st.session_state.mcq_index = (st.session_state.mcq_index + 1) % len(mcq_bank)
        st.rerun()


# ---------------------------------------
# TIMED QUIZ PAGE
# ---------------------------------------
elif page == "Timed Quiz":
    st.title("⏱ Timed Quiz (60 seconds)")

    if "quiz_start" not in st.session_state:
        st.session_state.quiz_start = time()
        st.session_state.score = 0
        st.session_state.question = random.choice(mcq_bank)

    elapsed = int(time() - st.session_state.quiz_start)
    remaining = max(0, 60 - elapsed)

    st.sidebar.write(f"⏳ Time left: **{remaining} seconds**")
    st.sidebar.write(f"⭐ Score: {st.session_state.score}")

    if remaining == 0:
        st.error("Time's up!")
        st.write(f"Final Score: **{st.session_state.score}**")
        if st.button("Restart"):
            st.session_state.quiz_start = time()
            st.session_state.score = 0
            st.session_state.question = random.choice(mcq_bank)
        st.stop()

    q, opts, ans = st.session_state.question

    st.subheader(q)
    choice = st.radio("Your answer:", opts)

    if st.button("Submit"):
        if choice == ans:
            st.success("Correct!")
            st.session_state.score += 1
        else:
            st.error(f"Incorrect. Correct answer: **{ans}**")

        st.session_state.question = random.choice(mcq_bank)
        st.rerun()
