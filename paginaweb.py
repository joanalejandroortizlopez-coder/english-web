import streamlit as st

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="English Learning Hub", layout="wide")

# --- ESTILOS PERSONALIZADOS (CSS) ---
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #007bff; color: white; }
    .spanish-text { color: #555e6d; font-style: italic; border-left: 3px solid #007bff; padding-left: 10px; margin-bottom: 20px; }
    .english-text { font-weight: bold; font-size: 1.1em; }
    </style>
    """, unsafe_allow_html=True)

# --- NAVEGACIÓN LATERAL ---
st.sidebar.title("📚 Navigation / Navegación")
topic = st.sidebar.selectbox(
    "Select a topic / Selecciona un tema:",
    ["Home", "1. Articles (A/An)", "2. Subject Pronouns", "3. Verb To Be", 
     "4. Contractions", "5. Adjectives", "6. Word Order", "7. Countable/Uncountable",
     "8. Quantifiers", "9. Numbers", "10. Telling Time", 
     "11. Comparatives/Superlatives", "12. Simple Past", "13. Cooking Verbs", "14. Demonstratives"]
)

# --- FUNCIÓN PARA MOSTRAR CONTENIDO ---
# Aquí es donde insertaremos la lógica de cada número que me pidas.

if topic == "Home":
    st.title("Welcome to your English Learning Space! 🚀")
    st.write("Select a topic from the sidebar to start learning.")
    st.info("Selecciona un tema en la barra lateral para comenzar a aprender.")

# --- ESPACIO PARA TEMAS ---
# Cuando me digas un número, te daré el bloque de código que va aquí.
# --- TEMA 1: ARTICLES (A / AN) ---
if topic == "1. Articles (A/An)":
    st.title("📝 Topic 1: Articles (A / An)")
    st.info("Tema 1: Artículos (A / An)")

    # Sección de Definición
    st.subheader("1. Definition & Usage / Definición y Uso")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **English**: We use **'A'** or **'An'** for singular, non-specific nouns. 
         Use **'A'** before words starting with a consonant sound.
         Use **'An'** before words starting with a vowel sound.
        """)
    with col2:
        st.markdown("""
        <div class="spanish-text">
        Español: Usamos 'A' o 'An' para sustantivos singulares no específicos.
        * Usa 'A' antes de palabras que comienzan con sonido de consonante.
        * Usa 'An' antes de palabras que comienzan con sonido de vocal.
        </div>
        """, unsafe_allow_html=True)

    # Sección de Imagen y Ejemplos
    st.subheader("2. Visual Examples / Ejemplos Visuales")
    
    # URL de imagen representativa (Puedes cambiar este link por cualquier imagen .jpg o .png)
    image_url = image_url = "https://github.com/joanalejandroortizlopez-coder/english-web/blob/main/a-an.jpg?raw=true"
    video_url = video_url = "https://youtu.be/ZA8iL8H_JGk?si=ijcZlDJvqklKdsQE"
    st.image(image_url, caption="A vs An rules", width=400)
    st.video(video_url)

    st.table({
        "Rule / Regla": ["Consonant Sound", "Vowel Sound", "The 'H' Exception", "The 'U' Exception"],
        "Example / Ejemplo": ["A car / A university", "An apple / An hour", "An hour (Silent H)", "A university (Y-sound)"],
        "Translation / Traducción": ["Un carro / Una universidad", "Una manzana / Una hora", "Una hora (H muda)", "Una universidad (Sonido 'Yu')"]
    })

    # Sección de Práctica
    st.subheader("3. Practice Activity / Actividad de Práctica")
    st.write("Complete the sentences using **a** or **an**:")
    st.caption("Completa las oraciones usando **a** o **an**:")

    # Actividad interactiva
    ans1 = st.text_input("1. I have ____ umbrella in my bag.", key="q1")
    ans2 = st.text_input("2. She is ____ doctor at the local hospital.", key="q2")
    ans3 = st.text_input("3. It takes ____ hour to get there.", key="q3")

    if st.button("Check Answers / Revisar Respuestas"):
        # Lógica de corrección
        score = 0
        if ans1.lower().strip() == "a": score += 1
        if ans2.lower().strip() == "a": score += 1
        if ans3.lower().strip() == "an": score += 1
        
        st.success(f"Your score: {score}/3")
        if score == 3:
            st.balloons()
        else:
            st.warning("Try again! / ¡Inténtalo de nuevo!")
