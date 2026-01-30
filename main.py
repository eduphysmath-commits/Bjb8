import streamlit as st
import requests
import streamlit.components.v1 as components
import json

# --- 1. БАЗА БАПТАУЛАРЫ ---
URL = "https://bjqoazdkiyhrdrfkkgaz.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJqcW9hemRraXlocmRyZmtrZ2F6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3Njk3NTM4NjIsImV4cCI6MjA4NTMyOTg2Mn0.0t4S6fa9CmYa6WBdDvkVr4V4H91wLx9xLYtcEdriX4I"
TABLE_NAME = "tjb_8_synyp" # Жаңа кесте аты

st.set_page_config(page_title="8-СЫНЫП ФИЗИКА БЖБ", layout="wide", page_icon="⚡")

if 'submitted' not in st.session_state:
    st.session_state.submitted = False

# --- 2. СТИЛЬ ---
st.markdown("""
    <style>
    * { -webkit-user-select: none; user-select: none; } 
    .stRadio > div { background-color: white; padding: 15px; border-radius: 10px; border: 1px solid #e0e0e0; margin-bottom: 5px; }
    .stTextArea textarea { font-size: 16px; border: 2px solid #f0f2f6; }
    </style>
""", unsafe_allow_html=True)

def send_data(payload):
    headers = {"apikey": KEY, "Authorization": f"Bearer {KEY}", "Content-Type": "application/json"}
    return requests.post(f"{URL}/rest/v1/{TABLE_NAME}", json=payload, headers=headers)

# --- 3. БАСТЫ БЕТ ---
st.title("⚡ 8-СЫНЫП ФИЗИКА: ЖЫЛУ ЖӘНЕ ЭЛЕКТРОСТАТИКА")

if st.session_state.submitted:
    st.balloons()
    st.success("✅ Жұмысың қабылданды! Нәтижені төменнен іздеп көр.")
