import streamlit as st

def education_page():
    st.markdown("## 教育经历")
    
    st.markdown("""
    ### 市场营销（大数据）理学硕士
    **香港中文大学 | *2024.8 - 2025.7*
    
    - GPA: 3.7/4.0
    - 主要课程: 市场营销中的机器学习、社交媒体分析、市场营销分析、客户分析、数字营销、组织营销（B2B）、商业谈判、战略营销
    
    ### 广告学（品牌传播）文学学士
    **华南理工大学 | *2019.9 - 2023.6*

    - GPA: 3.8/4.0
    - 主要课程: 品牌战略管理、网络营销学、整合品牌传播、市场营销学、广告学原理、传播学概论、消费者行为学、公共关系学
    """)
    
    st.markdown("---")
    
    st.markdown("## 获奖经历")
    
    cert1, cert2, cert3, cert4 = st.columns(4)
    
    with cert1:
        st.markdown("""
        ### 华南理工大学毕业实习优秀实习生
        **2023年**
        """)
        
    with cert2:
        st.markdown("""
        ### 国家级创业训练项目"良好"结项
        **2022年**
        """)
        
    with cert3:
        st.markdown("""
        ### 大学生广告艺术大赛全国优秀奖、广东省三等奖
        **2021年**
        """)
        
    with cert4:
        st.markdown("""
        ### 华南理工大学校三等奖学金、三好学生
        **2021年**
        """)
    st.markdown("---")
    
    st.markdown("## 学术研究")
    
    st.markdown("""
    ### 虚拟数字人营销效果研究
    - 对虚拟数字人、形式逼真度和行为逼真度进行文献综述，厘清发展历程和研究现状
    - 通过实验研究虚拟数字人的形式真实性超过行为真实性程度对顾客购买倾向的影响
    - 运用SPSS进行数据分析，验证中介变量，为虚拟数字人的营销应用提出建议
    """)
    
    st.markdown("---") 