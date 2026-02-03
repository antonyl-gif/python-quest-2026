import streamlit as st

st.set_page_config(
    page_title="Python Quest 2026",
    page_icon="🤖",
    layout="wide"
)

# ---------------- QUESTIONS ----------------
easy_r1 = [
    {"q":"Which prints a string?","o":["print(12)","print(True)",'print("hi")',"print(5.6)"],"a":'print("hi")'},
    {"q":"Immutable type?","o":["List","Set","String","Dict"],"a":"String"},
    {"q":"Mutable type?","o":["Tuple","Int","String","Dict"],"a":"Dict"},
    {"q":"// means?","o":["Divide","Floor divide","Add","Multiply"],"a":"Floor divide"},
    {"q":"Variables are?","o":["Fixed","Unknown","Only int","Only str"],"a":"Unknown"},
    {"q":"Correct input?","o":['x=input("name")','x=int("name")','input=x()','print(input)'],"a":'x=input("name")'},
    {"q":"After if comes?","o":["else","elif","when","loop"],"a":"elif"},
]

easy_r2 = [
    {"q":"Python is?","o":["Low-level","High-level","Binary","Assembly"],"a":"High-level"},
    {"q":"Creator of Python?","o":["Guido","Linus","Dennis","Bill"],"a":"Guido"},
    {"q":"Python named after?","o":["Snake","Movie","Comedy","Game"],"a":"Comedy"},
    {"q":"File extension?","o":[".pt",".py",".p",".python"],"a":".py"},
    {"q":"Python is?","o":["Compiled","Interpreted","Binary","None"],"a":"Interpreted"},
    {"q":"Used in AI?","o":["No","Yes","Only games","Only web"],"a":"Yes"},
    {"q":"Python 2 ended?","o":["2015","2018","2020","2022"],"a":"2020"},
]

medium_r1 = [
    {"q":"Correct list?","o":["(1,2)","{1,2}","[1,2]","1,2"],"a":"[1,2]"},
    {"q":"len([1,2,3])?","o":["2","3","4","Error"],"a":"3"},
    {"q":"Boolean values?","o":["yes/no","0/1","True/False","on/off"],"a":"True/False"},
    {"q":"Index starts at?","o":["0","1","-1","None"],"a":"0"},
    {"q":"Keyword to loop?","o":["repeat","for","when","loop"],"a":"for"},
    {"q":"Comment symbol?","o":["//","#","/*","--"],"a":"#"},
    {"q":"Function keyword?","o":["func","define","def","fun"],"a":"def"},
]

medium_r2 = [
    {"q":"Output of 3*2**2?","o":["12","18","6","9"],"a":"12"},
    {"q":"Tuple is?","o":["Mutable","Immutable","Both","None"],"a":"Immutable"},
    {"q":"Dictionary uses?","o":["()","[]","{}","<>"],"a":"{}"},
    {"q":"Input returns?","o":["int","str","bool","float"],"a":"str"},
    {"q":"Logical AND?","o":["&&","and","&","AND"],"a":"and"},
    {"q":"Exit loop?","o":["stop","exit","break","end"],"a":"break"},
    {"q":"Add to list?","o":["add()","push()","append()","insert()"],"a":"append()"},
]

hard_r1 = [
    {"q":"What is PEP 8?","o":["Library","Style guide","Compiler","IDE"],"a":"Style guide"},
    {"q":"Lambda is?","o":["Loop","Function","Class","Module"],"a":"Function"},
    {"q":"None means?","o":["0","Empty","Null value","False"],"a":"Null value"},
    {"q":"Try/except used for?","o":["Loops","Errors","Functions","Files"],"a":"Errors"},
    {"q":"Global keyword?","o":["share","global","public","all"],"a":"global"},
    {"q":"__init__ is?","o":["Method","Variable","Loop","File"],"a":"Method"},
    {"q":"OOP stands for?","o":["Order","Object Oriented","Open","Only"],"a":"Object Oriented"},
]

