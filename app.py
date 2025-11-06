import streamlit as st
import pandas as pd
from utils import get_prediction

st.title("HR Analytic")
st.header("HR Attrition Prediction")
st.write("Hello !")

company_list = ['Pvt Ltd', 'Funded Startup', 'Early Stage Startup', 'Other',
                'Public Sector', 'NGO']
size_list = ['50-99', '<10', '10000+', '5000-9999', '1000-4999', '10/49',
             '100-500', '500-999']
education_list = ['Graduate', 'Masters', 'High School', 'Phd', 'Primary School']
exp_list = ['Has relevent experience', 'No relevent experience']
last_job_list = ['1', '>4', 'never', '4', '3', '2']
major_list = ['STEM', 'Business Degree','Arts', 'Humanities', 'No Major', 'Other']
university_list = ['no_enrollment', 'Full time course', 'Part time course']
city_list = ['city_103', 'city_40', 'city_21', 'city_115', 'city_162',
       'city_176', 'city_160', 'city_46', 'city_61', 'city_114',
       'city_13', 'city_159', 'city_102', 'city_67', 'city_100',
       'city_16', 'city_71', 'city_104', 'city_64', 'city_101', 'city_83',
       'city_105', 'city_73', 'city_75', 'city_41', 'city_11', 'city_93',
       'city_90', 'city_36', 'city_20', 'city_57', 'city_152', 'city_19',
       'city_65', 'city_74', 'city_173', 'city_136', 'city_98', 'city_97',
       'city_50', 'city_138', 'city_82', 'city_157', 'city_89',
       'city_150', 'city_70', 'city_175', 'city_94', 'city_28', 'city_59',
       'city_165', 'city_145', 'city_142', 'city_26', 'city_12',
       'city_37', 'city_43', 'city_116', 'city_23', 'city_99', 'city_149',
       'city_10', 'city_45', 'city_80', 'city_128', 'city_158',
       'city_123', 'city_7', 'city_72', 'city_106', 'city_143', 'city_78',
       'city_109', 'city_24', 'city_134', 'city_48', 'city_144',
       'city_91', 'city_146', 'city_133', 'city_126', 'city_118',
       'city_9', 'city_167', 'city_27', 'city_84', 'city_54', 'city_39',
       'city_79', 'city_76', 'city_77', 'city_81', 'city_131', 'city_44',
       'city_117', 'city_155', 'city_33', 'city_141', 'city_127',
       'city_62', 'city_53', 'city_25', 'city_2', 'city_69', 'city_120',
       'city_111', 'city_30', 'city_1', 'city_140', 'city_179', 'city_55',
       'city_14', 'city_42', 'city_107', 'city_18', 'city_139',
       'city_180', 'city_166', 'city_121', 'city_129', 'city_8',
       'city_31', 'city_171']

company_type = st.selectbox(label="Company Type", options=company_list)
company_size = st.selectbox(label="Company Size", options=size_list)
education_level = st.selectbox(label="Education", options=education_list)
relevant_experience = st.selectbox(label="Has Relevant Experience", options=exp_list)
last_new_job = st.selectbox(label="Last Job", options=last_job_list)
major_dicipline = st.selectbox(label="Major Dicipline", options=major_list)
enrolled_university = st.selectbox(label="University", options=university_list)
experience = st.number_input(label="Total Experience (Year)")
city = st.selectbox(label="City", options=city_list)

df = pd.DataFrame({
    "company_type" : [company_type],
    "company_size" : [company_size],
    "education_level" : [education_level],
    "relevent_experience" : [relevant_experience],
    "last_new_job" : [last_new_job],
    "major_discipline" : [major_dicipline],
    "enrolled_university" : [enrolled_university],
    "experience" : [experience if experience <= 20 else 21],
    "city" : [city]
})

st.dataframe(df)

predict_button = st.button("Predict", use_container_width=True)

if predict_button:
    result = get_prediction(df)
    st.write("Class : ", result["class"])
    st.write(f"Prob : {result["probability"]:2%}")