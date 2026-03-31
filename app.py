import streamlit as st
from datetime import datetime

st.set_page_config(page_title="명리체질의학 25상 진단", layout="centered")
st.title("명리체질의학: 백경 白炅 의 25상 양생법")
st.subheader("창시자 김재성 박사 공식 자동 진단 시스템")

st.info("학술적 근거: 『黃帝內經(황제내경)』 「靈樞(영추)」 제64편 「陰陽二十五人(음양이십오인)」 및 원광대학교 박사학위 논문")
st.write("RISS학술연구정보서비스: https://naver.me/GT4MSUyP")

def analyze_25_sang(saju_list):
mapping = {
'갑': '木', '을': '木', '인': '木', '묘': '木',
'병': '火', '정': '火', '사': '火', '오': '火',
'무': '土', '기': '土', '진': '土', '술': '土', '축': '土', '미': '土',
'경': '金', '신': '金', '유': '金',
'임': '水', '계': '水', '해': '水', '자': '水'
}
scores = {'木': 0, '火': 0, '土': 0, '金': 0, '水': 0}
for i, pillar in enumerate(saju_list):
for char in pillar:
if char in mapping:
weight = 2.0 if i == 1 else 1.0
scores[mapping[char]] += weight
sorted_el = sorted(scores.items(), key=lambda x: x[1], reverse=True)
return f"{sorted_el[0][0]}형 {sorted_el[1][0]}상", scores

st.divider()
name = st.text_input("이름", value="임현경")
c1, c2 = st.columns(2)
with c1: gender = st.radio("성별", ["남자", "여자"], horizontal=True)
with c2: cal_type = st.radio("양/음력", ["양력", "음력"], horizontal=True)

st.write("출생정보 입력")
cy, cm, cd = st.columns(3)
with cy: y = st.number_input("서기(年)", 1900, 2100, 1970)
with cm: m = st.number_input("월(月)", 1, 12, 1)
with cd: d = st.number_input("일(日)", 1, 31, 27)

birth_time = st.selectbox("출생시간", ["자시", "축시", "인시", "묘시", "진시", "사시", "오시", "미시", "신시", "유시", "술시", "해시"], index=6)

st.divider()
st.subheader("사주팔자(四柱八字) 최종 확인")
t1, t2, t3, t4 = st.columns(4)
with t1: y_input = st.text_input("년주", "기유")
with t2: m_input = st.text_input("월주", "정축")
with t3: d_input = st.text_input("일주", "정미")
with t4: h_input = st.text_input("시주", "병오")

if st.button("명리체질 진단하기"):
res, final_scores = analyze_25_sang([y_input, m_input, d_input, h_input])
st.divider()
st.markdown(f"### [ {name} ] 님의 진단 결과")
st.write(f"확정 사주: {y_input}(年) {m_input}(月) {d_input}(日) {h_input}(시)")
st.success(f"판별 체질: {res}")
st.bar_chart(final_scores)
st.subheader("백경(白炅)의 양생 비책")
st.write("체질에 맞는 양생법을 실천하는 것이 건강의 척경(捷徑)입니다.")
st.divider()
st.caption("출처: 『春秋繁露(춘추번로)』 제10권 「五行之義(오행지이)」 제42편.")