# --- TEMA 2: SUBJECT PRONOUNS ---
if topic == "2. Subject Pronouns":
    st.title("👤 Topic 2: Subject Pronouns")
    st.info("Tema 2: Pronombres Sujetos")

    # Sección de Definición
    st.subheader("1. Definition & Usage / Definición y Uso")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **English:** Subject pronouns replace the name of a person or object that performs the action in a sentence.
        * **I, You, He, She, It, We, They.**
        * 'It' is used for animals, objects, or abstract ideas.
        """)
    with col2:
        st.markdown("""
        <div class="spanish-text">
        Español: Los pronombres sujetos reemplazan el nombre de la persona u objeto que realiza la acción.
         Yo, Tú/Usted, Él, Ella, Ello (Cosas/Animales), Nosotros, Ellos.
         'It' se usa para animales, objetos o ideas abstractas.
        </div>
        """, unsafe_allow_html=True)

    # Sección de Imagen y Ejemplos
    st.subheader("2. Chart and Examples / Tabla y Ejemplos")
    
    # URL de imagen representativa sobre Pronombres
    image_url_2 = "https://github.com/joanalejandroortizlopez-coder/english-web/blob/main/english-pronouns.jpg?raw=true"
    video_url = "https://youtu.be/EqHWrAYUJ3w?si=EeMqTjpEJ1SNzUS7"
    st.image(image_url_2, caption="Subject Pronouns Overview", width=400)
    st.video(video_url)

    st.table({
        "Pronoun / Pronombre": ["I", "You", "He / She", "It", "We", "They"],
        "Usage / Uso": ["Myself", "The person I'm talking to", "Male / Female person", "Object or Animal", "Myself + others", "Other people/objects"],
        "Example / Ejemplo": ["I am happy", "You are tall", "He is a chef", "It is a blue pen", "We are friends", "They are students"]
    })

    # Sección de Práctica
    st.subheader("3. Practice Activity / Actividad de Práctica")
    st.write("Replace the underlined word with the correct **Subject Pronoun**:")
    st.caption("Reemplaza la palabra subrayada con el **Pronombre Sujeto** correcto:")

    # Actividad interactiva
    ans_p1 = st.text_input("1. **Maria** is a teacher. (____ is a teacher)", key="p1")
    ans_p2 = st.text_input("2. **The dog** is big. (____ is big)", key="p2")
    ans_p3 = st.text_input("3. **John and I** are brothers. (____ are brothers)", key="p3")

    if st.button("Check Answers / Revisar Respuestas"):
        score = 0
        if ans_p1.lower().strip() == "she": score += 1
        if ans_p2.lower().strip() == "it": score += 1
        if ans_p3.lower().strip() == "we": score += 1
        
        st.success(f"Your score: {score}/3")
        if score == 3:
            st.balloons()
        else:
            st.warning("Keep trying! / ¡Sigue intentándolo!")
            # --- TEMA 3: VERB TO BE ---
if topic == "3. Verb To Be":
    st.title("🐝 Topic 3: Verb To Be (Am, Is, Are)")
    st.info("The foundation of English sentences. / La base de las oraciones en inglés.")

    # 1. Definición y Usos
    st.subheader("1. Definition & Uses / Definición y Usos")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **English:** We use the verb 'To Be' to describe:
        * **Identity:** I am Carlos.
        * **Feelings:** She is happy.
        * **Location:** They are at school.
        * **Profession:** You are a student.
        """)
    with col2:
        st.markdown("""
        <div class="spanish-text">
        Español: Usamos el verbo 'To Be' para describir:
        Identidad: Yo soy Carlos.
        Sentimientos: Ella está feliz.
        Ubicación: Ellos están en la escuela.
        Profesión: Tú eres un estudiante.
        </div>
        """, unsafe_allow_html=True)

    # 2. Imagen y Excepciones
    st.subheader("2. Visual Guide & Exceptions / Guía Visual y Excepciones")
    
    # URL de imagen educativa
    image_url_3 = "https://github.com/joanalejandroortizlopez-coder/english-web/blob/main/Explicaci%C3%B3n-del-verbo-to-be.jpg?raw=true"
    video_url = "https://youtu.be/nxk6IXlBqmU?si=4FWDab03SWK62U1O"
    st.image(image_url_3, caption="Verb To Be Conjugation Chart", width=400)
    st.video(video_url)

    with st.expander("⚠️ Important Exception / Excepción Importante"):
        st.write("**Age (Edad):** In English, we don't 'have' years, we 'ARE' years.")
        st.error("❌ Incorrect: I have 20 years. | ✅ Correct: I am 20 years old.")
        st.caption("En inglés no 'tenemos' años, 'somos' años viejos.")

    # 3. Actividad de 3 puntos
    st.subheader("3. Practice Activity / Actividad de Práctica")
    st.write("Select or write the correct form of the verb **To Be**:")
    
    # Punto 1: Opción múltiple
    p1 = st.selectbox("1. My parents ________ doctors.", ["-", "am", "is", "are"], key="be_p1")
    
    # Punto 2: Negativo
    p2 = st.text_input("2. It (not / be) ________ cold today.", placeholder="Example: is not", key="be_p2")
    
    # Punto 3: Pregunta
    p3 = st.text_input("3. ________ you ready for the exam?", placeholder="Am / Is / Are", key="be_p3")

    if st.button("Submit Answers / Enviar Respuestas"):
        score = 0
        if p1 == "are": score += 1
        if p2.lower().strip() in ["is not", "isn't"]: score += 1
        if p3.lower().strip() == "are": score += 1
        
        if score == 3:
            st.success("Perfect! 🌟 3/3")
            st.balloons()
        else:
            st.warning(f"You got {score}/3. Check your spelling and try again!")
            # --- TEMA 4: CONTRACTIONS ---