hard_r2 = [
    {"q":"Inheritance allows?","o":["Reuse","Delete","Hide","Stop"],"a":"Reuse"},
    {"q":"Module is?","o":["File","Class","Loop","Variable"],"a":"File"},
    {"q":"Import math gives?","o":["Error","Functions","Loop","None"],"a":"Functions"},
    {"q":"is vs ==?","o":["Same","Identity vs Equality","No diff","Error"],"a":"Identity vs Equality"},
    {"q":"Recursion is?","o":["Loop","Self-calling","Error","Stop"],"a":"Self-calling"},
    {"q":"Set removes?","o":["Order","Duplicates","Values","Keys"],"a":"Duplicates"},
    {"q":"Virtual env is?","o":["OS","Folder","Isolated env","Compiler"],"a":"Isolated env"},
]

levels = {
    "Easy": [easy_r1, easy_r2],
    "Medium": [medium_r1, medium_r2],
    "Hard": [hard_r1, hard_r2]
}

# ---------------- SESSION STATE ----------------
if "level" not in st.session_state:
    st.session_state.level = None
    st.session_state.round = 0
    st.session_state.q = 0
    st.session_state.score = 0
    st.session_state.show_answer = False
    st.session_state.choice = None

# ---------------- FUNCTIONS ----------------
def reset():
    st.session_state.level = None
    st.session_state.round = 0
    st.session_state.q = 0
    st.session_state.score = 0
    st.session_state.show_answer = False
    st.session_state.choice = None
    st.rerun()

def run_quiz(questions):
    q = questions[st.session_state.q]
    st.subheader(f"Question {st.session_state.q+1}/7")
    st.write(q["q"])

    # Radio buttons only if user has not submitted yet
    if not st.session_state.show_answer:
        st.session_state.choice = st.radio(
            "Choose:",
            q["o"],
            key=f"{st.session_state.level}_{st.session_state.round}_{st.session_state.q}"
        )
        if st.button("Submit"):
            st.session_state.show_answer = True
            st.rerun()
    else:
        if st.session_state.choice == q["a"]:
            st.success("✅ Correct!")
        else:
            st.error("❌ Wrong!")
        st.info(f"💡 Correct answer: **{q['a']}**")
        if st.session_state.choice == q["a"]:
            st.session_state.score += 1
        if st.button("Next Question"):
            st.session_state.q += 1
            st.session_state.show_answer = False
            st.session_state.choice = None
            st.rerun()

# ---------------- UI ----------------
st.title("🤖 Python Quest 2026")

if not st.session_state.level:
    st.subheader("Choose Difficulty")
    c1, c2, c3 = st.columns(3)
    if c1.button("🟢 Easy"): st.session_state.level="Easy"; st.rerun()
    if c2.button("🟡 Medium"): st.session_state.level="Medium"; st.rerun()
    if c3.button("🔴 Hard"): st.session_state.level="Hard"; st.rerun()
else:
    st.info(f"Level: {st.session_state.level} | Round {st.session_state.round+1} | Score: {st.session_state.score}")

    current = levels[st.session_state.level][st.session_state.round]

    if st.session_state.q < 7:
        run_quiz(current)
    else:
        if st.session_state.round == 0:
            if st.session_state.score >= 5:
                st.success("🎉 Congratulations! You entered Round 2!")
                if st.button("Continue to Round 2"):
                    st.session_state.round = 1
                    st.session_state.q = 0
                    st.session_state.show_answer = False
                    st.session_state.choice = None
                    st.rerun()
            else:
                st.error("❌ Score 5 or more to continue")
                st.button("Restart", on_click=reset)
        else:
            st.balloons()
            st.success(f"🏆 Completed {st.session_state.level}! Final Score: {st.session_state.score}")
            st.subheader("📋 All Answers for this Level:")
            for r in levels[st.session_state.level]:
                for i, q in enumerate(r):
                    st.markdown(f"**Q{i+1}:** {q['q']}")
                    st.markdown(f"**Answer:** {q['a']}")
                    st.markdown("---")
            st.button("Play Again", on_click=reset)
