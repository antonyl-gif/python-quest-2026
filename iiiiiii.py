# streamlit_app.py
import streamlit as st
import random

st.set_page_config(page_title="Python Quest 2026", page_icon="🤖", layout="wide")

st.title("🧩 Python Quest 2026 Quiz 🧩")
st.markdown("""
Welcome to Python Quest 2026!  

- **Easy → Medium → Hard levels**  
- **2 rounds per difficulty**  
- Must score **5 or more** in Round 1 to enter Round 2  
- Timer runs for the whole round  
- Correct and incorrect answers are shown immediately  
""")

# ---------------- Quiz Data ----------------
easy_round1 = [
    {"q": "Which prints a string?", "options": ["print(12345)", 'print("hello")', "print(12.5)", "print(True)"],
     "answer": 'print("hello")'},
    {"q": "Which data type is immutable?", "options": ["Dictionary", "Set", "String", "Function"], "answer": "String"},
    {"q": "Which is mutable?", "options": ["Integer", "Tuple", "String", "Dictionary"], "answer": "Dictionary"},
    {"q": "What does // do?", "options": ["Adds numbers", "Shows decimal", "Removes decimal", "Multiplies"],
     "answer": "Removes decimal"},
    {"q": "Variables are:", "options": ["Fixed numbers", "Unknown values", "Only strings", "Only integers"],
     "answer": "Unknown values"},
    {"q": "Take string input correctly?",
     "options": ['k = input("name?")', 'k = int("name")', 'input = k("name")', 'print(input)'],
     "answer": 'k = input("name?")'},
    {"q": "Keyword after if for more conditions?", "options": ["else", "when", "elif", "repeat"], "answer": "elif"}
]

easy_round2 = [
    {"q": "What is Python?", "options": ["Snake", "Language", "Movie", "Car"], "answer": "Language"},
    {"q": "Who created Python?",
     "options": ["Guido van Rossum", "Dennis Ritchie", "James Gosling", "Bjarne Stroustrup"],
     "answer": "Guido van Rossum"},
    {"q": "Year Python released?", "options": ["1989", "1991", "1995", "2000"], "answer": "1991"},
    {"q": "Python named after?", "options": ["Snake", "TV show", "Greek Myth", "Pet"], "answer": "TV show"},
    {"q": "Which version ended Python 2?", "options": ["2.5", "2.7", "3.0", "3.5"], "answer": "2.7"},
    {"q": "Mutable data type?", "options": ["Set", "String", "Tuple", "Integer"], "answer": "Set"},
    {"q": "Immutable data type?", "options": ["List", "Tuple", "Set", "Dict"], "answer": "Tuple"}
]

# You can add medium_round1/2 and hard_round1/2 similarly
medium_round1 = [
    {"q": "What does BDFL stand for?",
     "options": ["Best Developer For Language", "Benevolent Dictator For Life", "Basic Dev Framework",
                 "Binary Data Format"], "answer": "Benevolent Dictator For Life"},
    {"q": "Python 3.0 release year?", "options": ["2005", "2007", "2008", "2010"], "answer": "2008"},
    {"q": "Python philosophy focus?", "options": ["Speed", "Readability", "Memory", "Complexity"],
     "answer": "Readability"},
    {"q": "Python is ___ typed?", "options": ["Strong", "Weak", "No", "Both"], "answer": "Strong"},
    {"q": "What is PEP8?", "options": ["Style Guide", "Library", "Game", "Function"], "answer": "Style Guide"},
    {"q": "Which is Python IDE?", "options": ["PyCharm", "Chrome", "VS Code", "None"], "answer": "PyCharm"},
    {"q": "Python is ___ programming?", "options": ["Procedural", "OOP", "Functional", "All"], "answer": "All"}
]

medium_round2 = [
    {"q": "Python uses ___ for comments?", "options": ["//", "#", "/*", "$$"], "answer": "#"},
    {"q": "Python version with f-strings?", "options": ["3.4", "3.5", "3.6", "3.7"], "answer": "3.6"},
    {"q": "List append method?", "options": ["add()", "append()", "push()", "insert()"], "answer": "append()"},
    {"q": "Python interprets ___?", "options": ["Code", "Text", "HTML", "All"], "answer": "Code"},
    {"q": "Keyword to define function?", "options": ["fun", "def", "function", "define"], "answer": "def"},
    {"q": "Python package installer?", "options": ["pip", "npm", "apt", "gem"], "answer": "pip"},
    {"q": "Python is ___ typed?", "options": ["Dynamically", "Statically", "Strong", "Weak"], "answer": "Dynamically"}
]


# ---------------- Quiz Logic ----------------
def run_quiz(round_data):
    st.session_state.score = 0
    st.session_state.index = 0
    total = len(round_data)

    timer_placeholder = st.empty()

    # Timer (for whole round, 2 minutes)
    import time
    start_time = time.time()
    total_time = 120  # seconds

    while st.session_state.index < total:
        q = round_data[st.session_state.index]
        st.subheader(f"Q{st.session_state.index + 1}: {q['q']}")
        choice = st.radio("Choose answer:", q["options"], key=st.session_state.index)
        if st.button("Submit Answer", key=f"btn{st.session_state.index}"):
            if choice == q["answer"]:
                st.success("Correct ✅")
                st.session_state.score += 1
            else:
                st.error(f"Incorrect ❌. Correct answer: {q['answer']}")
            st.session_state.index += 1
        # Timer display
        elapsed = int(time.time() - start_time)
        remaining = total_time - elapsed
        mins, secs = divmod(max(remaining, 0), 60)
        timer_placeholder.markdown(f"⏱ Time left for round: {mins:02d}:{secs:02d}")
        if remaining <= 0:
            st.warning("Time's up for this round!")
            break

    st.info(f"Round over! Your score: {st.session_state.score}/{total}")
    if st.session_state.score >= 5:
        st.balloons()
        st.success("🎉 Congratulations! You passed this round and can enter the next round! 🎉")
    else:
        st.warning("😢 You did not score enough to enter the next round. Try again!")


# ---------------- Main App ----------------
difficulty = st.selectbox("Select Difficulty Level:", ["Easy", "Medium"])  # Hard can be added
if st.button("Start Quiz"):
    if difficulty == "Easy":
        st.session_state.score = 0
        st.session_state.index = 0
        st.experimental_rerun()
    elif difficulty == "Medium":
        st.session_state.score = 0
        st.session_state.index = 0
        st.experimental_rerun()

if 'score' in st.session_state and st.session_state.score == 0:
    # Show Round 1 first
    if difficulty == "Easy":
        run_quiz(easy_round1)
    elif difficulty == "Medium":
        run_quiz(medium_round1)