if topic == "4. Contractions":
    st.title("🔗 Topic 4: Contractions")
    st.info("Making English sound natural. / Haciendo que el inglés suene natural.")

    # 1. Definition
    st.subheader("1. Definition & Usage / Definición y Uso")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **English:** A contraction is a shortened form of two words. We use an **apostrophe (')** to replace the missing letters.
        * **Formal:** I am not hungry.
        * **Informal/Natural:** I'm not hungry.
        """)
    with col2:
        st.markdown("""
        <div class="spanish-text">
        Español: Una contracción es una forma corta de dos palabras. Usamos un apóstrofe (') para reemplazar las letras que faltan.
        Formal: I am not hungry.
        Informal: I'm not hungry.
        </div>
        """, unsafe_allow_html=True)

    # 2. Examples & Image
    st.subheader("2. Common Examples / Ejemplos Comunes")
    
    # Imagen sugerida (Link directo)
    image_url_4 = "https://github.com/joanalejandroortizlopez-coder/english-web/blob/main/contractions.jpg?raw=true"
    video_url = "https://youtu.be/vnB4Eu7X1Qg?si=Fpg8Nb_yEwriftYs"
    st.image(image_url_4, caption="Guide to English Contractions", width=400)
    st.video(video_url)

    # Tabla comparativa
    st.table({
        "Full Form": ["I am", "You are", "She is", "We are", "They are", "Do not", "Does not", "Is not"],
        "Contraction": ["I'm", "You're", "She's", "We're", "They're", "Don't", "Doesn't", "Isn't"],
        "Spanish Meaning": ["Yo soy/estoy", "Tú eres/estás", "Ella es/está", "Nosotros somos", "Ellos son", "No (verbo)", "No (ella/él)", "No es/está"]
    })

    # 3. Activity (3 Points)
    st.subheader("3. Practice Activity / Actividad de Práctica")
    st.write("Convert the words in brackets into a **contraction**:")
    
    # Punto 1
    act1 = st.text_input("1. (It is) ________ a beautiful day!", placeholder="Type here...", key="con_1")
    
    # Punto 2
    act2 = st.text_input("2. They (are not) ________ coming to the party.", placeholder="Type here...", key="con_2")
    
    # Punto 3
    act3 = st.text_input("3. (I am) ________ learning Python and English.", placeholder="Type here...", key="con_3")

    if st.button("Check My Progress / Revisar"):
        score = 0
        # Validamos permitiendo minúsculas para que sea más fácil para el usuario
        if act1.lower().strip() == "it's": score += 1
        if act2.lower().strip() == "aren't": score += 1
        if act3.lower().strip() == "i'm": score += 1
        
        if score == 3:
            st.success("Excellent! You've mastered contractions. 🏆")
            st.balloons()
        else:
            st.warning(f"You got {score}/3. Remember to use the apostrophe (') correctly!")
            # --- TEMA 5: ADJECTIVES (DEFINITIVE VERSION) ---
if topic == "5. Adjectives":
    st.title("🎨 Topic 5: Adjectives & The Order Rule")
    st.info("Describing things correctly. / Describiendo las cosas correctamente.")

    # 1. Basic Rules (The Introduction)
    st.subheader("1. Basic Rules / Reglas Básicas")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **English:** * **Position:** Adjectives go **BEFORE** the noun. 
        * **No Plural:** Adjectives never end in 's'.
        * *Example:* Two **big** houses (Not: bigs houses).
        """)
    with col2:
        st.markdown("""
        <div class="spanish-text">
        Español:
        Posición:** Los adjetivos van ANTES del sustantivo.
        Sin Plural:** Los adjetivos nunca terminan en 's'.
        Ejemplo: Dos casas grandes (En inglés: Two big houses).
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    # 2. Advanced Rule: OSASCOMP (The 8 Points)
    st.subheader("2. The Order of Adjectives / El Orden de los Adjetivos")
    st.write("When using multiple adjectives, follow the **OSASCOMP** order:")
    
    # Tabla de los 8 puntos para diseño limpio
    st.table({
        "Order": ["1", "2", "3", "4", "5", "6", "7", "8"],
        "Category": ["Opinion", "Size", "Age", "Shape", "Color", "Origin", "Material", "Purpose"],
        "English Example": ["Beautiful", "Big", "Old", "Round", "Blue", "Italian", "Cotton", "Sleeping"],
        "Español": ["Opinión", "Tamaño", "Edad", "Forma", "Color", "Origen", "Material", "Propósito"]
    })

    # Imagen de referencia
    img_adj = "https://github.com/joanalejandroortizlopez-coder/english-web/blob/main/adjetives.png?raw=true"
    video_url = "https://youtu.be/4f3H12YNlxo?si=h35XVtNONCCQQtH7"
    st.image(img_adj, caption="Adjective Hierarchy Chart", width=400)
    st.video(video_url)

    # 3. Practice Activity (3 Points)
    st.subheader("3. Practice Activity / Actividad de Práctica")
    
    # Punto 1: Gramática básica (Plural)
    q1 = st.radio("1. Choose the correct sentence:", 
                 ["The flowers are red.", "The flowers are reds."], key="adj_q1")
    
    # Punto 2: Orden (Opinion + Color)
    q2 = st.text_input("2. Organize: (yellow / ugly) car", placeholder="An...", key="adj_q2")
    
    # Punto 3: Orden (Size + Origin + Material)
    q3 = st.text_input("3. Organize: (Chinese / large / plastic) toy", placeholder="A...", key="adj_q3")

    if st.button("Check Answers / Verificar"):
        score = 0
        if q1 == "The flowers are red.": score += 1
        if "ugly yellow car" in q2.lower(): score += 1
        if "large chinese plastic toy" in q3.lower(): score += 1
        
        if score == 3:
            st.success("Perfect! You understand the basics and the order. 🌟")
            st.balloons()
        else:
            st.warning(f"Score: {score}/3. Remember the order: Opinion -> Size -> Color -> Origin -> Material.")
            # --- TEMA 6: WORD ORDER (SVO) ---
if topic == "6. Word Order":
    st.title("🧩 Topic 6: Word Order")
    st.info("The skeleton of every English sentence. / El esqueleto de cada oración en inglés.")

    # 1. Definition & The SVO Rule
    st.subheader("1. The Basic Structure / La Estructura Básica")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **English:** Most English sentences follow a strict order:
        1. **Subject:** Who or what does the action.
        2. **Verb:** The action or state.
        3. **Object:** Who or what receives the action.
        
        *Example:* **I** (S) **love** (V) **pizza** (O).
        """)
    with col2:
        st.markdown("""
        <div class="spanish-text">
        Español: La mayoría de las oraciones siguen un orden estricto:
        1. Sujeto: Quién hace la acción.
        2. Verbo: La acción.
        3. Objeto: Quién recibe la acción.
        
        Ejemplo:* Yo (S) amo (V) la pizza (O).
        </div>
        """, unsafe_allow_html=True)

    # 2. Place and Time (The Extension)
    st.subheader("2. Adding Place and Time / Añadiendo Lugar y Tiempo")
    st.warning("Rule: Place comes BEFORE Time. / Regla: El Lugar va ANTES que el Tiempo.")
    
    # Imagen educativa sobre el orden SVO
    image_url_6 = "https://github.com/joanalejandroortizlopez-coder/english-web/blob/main/wordorder.jpg?raw=true"
    video_url = "https://youtu.be/LWigoLHN9WU?si=cPwkb5sofp4VOR2m"
    st.image(image_url_6, caption="Subject + Verb + Object + Place + Time", width=400)
    st.video(video_url)

    st.table({
        "Part": ["Subject", "Verb", "Object", "Place", "Time"],
        "Example 1": ["He", "reads", "a book", "in the library", "every day"],
        "Example 2": ["They", "play", "soccer", "at the park", "on Sundays"],
        "Spanish": ["Sujeto", "Verbo", "Objeto", "Lugar", "Tiempo"]
    })

    # 3. Practice Activity (3 Points)
    st.subheader("3. Practice Activity / Actividad de Práctica")
    st.write("Unscramble the words to make correct sentences:")
    st.caption("Ordena las palabras para formar oraciones correctas:")

    # Punto 1: SVO Básico
    st.markdown("**1. (apples / likes / she)**")
    order1 = st.text_input("Answer 1:", placeholder="Type here...", key="wo_1")
    
    # Punto 2: SVO + Place
    st.markdown("**2. (we / English / study / at school)**")
    order2 = st.text_input("Answer 2:", placeholder="Type here...", key="wo_2")
    
    # Punto 3: Place + Time (La regla difícil)
    st.markdown("**3. (at 8:00 / goes / he / to bed)**")
    order3 = st.text_input("Answer 3:", placeholder="Type here...", key="wo_3")

    if st.button("Check Order / Revisar Orden"):
        score = 0
        if order1.lower().strip() == "she likes apples": score += 1
        if order2.lower().strip() == "we study english at school": score += 1
        # Aceptamos la variante con punto o sin punto
        if order3.lower().strip().replace(".", "") == "he goes to bed at 8:00": score += 1
        
        if score == 3:
            st.success("Perfect! You have a great sense of structure. 🏁")
            st.balloons()
        else:
            st.error(f"Score: {score}/3. Remember: Subject + Verb + Object + Place + Time.")
            # --- TEMA 7: COUNTABLE AND UNCOUNTABLE (EXTENDED VERSION) ---
if topic == "7. Countable/Uncountable":
    st.title("🍎 Topic 7: Countable and Uncountable Nouns")
    st.info("Deep dive into noun types. / Profundización en los tipos de sustantivos.")

    # 1. Definition & Rules
    st.subheader("1. Definition & Usage / Definición y Uso")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **English:** * **Countable:** Things we can count (1, 2, 3...). They have a plural form.
        * **Uncountable:** Mass nouns, liquids, and abstract concepts. They **never** have a plural form and don't use 'a/an'.
        """)
    with col2:
        st.markdown("""
        <div class="spanish-text">
        Español: Contables: Cosas que podemos contar. Tienen forma plural.
        Incontables: Sustantivos en masa, líquidos y conceptos abstractos. Nunca tienen plural y no usan 'a/an'.
        </div>
        """, unsafe_allow_html=True)

    # 2. Image (Maintaining the same style)
    st.subheader("2. Visual Guide / Guía Visual")
    # Usando el link de Wikimedia que es más estable
    image_url_7 = "https://github.com/joanalejandroortizlopez-coder/english-web/blob/main/Countable-and-Uncountable-Nouns.webp?raw=true"
    video_url = "https://youtu.be/nKIOHbieDrQ?si=6nEUWslzB5lqX62m"
    st.image(image_url_7, caption="Countable vs Uncountable Examples", width=400)
    st.video(video_url)

    # TABLA EXTENDIDA DE TIPOS (Aquí están todos los que mencionaste)
    st.subheader("3. All Categories / Todas las Categorías")
    st.table({
        "Category / Categoría": ["Liquids", "Grains/Powder", "Mass/Food", "Materials", "Abstract", "Subjects", "Group Concepts"],
        "Examples / Ejemplos": ["Water, Juice, Oil", "Rice, Sugar, Salt", "Bread, Meat, Cheese", "Wood, Gold, Paper", "Love, Time, Luck", "Math, Science", "Money, Furniture, News"],
        "Type": ["Uncountable", "Uncountable", "Uncountable", "Uncountable", "Uncountable", "Uncountable", "Uncountable"]
    })

    # 3. Practice Activity (3 Points)
    st.subheader("4. Practice Activity / Actividad de Práctica")
    st.write("Complete the tasks based on the categories above:")
    
    # Punto 1: Identificación
    p7_1 = st.selectbox("1. Which of these is COUNTABLE?", ["-", "Air", "Bottle", "Salt"], key="ext_1")
    
    # Punto 2: Error común
    p7_2 = st.radio("2. Is 'Money' countable in English?", ["Yes", "No"], key="ext_2")
    
    # Punto 3: Aplicación
    p7_3 = st.text_input("3. Write the plural of 'Water' (If it doesn't exist, write 'None'):", key="ext_3")

    if st.button("Check Answers / Revisar"):
        score = 0
        if p7_1 == "Bottle": score += 1
        if p7_2 == "No": score += 1
        if p7_3.lower().strip() == "none": score += 1
        
        st.success(f"Score: {score}/3")
        if score == 3:
            st.balloons()
            # --- TEMA 8: QUANTIFIERS (MUCH, MANY, SOME, ANY) ---
if topic == "8. Quantifiers":
    st.title("🔢 Topic 8: Quantifiers")
    st.info("How to talk about quantities. / Cómo hablar de cantidades.")

    # 1. Rules and Definitions
    st.subheader("1. General Rules / Reglas Generales")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **English:**
        * **Many:** Used with Countable nouns (plural).
        * **Much:** Used with Uncountable nouns (singular).
        * **Some:** Used in Affirmative sentences (+).
        * **Any:** Used in Negative (-) and Questions (?).
        """)
    with col2:
        st.markdown("""
        <div class="spanish-text">
        Español:
        Many: Se usa con contables (plural).
        Much: Se usa con incontables (singular).
        Some: Se usa en oraciones afirmativas (+).
        Any: Se usa en negativas (-) e interrogativas (?).
        </div>
        """, unsafe_allow_html=True)

    # 2. Examples & Visual
    st.subheader("2. Examples in Context / Ejemplos en Contexto")
    
    # Imagen de referencia para cuantificadores
    image_url_8 = "https://github.com/joanalejandroortizlopez-coder/english-web/blob/main/quantifiers-en-ingles-1024x1024.png?raw=true"
    video_url = "https://youtu.be/-oll5WNHWAk?si=dFtJlYz8JKGTPHWL"
    st.image(image_url_8, caption="Quantifiers Guide", width=400)
    st.video(video_url)
    
    st.table({
        "Quantifier": ["Many", "Much", "Some", "Any"],
        "Example / Ejemplo": ["Many books", "Much water", "Some apples", "Any sugar"],
        "Sentence Type": ["Countable", "Uncountable", "Affirmative (+)", "Negative (-) / ?"]
    })

    # 3. Exception (Offers/Requests)
    st.subheader("3. Important Exception / Excepción Importante")
    st.warning("Use **SOME** in questions when offering or asking for something.")
    st.write("Example: *Would you like **some** tea?* / *Can I have **some** help?*")

    # 4. Activity
    st.subheader("4. Practice Activity / Actividad de Práctica")
    q1 = st.selectbox("1. I don't have ____ money.", ["-", "many", "much"], key="q8_1")
    q2 = st.selectbox("2. There are ____ trees in the park.", ["-", "many", "much"], key="q8_2")
    q3 = st.text_input("3. Do you have ____ (some/any) siblings?", key="q8_3")

    if st.button("Check Answers / Verificar"):
        score = 0
        if q1 == "much": score += 1
        if q2 == "many": score += 1
        if q3.lower().strip() == "any": score += 1
        
        st.success(f"Score: {score}/3")
        if score == 3:
            st.balloons()
            # --- TEMA 9: CARDINAL AND ORDINAL NUMBERS (DETALLADO) ---
