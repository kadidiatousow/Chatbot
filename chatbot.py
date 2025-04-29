import streamlit as st
from groq import Groq


groq_client = Groq(api_key="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")


if "messages" not in st.session_state:
    st.session_state.messages = []


st.markdown("""
    <style>
        .main {
            background-color: #f5f6f8;
        }
        .chat-container {
            max-width: 800px;
            margin: auto;
            padding-bottom: 100px;
        }
        .message {
            padding: 18px 25px;
            margin: 15px 0;
            border-radius: 20px;
            max-width: 80%;
            word-wrap: break-word;
            color: #2d3436;
            box-shadow: 0 3px 10px rgba(0,0,0,0.05);
            position: relative;
            border: 1px solid #e0e0e0;
        }
        .user-message {
            background: #ffffff;
            margin-left: auto;
            border-left: 4px solid #6c5ce7;
        }
        .bot-message {
            background: #fff;
            margin-right: auto;
            border-left: 4px solid #00b894;
        }
        .message-header {
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 8px;
        }
        .stTextInput input {
            
            padding: 18px;
            border: 2px solid #dfe6e9 !important;
            background: #ffffff !important;
            font-size: 16px;
            color: #2d3436 !important;
        }
        .stTextInput input::placeholder {
            color: #95a5a6 !important;
        }
        .stButton button {
            border-radius: 50%;
            width: 60px;
            height: 60px;
            background: #6c5ce7 !important;
            border: none !important;
            transition: 0.3s;
            font-size: 20px;
            color: white !important;
        }
        .stButton button:hover {
            transform: rotate(90deg) scale(1.1);
            background: #5b4bc4 !important;
        }
        .bot-icon {
            width: 35px;
            height: 35px;
            background: #00b894;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: bold;
        }
        .user-icon {
            width: 35px;
            height: 35px;
            background: #6c5ce7;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
        }
        /* Zone de saisie */
        .st-emotion-cache-1q7spjk {
            background: #f5f6f8 !important;
            box-shadow: 0 -2px 15px rgba(0,0,0,0.08) !important;
            border-top: 1px solid #e0e0e0 !important;
        }
    </style>
""", unsafe_allow_html=True)


st.markdown("""
    <div style='text-align: center; margin-bottom: 40px;'>
        <h1 style='color: #2d3436; font-size: 2.5em; margin-bottom: 10px;'>🤖 Chatbot Intelligent</h1>
        <p style='color: #636e72;'>Discutez avec une IA </p>
    </div>
""", unsafe_allow_html=True)


chat_container = st.container()


with st.form(key="chat_form"):
    cols = st.columns([6, 1])
    with cols[0]:
        user_input = st.text_input(
            "Message",
            placeholder="Tapez votre message ici... ✍️",
            label_visibility="collapsed"
        )
    with cols[1]:
        submit_button = st.form_submit_button("➤")


if submit_button and user_input:
    
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    
    with st.spinner("🧠 Traitement en cours..."):
        bot_response = groq_client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[{"role": "user", "content": user_input}]
        ).choices[0].message.content
    
    
    st.session_state.messages.append({"role": "assistant", "content": bot_response})


with chat_container:
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f"""
                <div class="message user-message">
                    <div class="message-header">
                        <div class="user-icon">👤</div>
                        <div style="font-weight: 600; color: #6c5ce7;">Vous</div>
                    </div>
                    <div style="color: #2d3436;">{message["content"]}</div>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div class="message bot-message">
                    <div class="message-header">
                        <div class="bot-icon">AI</div>
                        <div style="font-weight: 600; color: #00b894;">Assistant</div>
                    </div>
                    <div style="color: #2d3436;">{message["content"]}</div>
                </div>
            """, unsafe_allow_html=True)