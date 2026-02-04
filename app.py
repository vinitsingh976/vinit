import streamlit as st

st.set_page_config(page_title="Be My Valentine 💘", layout="centered")

st.markdown("<h1 style='text-align:center;'>💖 Be My Valentine 💖</h1>", unsafe_allow_html=True)

if "unlocked" not in st.session_state:
    st.session_state.unlocked = False

if not st.session_state.unlocked:
    st.subheader("🔒 Envelope Locked")
    secret = st.text_input("Type the magic word 💌", type="password")

    if st.button("Unlock Envelope"):
        if secret.lower() == "love":
            st.session_state.unlocked = True
            st.success("💌 Envelope unlocked!")
            st.rerun()
        else:
            st.error("❌ Wrong word 😏")
else:
    st.subheader("💌 Will you be my Valentine? 💖")

    image = st.file_uploader("Upload her picture", type=["jpg","png","jpeg"])
    if image:
        st.image(image, width=250)

    col1, col2 = st.columns([4,1])
    with col1:
        if st.button("❤️ YES ❤️"):
            st.balloons()
            st.success("🥰 Valentine secured 💕")
    with col2:
        if st.button("no"):
            st.warning("😌 Decorative option only")