if topic == "9. Numbers":
    st.title("🔢 Topic 9: Cardinal and Ordinal Numbers")
    st.info("How to count and how to rank. / Cómo contar y cómo clasificar.")

    # 1. Definición Detallada
    st.subheader("1. The Difference / La Diferencia")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **Cardinal Numbers (Quantity):**
        Used to say *how many* of something there are.
        * *Examples:* 1 (one), 2 (two), 10 (ten), 50 (fifty).
        * *Use:* "I have **two** brothers."
        """)
    with col2:
        st.markdown("""
        <div class="spanish-text">
        Ordinal Numbers (Position):
        Used to tell the *order* or *date*.
        Examples: 1st (first), 2nd (second), 3rd (third).
        Use: "I am the second son."
        </div>
        """, unsafe_allow_html=True)

    # 2. Reglas de las Terminaciones (Importante)
    st.subheader("2. The 'Last Two Letters' Rule / La Regla de las últimas dos letras")
    st.write("En los números ordinales, la abreviatura (1st, 2nd) viene de las últimas dos letras de la palabra escrita:")
    
    st.markdown("""
    * **ST** (firs**t**): Usado con el número 1 (1st, 21st, 31st...).
    * **ND** (seco**nd**): Usado con el número 2 (2nd, 22nd, 32nd...).
    * **RD** (thi**rd**): Usado con el número 3 (3rd, 23rd, 33rd...).
    * **TH** (four**th**): Usado para TODOS los demás (4th, 5th, 10th, 100th...).
    """)
    
    st.warning("⚠️ **Watch out!** 11, 12, and 13 always use **TH** (11th, 12th, 13th).")

    # 3. Imagen Educativa
    st.subheader("3. Visual Reference Chart / Tabla Visual")
    # 
    image_url_9 = "https://github.com/joanalejandroortizlopez-coder/english-web/blob/main/numeros-ordinales-y-cardinales_1718363204.webp?raw=true"
    video_url = "https://youtu.be/cvnseqvcwcE?si=QKuhbMK5cO2NRZhp"
    st.image(image_url_9, caption="Cardinal vs Ordinal Chart", width=400)
    st.video(video_url)

    # 4. Tabla de ejemplos complejos
    st.subheader("4. More Examples / Más Ejemplos")
    st.table({
        "Cardinal": ["5 (Five)", "9 (Nine)", "12 (Twelve)", "20 (Twenty)", "21 (Twenty-one)"],
        "Ordinal": ["5th (Fifth)", "9th (Ninth)", "12th (Twelfth)", "20th (Twentieth)", "21st (Twenty-first)"],
        "Nota": ["V cambia a F", "Pierde la E", "V cambia a F", "Y cambia a IE", "Solo cambia el último número"]
    })

    # 5. Actividad (3 Puntos)
    st.subheader("5. Practice Activity / Actividad de Práctica")
    
    # Punto 1: Ortografía difícil
    p9_1 = st.text_input("1. Write the ordinal for 12 (12th):", placeholder="Twel...", key="n_1")
    
    # Punto 2: Uso en fechas
    p9_2 = st.selectbox("2. My birthday is on the ________ of October.", ["-", "four", "fourth", "4"], key="n_2")
    
    # Punto 3: Lógica de terminación
    p9_3 = st.text_input("3. What are the last two letters for the number 23?", placeholder="st, nd, rd or th?", key="n_3")

    if st.button("Verify / Verificar"):
        score = 0
        if p9_1.lower().strip() == "twelfth": score += 1
        if p9_2 == "fourth": score += 1
        if p9_3.lower().strip() == "rd": score += 1
        
        st.success(f"Score: {score}/3")
        if score == 3:
            st.balloons()
        else:
            st.info("Check the 'Spelling' in the table above! / ¡Revisa la ortografía en la tabla!")
            # --- TEMA 10: TELLING THE TIME ---
if topic == "10. Telling Time":
    st.title("⌚ Topic 10: Telling the Time")
    st.info("What time is it? / ¿Qué hora es?")

    # 1. Basic Structure
    st.subheader("1. The Two Ways / Las Dos Formas")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **English:** There are two ways to say the time:
        1. **Digital:** Hour + Minutes (Ten twenty).
        2. **Analog (Classical):** Minutes + PAST/TO + Hour.
        
        * **O'clock:** Exactly on the hour.
        * **Half past:** 30 minutes.
        * **Quarter past/to:** 15 minutes.
        """)
    with col2:
        st.markdown("""
        <div class="spanish-text">
        Español: Hay dos formas de decir la hora:
        1. Digital: Hora + Minutos (Ten twenty).
        2. Analógica: Minutos + PAST/TO + Hora.
        
        O'clock: En punto.
        Half past: Y media.
        Quarter past/to: Y cuarto / Cuarto para.
        </div>
        """, unsafe_allow_html=True)

    # 2. The Clock Diagram
    st.subheader("2. The Clock Rule / La Regla del Reloj")
    st.write("Divide the clock in two halves: **PAST** (minutes 1-30) and **TO** (minutes 31-59).")
    
    # 
    img_time = "https://github.com/joanalejandroortizlopez-coder/english-web/blob/main/clock.webp?raw=true"
    video_url = "https://youtu.be/3YJxNWyc-Tw?si=xAifU-2ARcYpXZSx"
    st.image(img_time, caption="Minutes + Past/To + Hour", width=400)
    st.video(video_url)

    # 3. Examples Table
    st.subheader("3. Examples / Ejemplos")
    st.table({
        "Time": ["8:00", "8:15", "8:30", "8:45", "9:10"],
        "Formal (Analog)": ["Eight o'clock", "Quarter past eight", "Half past eight", "Quarter to nine", "Ten past nine"],
        "Informal (Digital)": ["Eight", "Eight fifteen", "Eight thirty", "Eight forty-five", "Nine ten"],
        "Español": ["8 en punto", "8 y cuarto", "8 y media", "9 menos cuarto", "9 y diez"]
    })

    # 4. Practice Activity (3 Points)
    st.subheader("4. Practice Activity / Actividad de Práctica")
    
    # Punto 1: Digital
    p10_1 = st.text_input("1. Write 10:20 in digital form (Hour + Minutes):", placeholder="Example: Ten twenty", key="t_1")
    
    # Punto 2: Analog (Past)
    p10_2 = st.selectbox("2. How do you say 5:15 formally?", ["-", "Quarter to five", "Quarter past five", "Five fifteen"], key="t_2")
    
    # Punto 3: Analog (To)
    p10_3 = st.text_input("3. How do you say 6:45 formally? (Quarter to...)", placeholder="Quarter to...", key="t_3")

    if st.button("Check Clock / Revisar"):
        score = 0
        if p10_1.lower().strip() == "ten twenty": score += 1
        if p10_2 == "Quarter past five": score += 1
        if "quarter to seven" in p10_3.lower().strip(): score += 1
        
        st.success(f"Score: {score}/3")
        if score == 3:
            st.balloons()
        else:
            st.warning("Remember: After 30 minutes, we use TO and look at the NEXT hour!")
            # --- TEMA 11: COMPARATIVES AND SUPERLATIVES (THE SYLLABLE RULE) ---
