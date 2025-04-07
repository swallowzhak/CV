import streamlit as st
from PIL import Image
import os

def home_page():
    left_col, right_col = st.columns(2)
    left_col.markdown(
        """
        <h4>陕燕姿</h4>
        <p>香港中文大学 市场营销（大数据）硕士<br>
        华南理工大学 广告学（品牌传播） 学士
        12 Chak Cheung St., Ma Liu Shui, HKSAR<br>
        <a href="mailto:yanzishan2020@163.com">yanzishan2020@163.com</a></p>
        """,
        unsafe_allow_html=True
    )

    # add a photo to the right column
    image_path = os.path.join("static", "images", "WechatIMG1788.jpg")
    if os.path.exists(image_path):
        image = Image.open(image_path)
        right_col.image(image, width=200)
    else:
        right_col.warning("Profile image not found")

    st.markdown("---")

    st.markdown(
        """
        ### 个人简介
        我是一名将于2025年从香港中文大学市场营销（大数据）专业毕业的硕士研究生，渴望在专业领域中运用所学知识和技能。在求学期间，我在数据分析、数字营销和创意策划方面打下了坚实的基础。

        在硕士课程期间，我完成了多个涉及实际商业场景和应用各种市场营销理论的项目。这些项目使我获得了商业分析、campaign策划、商业谈判和ToB营销方面的实践经验。
        
        我热衷于利用数据驱动洞察并做出明智的决策。我学习能力强，善于团队协作，并具备出色的问题解决能力。我期待在充满活力和挑战的环境中贡献自己的技能，并在数据科学领域不断成长。
        """
    )

    st.markdown(
        """
        ### 技能
        - 编程语言: Python, R
        - 数据分析: Pandas, Matplotlib
        - 数据库: SQL
        - 数据可视化: Tableau, Power BI
        - Communication: Presentation Skills
        - 其他: Microsoft Office, PR
        """
    )

    st.markdown("---")
    
    # Interactive component has been moved to the experience page 