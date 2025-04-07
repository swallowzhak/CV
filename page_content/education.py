import streamlit as st

def education_page():
    st.markdown("## 教育经历")
    
    st.markdown("""
    ### 市场营销（大数据）理学硕士
    **香港中文大学 | *2024.8 - 2025.7*
    
    - GPA: 3.7/4.0
    - 主要课程: Advanced Machine Learning, Deep Learning, Natural Language Processing, Data Visualization, Statistical Methods for Data Science, Big Data Analytics
    
    ### 广告学（品牌传播）文学学士
    **华南理工大学 | *2019.9 - 2023.6*

    - GPA: 3.8/4.0
    - 主要课程: Algorithms and Data Structures, Database Systems, Computer Networks, Operating Systems, Software Engineering, Web Development
    """)
    
    st.markdown("---")
    
    st.markdown("## 获奖经历")
    
    cert1, cert2, cert3 = st.columns(3)
    
    with cert1:
        st.markdown("""
        ### 全国大学生广告艺术大赛 - 国家级优秀奖, 广东省二等奖
        **2021年**
        **Amazon Web Services** | *March 2022*
        
        Demonstrated expertise in designing, building, securing, and maintaining analytics solutions on AWS.
        """)
        
    with cert2:
        st.markdown("""
        ### TensorFlow Developer Certificate
        **Google** | *January 2022*
        
        Validated ability to develop deep learning models using TensorFlow.
        """)
        
    with cert3:
        st.markdown("""
        ### Microsoft Certified: Azure Data Scientist Associate
        **Microsoft** | *November 2021*
        
        Demonstrated expertise in using Azure services to train, evaluate, and deploy machine learning models.
        """)
    
    st.markdown("---")
    
    st.markdown("## 学术研究")
    
    st.markdown("""
    ### Sentiment Analysis of Product Reviews
    - Developed a deep learning model to analyze customer reviews and predict sentiment
    - Achieved 92% accuracy using BERT and fine-tuning techniques
    - Implemented the model as a web application using Flask
    
    ### Image Classification for Medical Diagnosis
    - Created a convolutional neural network to classify medical images
    - Worked with a dataset of X-ray images to detect pneumonia
    - Achieved 88% accuracy and deployed the model on a cloud platform
    """)
    
    st.markdown("---") 