if topic == "11. Comparatives/Superlatives":
    st.title("🏆 Topic 11: Comparatives and Superlatives")
    st.info("Comparing two or more things. / Comparando dos o más cosas.")

    # 1. The Syllable Rule
    st.subheader("1. The Rule of Syllables / La Regla de las Sílabas")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **Short Adjectives (1 Syllable):**
        * **Comparative:** Add **-er** (Tall -> Taller).
        * **Superlative:** Add **-est** (Tall -> Tallest).
        
        **Long Adjectives (2+ Syllables):**
        * **Comparative:** Use **More** (More intelligent).
        * **Superlative:** Use **The Most** (The most intelligent).
        """)
    with col2:
        st.markdown("""
        <div class="spanish-text">
        Adjetivos Cortos (1 Sílaba):
        Comparativo: Agrega -er (Más alto).
        Superlativo: Agrega -est (El más alto que).
        
        Adjetivos Largos (2+ Sílabas):
        Comparativo: Usa More (Más inteligente).
        Superlativo: Usa The Most (El más inteligente).
        </div>
        """, unsafe_allow_html=True)

    # 2. Visual Guide
    st.subheader("2. Comparison Chart / Tabla de Comparación")
    
    # 
    img_comp = "https://github.com/joanalejandroortizlopez-coder/english-web/blob/main/comparativos-y-superlativos-en-ingles-1.webp?raw=true"
    video_url = "https://youtu.be/p0kwsNq3A2w?si=PJ9DMfVK8WwP4qPw"
    st.image(img_comp, caption="Adjective Transformations", width=400)
    st.video(video_url)

    st.table({
        "Adjective": ["Tall (1 syl)", "Big (1 syl)", "Happy (2 syl -y)", "Expensive (3 syl)"],
        "Comparative (2 things)": ["Taller than", "Bigger than", "Happier than", "More expensive than"],
        "Superlative (3+ things)": ["The Tallest", "The Biggest", "The Happiest", "The Most expensive"]
    })

    # 3. Irregular Adjectives
    st.subheader("3. Irregulars / Irregulares")
    st.error("These don't follow the rules: Good -> Better/Best | Bad -> Worse/Worst")

    # 4. Practice Activity (3 Points)
    st.subheader("4. Practice Activity / Actividad de Práctica")
    
    # Punto 1: Aplicación de sílaba corta (Tu ejemplo)
    p11_1 = st.text_input("1. Mount Everest is the ________ (Tall) mountain in the world.", placeholder="Tallest or Most Tall?", key="c_1")
    
    # Punto 2: Adjetivo largo
    p11_2 = st.selectbox("2. Ferrari is ________ than a Fiat.", ["-", "expensiver", "more expensive"], key="c_2")
    
    # Punto 3: Irregulares
    p11_3 = st.text_input("3. What is the comparative of GOOD?", placeholder="Gooder or Better?", key="c_3")

    if st.button("Check Ranking / Verificar"):
        score = 0
        if p11_1.lower().strip() == "tallest": score += 1
        if p11_2 == "more expensive": score += 1
        if p11_3.lower().strip() == "better": score += 1
        
        st.success(f"Score: {score}/3")
        if score == 3:
            st.balloons()
            # --- TEMA 12: SIMPLE PAST ---
if topic == "12. Simple Past":
    st.title("⏳ Topic 12: Simple Past Tense")
    st.info("Talking about finished actions. / Hablando de acciones terminadas.")

    # 1. Regular vs Irregular
    st.subheader("1. The Two Groups / Los Dos Grupos")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **Regular Verbs:**
        Just add **-ed** to the verb.
        * Play -> Play**ed**
        * Watch -> Watch**ed**
        
        **Irregular Verbs:**
        They change their form completely.
        * Go -> **Went**
        * Eat -> **Ate**
        * Buy -> **Bought**
        """)
    with col2:
        st.markdown("""
        <div class="spanish-text">
        Verbos Regulares:
        Solo añade -ed al final del verbo.
        * Play -> Play-ed
        * Watch -> Watch-ed
        
        **Verbos Irregulares:**
        Cambian su forma completamente (hay que memorizarlos).
        * Go -> **Went** (Fui)
        * Eat -> **Ate** (Comí)
        </div>
        """, unsafe_allow_html=True)

    # 2. Structure (Auxiliary DID)
    st.subheader("2. Sentence Structure / Estructura de la Oración")
    st.warning("⚠️ Rule: When you use **DID** or **DIDN'T**, the verb returns to its **present** form.")
    st.caption("Regla: Cuando usas el auxiliar DID o DIDN'T, el verbo vuelve a su forma presente.")

    st.table({
        "Type": ["Affirmative (+)", "Negative (-)", "Question (?)"],
        "Structure": ["Subject + Verb (Past)", "Subject + DIDN'T + Verb (Present)", "DID + Subject + Verb (Present)?"],
        "Example": ["I went to the park", "I didn't go to the park", "Did you go to the park?"]
    })

    # 3. Visual Reference
    st.subheader("3. Common Irregular Verbs / Verbos Irregulares Comunes")
    # 
    image_url_12 = "https://github.com/joanalejandroortizlopez-coder/english-web/blob/main/Simple%20Past%20Tense.jpg?raw=true"
    video_url = "https://youtu.be/DQlzxDz5T0w?si=gkb7IZgip6v1Dv4B"
    st.image(image_url_12, caption="Past Tense Guide", width=400)
    st.video(video_url)

    # 4. Practice Activity (3 Points)
    st.subheader("4. Practice Activity / Actividad de Práctica")
    
    # Punto 1: Regular
    p12_1 = st.text_input("1. Past of 'COOK' (Regular):", placeholder="Add the ending...", key="sp_1")
    
    # Punto 2: Irregular
    p12_2 = st.text_input("2. Past of 'SLEEP' (Irregular):", placeholder="It's not sleeped!", key="sp_2")
    
    # Punto 3: Estructura Negativa (El error más común)
    p12_3 = st.selectbox("3. Choose the correct negative sentence:", 
                        ["-", "I didn't ate pizza", "I didn't eat pizza"], key="sp_3")

    if st.button("Check Past / Verificar"):
        score = 0
        if p12_1.lower().strip() == "cooked": score += 1
        if p12_2.lower().strip() == "slept": score += 1
        if p12_3 == "I didn't eat pizza": score += 1
        
        st.success(f"Score: {score}/3")
        if score == 3:
            st.balloons()
            # --- TEMA 13: COOKING VERBS ---
