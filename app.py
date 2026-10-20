
import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Ortak Not Panosu", page_icon="📝")

st.title("📝 Ortak Not Panosu")
st.write("Ekibinle notlarını paylaş.")

# Bu ilk sürümde notlar geçici olarak saklanır.
if "notlar" not in st.session_state:
    st.session_state.notlar = []

with st.form("not_formu", clear_on_submit=True):
    isim = st.text_input("Adınız")
    mesaj = st.text_area("Notunuz")
    gonder = st.form_submit_button("Notu gönder")

if gonder:
    if isim.strip() and mesaj.strip():
        st.session_state.notlar.append({
            "isim": isim.strip(),
            "mesaj": mesaj.strip(),
            "zaman": datetime.now().strftime("%d.%m.%Y %H:%M")
        })
        st.success("Not eklendi!")
    else:
        st.warning("Lütfen adınızı ve notunuzu girin.")

st.subheader("📌 Notlar")

if not st.session_state.notlar:
    st.info("Henüz not yok.")
else:
    for not_item in reversed(st.session_state.notlar):
        with st.container(border=True):
            st.markdown(f"**{not_item['isim']}**")
            st.write(not_item["mesaj"])
            st.caption(not_item["zaman"])
