import streamlit as st
from content import CSS, BANNER, KPIS, nav, block, S, FOOTER

st.set_page_config(page_title="Sony Europe | Recruitment Specialist Plan | Adam Baig", page_icon="🎬", layout="wide")
st.markdown(f"""<style>
.stApp, [data-testid="stAppViewContainer"], [data-testid="stMain"] {{ background:#FFFFFF !important; }}
[data-testid="stHeader"] {{ background:rgba(255,255,255,0) !important; }}
[data-testid="stToolbar"] {{ visibility:hidden; }}
.block-container {{ max-width:1180px; padding-top:1.2rem; }}
html {{ scroll-behavior:smooth; }}
{CSS}
</style>""", unsafe_allow_html=True)

def show(html):
    st.markdown(f'<div class="cs">{html}</div>', unsafe_allow_html=True)

show(BANNER + KPIS + nav())
for i in range(len(S)):
    show(block(i))
show(FOOTER)