if topic == "13. Cooking Verbs":
    st.title("🍳 Topic 13: Cooking Verbs")
    st.info("Master the kitchen vocabulary. / Domina el vocabulario de cocina.")

    # 1. Action Verbs
    st.subheader("1. Common Kitchen Actions / Acciones Comunes")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **English:**
        * **Chop:** Cut into small pieces.
        * **Boil:** Cook in very hot water.
        * **Bake:** Cook in the oven (bread/cakes).
        * **Whisk:** Mix quickly (eggs/cream).
        * **Peel:** Remove the skin of a fruit.
        """)
    with col2:
        st.markdown("""
        <div class="spanish-text">
        Español:
        Chop: Picar o trocear.
        Boil: Hervir.
        Bake: Hornear (pan o pasteles).
        Whisk: Batir (huevos o crema).
        Peel: Pelar (quitar la cáscara).
        </div>
        """, unsafe_allow_html=True)

    # 2. Visual Vocabulary
    st.subheader("2. Cooking Methods / Métodos de Cocina")
    
    # Imagen con ilustraciones de verbos de cocina
    image_url_13 = "https://github.com/joanalejandroortizlopez-coder/english-web/blob/main/Cooking-Verbs-1.png.webp?raw=true"
    video_url = "https://youtu.be/oqfh5i5Zfcs?si=o-18DBEHrEomQkRn"
    st.image(image_url_13, caption="Cooking Actions Guide", width=400)
    st.video(video_url)

    

    # 3. Reference Table
    st.table({
        "Verb": ["Fry", "Stir", "Pour", "Slice", "Grill", "Simmer"],
        "Definition": ["Cook in oil", "Mix with a spoon", "Transfer liquid", "Cut into thin pieces", "Cook on a fire", "Cook slowly"],
        "Spanish": ["Freír", "Revolver", "Verter / Echar", "Rebanar", "Asar a la parrilla", "Hervir a fuego lento"]
    })

    # 4. Practice Activity (3 Points)
    st.subheader("3. Practice Activity / Actividad de Práctica")
    st.write("Complete the kitchen instructions:")

    # Punto 1: Acción de horno
    p13_1 = st.selectbox("1. Put the pizza in the oven to ________ it.", ["-", "boil", "bake", "fry"], key="ck_1")
    
    # Punto 2: Líquidos
    p13_2 = st.text_input("2. ________ (Verter) the milk into the cup.", placeholder="Starts with P...", key="ck_2")
    
    # Punto 3: Mezclar
    p13_3 = st.selectbox("3. Use a spoon to ________ the soup.", ["-", "stir", "peel", "slice"], key="ck_3")

    if st.button("Finish Course / Finalizar"):
        score = 0
        if p13_1 == "bake": score += 1
        if p13_2.lower().strip() == "pour": score += 1
        if p13_3 == "stir": score += 1
        
        st.success(f"Score: {score}/3")
        if score == 3:
            st.balloons()

# --- TEMA 14: DEMONSTRATIVES ---
if topic == "14. Demonstratives":
    st.title("👈 Topic 14: Demonstratives")
    st.info("Learn how to point out specific objects. / Aprende a señalar objetos específicos.")

    # 1. Explanation with Columns
    st.subheader("1. Concept / Concepto")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **English:**
        * **This:** Singular and Near (here).
        * **That:** Singular and Far (there).
        * **These:** Plural and Near (here).
        * **Those:** Plural and Far (there).
        """)
    with col2:
        st.markdown("""
        <div class="spanish-text">
        Español:
        * This: Este / Esta (Cerca y Singular).
        * That: Ese / Aquel (Lejos y Singular).
        * These: Estos / Estas (Cerca y Plural).
        * Those: Esos / Aquellos (Lejos y Plural).
        </div>
        """, unsafe_allow_html=True)

    # 2. Visual Vocabulary (Image and Video)
    st.subheader("2. Visual Guide / Guía Visual")
    
    # Asegúrate de que el nombre de la imagen sea el correcto en tu GitHub
    image_url_14 = "https://github.com/joanalejandroortizlopez-coder/english-web/blob/main/demonstratives.jpg?raw=true"
    video_url_14 = "https://youtu.be/cnNB_ThNukc?si=oZlP_8kKY--Yjo4Q"
    
    st.image(image_url_14, caption="Demonstratives: Near vs Far", width=400)
    st.video(video_url_14)

    # 3. Reference Table
    st.subheader("3. Grammar Table / Tabla de Referencia")
    st.table({
        "Demonstrative": ["This", "That", "These", "Those"],
        "Number": ["Singular", "Singular", "Plural", "Plural"],
        "Distance": ["Near (Cerca)", "Far (Lejos)", "Near (Cerca)", "Far (Lejos)"],
        "Example": ["This is my car", "That is the moon", "These are my keys", "Those are mountains"]
    })

    # 4. Practice Activity (3 Points)
    st.subheader("4. Practice Activity / Actividad de Práctica")
    st.write("Choose the correct demonstrative pronoun:")

    # Punto 1: Singular Cerca
    p14_1 = st.selectbox("1. ________ (Cerca) is my favorite pencil.", ["-", "This", "That", "These"], key="dm_1")
    
    # Punto 2: Plural Lejos
    p14_2 = st.selectbox("2. Look at ________ (Lejos) stars in the sky.", ["-", "These", "Those", "This"], key="dm_2")
    
    # Punto 3: Plural Cerca
    p14_3 = st.text_input("3. ________ (Estas) are my new shoes.", placeholder="Starts with T...", key="dm_3")

    if st.button("Check Answers / Verificar"):
        score = 0
        if p14_1 == "This": score += 1
        if p14_2 == "Those": score += 1
        if p14_3.lower().strip() == "these": score += 1
        
        st.success(f"Score: {score}/3")
        if score == 3:
            st.balloons()
            st.write("✨ Excellent! You have mastered the Demonstratives.")
