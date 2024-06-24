import streamlit as st
from fpdf import FPDF
import json

# Load data from JSON file
with open('data.json') as f:
    data = json.load(f)

# Function to generate PDF
def generate_pdf(form_data):
    pdf = FPDF()
    pdf.add_page()
    
    # Add TH Sarabun New font for Thai language support
    pdf.add_font('THSarabunNew', '', 'THSarabunNew.ttf', uni=True)
    pdf.add_font('THSarabunNew', 'B', 'THSarabunNew Bold.ttf', uni=True)
    
    pdf.set_font("THSarabunNew", 'B', 16)
    pdf.cell(200, 10, txt="รายชื่อผู้สมัครที่เลือกจาก 20 กลุ่มไขว้", ln=True, align='C')
    pdf.ln(10)
    
    pdf.set_font("THSarabunNew", '', 12)
    for row_data in form_data:
        group = row_data["Group"]
        pdf.set_font("THSarabunNew", 'B', 14)
        pdf.cell(200, 10, txt=group, ln=True)
        pdf.ln(5)
        
        pdf.set_font("THSarabunNew", '', 12)
        for key, value in row_data.items():
            if key != "Group":
                pdf.cell(0, 10, txt=f"{key}: {value}", ln=True)
        
        pdf.ln(5)
    
    pdf_file = "form_data.pdf"
    pdf.output(pdf_file)
    return pdf_file

# Streamlit app
st.set_page_config(page_title="เลือกรายชื่อผู้สมัครจาก 20 กลุ่มไขว้", layout="wide")
st.title("เลือกรายชื่อผู้สมัครจาก 20 กลุ่มไขว้")

# Custom CSS for better UI and wider select boxes
st.markdown("""
    <style>
    .main {background-color: #333333;} 
    h1 {color: #4CAF50;}
    .stButton>button {background-color: #333333; color: white; border-radius: 5px;}
    .st-form label {font-weight: bold; color: #333333;}
    .st-expander>label {color: #333333;}
    .st-expander>div>div {color: #333333;}
    .st-expander {border: 1px solid #4CAF50; border-radius: 5px; padding: 10px;}
    .stSelectbox > div:first-child {width: 400px !important;}  /* Adjust the width as needed */
    </style>
    """, unsafe_allow_html=True)

# Define column groups
column_groups = [
    ("ผู้ที่ท่านจะเลือกลำดับที่ 1-5", ["คนที่ 1: ", "คนที่ 2: ", "คนที่ 3: ", "คนที่ 4: ", "คนที่ 5: "]),
    ("ผู้ที่ท่านจะเลือกลำดับที่ 6-10 หรือกรณี 1-5ไม่ผ่าน", ["คนที่ 6: ", "คนที่ 7: ", "คนที่ 8: ", "คนที่ 9: ", "คนที่ 10: "]),
]

# Define row groups
rows = [
    "กลุ่ม 1: กลุ่มการบริหารราชการแผ่นดินและความมั่นคง",
    "กลุ่ม 2: กลุ่มกฎหมายและกระบวนการยุติธรรม",
    "กลุ่ม 3: กลุ่มการศึกษา",
    "กลุ่ม 4: กลุ่มการสาธารณสุข",
    "กลุ่ม 5: กลุ่มอาชีพทำนา ปลูกพืชล้มลุก",
    "กลุ่ม 6: กลุ่มอาชีพทำสวน ป่าไม้ ปศุสัตว์ ประมง",
    "กลุ่ม 7: กลุ่มพนักงานหรือลูกจ้างของบุคคลซึ่งมิใช่ส่วนราชการหรือหน่วยงานของรัฐ ผู้ใช้แรงงาน",
    "กลุ่ม 8: กลุ่มผู้ประกอบอาชีพด้านสิ่งแวดล้อม ผังเมือง อสังหาริมทรัพย์และสาธารณูปโภค ทรัพยากรธรรมชาติ พลังงาน",
    "กลุ่ม 9: กลุ่มผู้ประกอบกิจการขนาดกลางและขนาดย่อมตามกฎหมายว่าด้วยการนั้น",
    "กลุ่ม 10: กลุ่มผู้ประกอบกิจการอื่นนอกจากกิจการตาม (๙)",
    "กลุ่ม 11: กลุ่มผู้ประกอบธุรกิจหรืออาชีพด้านการท่องเที่ยว อันได้แก่ผู้ประกอบธุรกิจท่องเที่ยว มัคคุเทศก์ ผู้ประกอบกิจการหรือพนักงานโรงแรม",
    "กลุ่ม 12: กลุ่มผู้ประกอบอุตสาหกรรม",
    "กลุ่ม 13: กลุ่มผู้ประกอบอาชีพด้านวิทยาศาสตร์ เทคโนโลยี การสื่อสาร การพัฒนานวัตกรรม",
    "กลุ่ม 14: กลุ่มสตรี",
    "กลุ่ม 15: กลุ่มผู้สูงอายุ คนพิการหรือทุพพลภาพ กลุ่มชาติพันธุ์ กลุ่มอัตลักษณ์อื่น",
    "กลุ่ม 16: กลุ่มศิลปะ วัฒนธรรม ดนตรี การแสดงและบันเทิง นักกีฬา",
    "กลุ่ม 17: กลุ่มประชาสังคม กลุ่มองค์กรสาธารณประโยชน์",
    "กลุ่ม 18: กลุ่มสื่อสามวลชน ผู้สร้างสรรค์วรรณกรรม",
    "กลุ่ม 19: กลุ่มผู้ประกอบวิชาชีพ อาชีพอิสระ",
    "กลุ่ม 20: กลุ่มอื่นๆ"
]

# Create the form
with st.form(key='form'):
    form_data = []
    for row in rows:
        with st.expander(f"#### {row}"):
            row_data = {"Group": row}
            for group_name, columns in column_groups:
                st.markdown(f"### {group_name}")
                cols = st.columns(len(columns))
                for i, col in enumerate(cols):
                    with col:
                        options = [""] + data.get(row, [])
                        value = st.selectbox(label=columns[i], options=options, key=f"{row}_{columns[i]}")
                        row_data[columns[i]] = value
            form_data.append(row_data)
    submit_button = st.form_submit_button(label='Submit')
    
# Handle form submission
if submit_button:
    pdf_file = generate_pdf(form_data)
    st.success("Form submitted successfully!")
    with open(pdf_file, "rb") as file:
        st.download_button(label="Download PDF", data=file, file_name="เลือกรายชื่อผู้สมัครจาก20กลุ่มไขว้.pdf", mime='application/pdf')
