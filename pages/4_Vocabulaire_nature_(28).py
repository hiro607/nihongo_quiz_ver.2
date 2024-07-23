import streamlit as st
import random

# 外枠と背景色を指定
style = """
<style>
div.my-question {
    text-align: center; 
    font-size: 70px; 
    font-family: 'Meiryo'; 
    padding:60px 10px;
    background-color: #f0f0f0;  /* 背景色 */
    border: 2px solid #ccc;     /* 枠線 */
    padding: 40px 20px;        /* パディング */
}
</style>
"""

st.write(style, unsafe_allow_html=True)

# 問題とクイズの辞書
nihongo_french_dictionary = {
    "雨（あめ）": "pluie",
    "雪（ゆき）": "neige",
    "風（かぜ）": "vent",
    "空（そら）": "ciel",
    "太陽（たいよう）": "soleil",
    "月（つき）": "lune",
    "星（ほし）": "étoile",
    "山（やま）": "montagne",
    "川（かわ）": "rivière",
    "海（うみ）": "mer",
    "湖（みずうみ）": "lac",
    "花（はな）": "fleur",
    "木（き）": "arbre",
    "森（もり）": "forêt",
    "緑（みどり）": "vert, verdure",
    "火（ひ）": "feu",
    "石（いし）": "pierre",
    "砂（すな）": "sable",
    "雲（くも）": "nuage",
    "虹（にじ）": "arc-en-ciel",
    "朝日（あさひ）": "lever du soleil",
    "夕日（ゆうひ）": "coucher du soleil",
    "光（ひかり）": "lumière",
    "嵐（あらし）": "tempête",
    "にわか雨（にわかあめ）": "averse",
    "風（かぜ）": "brise",
    "雹（ひょう）": "grêle",
    "土（つち）": "terre",
    "雷（かみなり）": "tonnerre",
}


# ランダムにクイズを選ぶ関数
def get_random_quiz(excluded_questions):
    available_questions = [q for q in nihongo_french_dictionary.keys() if q not in excluded_questions]
    if not available_questions:
        return None, None
    question = random.choice(available_questions)
    answer = nihongo_french_dictionary[question]
    return question, answer

# セッション情報の初期化
if 'remaining_quiz' not in st.session_state:
    st.session_state.remaining_quiz = 28
    st.session_state.score = 0
    st.session_state.asked_questions =[]
    st.session_state.question, st.session_state.answer = get_random_quiz(st.session_state.asked_questions)
    st.session_state.show_answer = False
    st.session_state.unknown_words = []

remaining_quiz = st.session_state.remaining_quiz
score = st.session_state.score

# Streamlitのアプリ
st.markdown("""
<h1 style="font-family: 'Segoe UI; text-align: center;">
    Flash cards Quiz 3  <br>  - nature -
</h1>
""", unsafe_allow_html=True)

# クイズが終了したかどうかを確認
if remaining_quiz == 0:
    st.markdown(f"<p style='font-family:Segoe UI; font-size: 22px; padding-top: 20px;'>Votre score est {score} points sur 28</p>", unsafe_allow_html=True)
    
    if st.session_state.unknown_words:
        st.markdown("<p style='font-family:Segoe UI; font-size: 22px;'>Mots à apprendre: </p>", unsafe_allow_html=True)
        for question, answer in st.session_state.unknown_words:
            st.markdown(f"<p style='font-family:Segoe UI; font-size: 20px;'>-{question} : {answer}</p>", unsafe_allow_html=True)   
    
    if st.button('Faire une fois de plus'):
        st.session_state.remaining_quiz = 28
        st.session_state.score = 0
        st.session_state.asked_questions =[]
        st.session_state.question, st.session_state.answer = get_random_quiz(st.session_state.asked_questions)
        st.session_state.show_answer = False
        st.session_state.unknown_words = []
        st.experimental_rerun()  

# アプリを再実行して新しいクイズを開始
else:
    st.markdown(f"<p style='font-family:Segoe UI; font-style: italic; font-size: 22px; padding-top: 40px;'>1. Lisez le mot ci-dessous et vérifiez le sens.</p>", unsafe_allow_html=True)

    question = st.session_state.question
    answer = st.session_state.answer

# テキストボックス
    st.write(f"""
        <div class="my-question">
            {question}
        </div>
    """, unsafe_allow_html=True)

    st.markdown(f"<p style='font-family:Segoe UI; font-style: italic; font-size: 22px; margin-top:25px;'>Que veut dire en français ?</p>", unsafe_allow_html=True)
    if st.button("Voir la signification"):
        st.session_state.show_answer = True

    if st.session_state.show_answer:
        st.markdown(f"<p style='font-family:Segoe UI; font-size: 20px;'>{question} veut dire ({answer})</p>", unsafe_allow_html=True)
    
    st.markdown("<p style='font-family:Segoe UI; font-style: italic; font-size: 22px; margin-top:25px;'>2. Connaissez-vous ce mot ?</p>", unsafe_allow_html=True)

    if st.button('Je connais'):
        st.session_state.remaining_quiz -= 1
        st.session_state.score += 1
        st.session_state.asked_questions.append(question)
        st.session_state.question, st.session_state.answer = get_random_quiz(st.session_state.asked_questions)
        st.session_state.show_answer = False
        st.experimental_rerun()

    if st.button('Je ne connais pas'):
        st.session_state.remaining_quiz -= 1
        st.session_state.score += 0
        st.session_state.asked_questions.append(question)
        st.session_state.unknown_words.append((question, answer))
        st.session_state.question, st.session_state.answer = get_random_quiz(st.session_state.asked_questions)
        st.session_state.show_answer = False
        st.experimental_rerun()

st.markdown(f"<p style='font-family:Segoe UI; font-size: 22px; margin-top:25px;'>-Nombre de questions restantes : {remaining_quiz}</p>", unsafe_allow_html=True)
st.markdown(f"<p style='font-family:Segoe UI; font-size: 22px;'>-Votre score : {score} points</p>", unsafe_allow_html=True)