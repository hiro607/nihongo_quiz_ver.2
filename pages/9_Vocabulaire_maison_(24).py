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
    "部屋（へや）": "chambre, pièce",
    "浴室（よくしつ）": "salle de bain",
    "ベランダ": "balcon",
    "玄関（げんかん）": "entrée",
    "階段（かいだん）": "escalier",
    "台所（だいどころ）": "cuisine",
    "リビングルーム": "salon",
    "寝室（しんしつ）": "chambre à coucher",
    "洗面所（せんめんじょ）": "lavabo",
    "トイレ": "toilettes",
    "庭（にわ）": "jardin",
    "屋根（やね）": "toit",
    "窓（まど）": "fenêtre",
    "壁（かべ）": "mur",
    "床（ゆか）": "plancher",
    "天井（てんじょう）": "plafond",
    "廊下（ろうか）": "couloir",
    "ガレージ": "garage",
    "地下室（ちかしつ）": "sous-sol",
    "ドア": "porte",
    "棚（たな）": "étagère",
    "和室（わしつ）": "pièce japonaise",
    "雨戸（あまど）": "volet",
    "ダイニング": "salle à manger"
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
    st.session_state.remaining_quiz = 24
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
    Flash cards Quiz 3  <br>  - maison -
</h1>
""", unsafe_allow_html=True)

# クイズが終了したかどうかを確認
if remaining_quiz == 0:
    st.markdown(f"<p style='font-family:Segoe UI; font-size: 22px; padding-top: 20px;'>Votre score est {score} points sur 24</p>", unsafe_allow_html=True)
    
    if st.session_state.unknown_words:
        st.markdown("<p style='font-family:Segoe UI; font-size: 22px;'>Mots à apprendre: </p>", unsafe_allow_html=True)
        for question, answer in st.session_state.unknown_words:
            st.markdown(f"<p style='font-family:Segoe UI; font-size: 20px;'>-{question} : {answer}</p>", unsafe_allow_html=True)   
    
    if st.button('Faire une fois de plus'):
        st.session_state.remaining_quiz = 24
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