import streamlit as st

def contact_page():
    st.markdown("## 与我联系")
    
    st.markdown("""
    欢迎通过以下任何渠道与我联系：
    
    ### Direct Contact
    - **Email**: [yanzishan2020@163.com](mailto:yanzishan2020@163.com)
    - **Phone**: +86 18834698169
    - **LinkedIn**: [linkedin.com/in/yanzishan](https://linkedin.com/in/yanzishan)
    """)
    
    st.markdown("### 给我发消息")
    
    with st.form("联系表单"):
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("姓名")
            email = st.text_input("邮箱")
            
        with col2:
            subject = st.text_input("主题")
            
        message = st.text_area("留言内容", height=150)
        
        submitted = st.form_submit_button("发送消息")
        
        if submitted:
            st.success("感谢您的留言！我会尽快回复。")
            # In a real application, you would process the form data here
            # For example, send an email or store in a database
    
    st.markdown("---")
    
   