else:
    st.info("⏱ Максималды ұпай: 20 ұпай. Тақырыптар: Жылу құбылыстары, Термодинамика, Электр заряды, Кулон заңы.")
    
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Оқушының аты-жөні:", placeholder="Мысалы: Оспанов Арман")
    with col2:
        s_class = st.selectbox("Сыныбыңыз:", ["8 А", "8 Б", "8 В", "8 Г"])

    if name:
        # ANTI-CHEAT JS
        components.html(f"""
            <script>
            let audioCtx = new (window.AudioContext || window.webkitAudioContext)();
            let alarmInterval;
            let isSubmitting = false;

            function startAlarm() {{
                if (isSubmitting) return;
                if (audioCtx.state === 'suspended') {{ audioCtx.resume(); }}
                alarmInterval = setInterval(() => {{
                    let osc = audioCtx.createOscillator();
                    let gain = audioCtx.createGain();
                    osc.type = 'sawtooth';
                    osc.frequency.setValueAtTime(880, audioCtx.currentTime);
                    gain.gain.setValueAtTime(0.5, audioCtx.currentTime);
                    gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.2);
                    osc.connect(gain);
                    gain.connect(audioCtx.destination);
                    osc.start();
                    osc.stop(audioCtx.currentTime + 0.2);
                }}, 300);
            }}

            function stopAlarm() {{ clearInterval(alarmInterval); }}

            document.addEventListener("visibilitychange", function() {{
                if (document.hidden && !isSubmitting) {{
                    startAlarm();
                    setTimeout(function() {{
                        if (document.hidden && !isSubmitting) {{
                            const payload = {{
                                student_name: "{name}",
                                student_class: "{s_class}",
                                status: "cheated",
                                ai_feedback: "Жұмыс ЖОЙЫЛДЫ: Дабыл іске қосылды."
                            }};
                            fetch('{URL}/rest/v1/{TABLE_NAME}', {{
                                method: 'POST',
                                headers: {{ 'apikey': '{KEY}', 'Authorization': 'Bearer {KEY}', 'Content-Type': 'application/json' }},
                                body: JSON.stringify(payload)
                            }}).then(() => {{ 
                                isSubmitting = true;
                                stopAlarm();
                                window.parent.location.reload(); 
                            }});
                        }}
                    }}, 5000);
                }} else {{
                    stopAlarm();
                }}
            }});

            window.onbeforeunload = function() {{
                isSubmitting = true;
                stopAlarm();
            }};
            </script>
        """, height=0)

        with st.form("exam_8_physics"):
            st.subheader("📍 А БӨЛІМІ: Тест тапсырмалары (10 ұпай)")
            q1 = st.radio("1. Ішкі энергияның өлшем бірлігі қандай?", ["A) Ватт", "B) Джоуль", "C) Ньютон", "D) Паскаль"], index=None)
            q2 = st.radio("2. Жылу берілудің қай түрі вакуумда жүзеге асады?", ["A) Конвекция", "B) Жылу өткізгіштік", "C) Сәуле шығару", "D) Диффузия"], index=None)
            q3 = st.radio("3. Судың қайнау температурасы қалыпты жағдайда қанша?", ["A) 0°C", "B) 80°C", "C) 100°C", "D) 273°C"], index=None)
            q4 = st.radio("4. Термодинамиканың 1-заңының формуласы:", ["A) Q = ΔU + A", "B) Q = cmΔt", "C) η = A/Q", "D) pV = nRT"], index=None)
            q5 = st.radio("5. Булану кезінде сұйықтықтың температурасы қалай өзгереді?", ["A) Жоғарылайды", "B) Төмендейді", "C) Өзгермейді", "D) Басында артады"], index=None)
            q6 = st.radio("6. Элементар электр зарядының мәні қанша?", ["A) 1.6 * 10^-19 Кл", "B) 9 * 10^9 Кл", "C) 1.6 * 10^-31 Кл", "D) 1 Кл"], index=None)
            q7 = st.radio("7. Аттас зарядтар (+ және +) қалай әрекеттеседі?", ["A) Тартылады", "B) Тебіледі", "C) Әрекеттеспейді", "D) Бейтараптанады"], index=None)
            q8 = st.radio("8. Дененің электрленгенін анықтайтын аспап:", ["A) Термометр", "B) Барометр", "C) Электроскоп", "D) Спидометр"], index=None)
            q9 = st.radio("9. Кулон заңының формуласы:", ["A) F = ma", "B) F = k*q1*q2/r^2", "C) F = mg", "D) E = F/q"], index=None)
            q10 = st.radio("10. Шыны таяқшаны жібекке үйкегенде таяқша қандай заряд алады?", ["A) Теріс (-)", "B) Оң (+)", "C) Бейтарап (0)", "D) Басында оң"], index=None)

            st.subheader("📍 В БӨЛІМІ: Қысқа жауаптар (6 ұпай)")
            q11 = st.text_area("11. Неліктен металл қасық ағаш қасыққа қарағанда суық болып көрінеді?", height=70)
            q12 = st.text_area("12. Егер екі зарядтың арақашықтығын 3 есе арттырсақ, Кулон күші қалай өзгереді?", height=70)

            st.subheader("📍 С БӨЛІМІ: Есеп шығару (4 ұпай)")
            q13 = st.text_area("13. Есеп: r = 10 см, q1 = 2*10^-7 Кл, q2 = 5*10^-7 Кл. Өзара әрекеттесу күшін (F) табыңыз:", height=100)

            submit_btn = st.form_submit_button("ЖҰМЫСТЫ АЯҚТАУ ✅")

            if submit_btn:
                all_answers = {
                    "section_a": [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10],
                    "section_b": [q11, q12],
                    "section_c": [q13]
                }
                payload = {
                    "student_name": name, "student_class": s_class,
                    "answers": json.dumps(all_answers), "status": "pending"
                }
                resp = send_data(payload)
                if resp.status_code in [200, 201]:
                    st.session_state.submitted = True
                    st.rerun()

# --- 4. НӘТИЖЕНІ ІЗДЕУ ---
st.markdown("---")
st.subheader("🔎 Нәтижені тексеру")
search_query = st.text_input("Аты-жөніңізді жазыңыз:", key="search_input")

if search_query:
    s_headers = {"apikey": KEY, "Authorization": f"Bearer {KEY}"}
    res = requests.get(f"{URL}/rest/v1/{TABLE_NAME}?student_name=eq.{search_query}&select=*&order=id.desc", headers=s_headers)
    
    if res.status_code == 200:
        results = res.json()
        if len(results) > 0:
            data = results[0]
            if data['status'] == 'cheated':
                st.error("🚫 Бұл жұмыс жойылған (анти-чит)!")
            elif data['status'] == 'pending':
                st.warning("⏳ Тексерілуде...")
            else:
                st.success(f"✅ Ұпайыңыз: {data.get('score', 0)} / 20")
                st.info(f"💬 Пікір: \n\n {data.get('ai_feedback', '')}")
        else:
            st.info("ℹ️ Табылған жоқ.")
    else:
        st.error(f"⚠️ Базамен байланыс үзілді. Код: {res.status_code}")