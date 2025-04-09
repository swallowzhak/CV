import streamlit as st
from PIL import Image
import os

def home_page():
    left_col, right_col = st.columns([1, 1.2])  # 调整列宽比例使内容更紧凑
    
    # add a photo to the left column
    image_path = os.path.join("static", "images", "IMG_4496.jpg")
    if os.path.exists(image_path):
        image = Image.open(image_path)
        # 提高图片清晰度并保持较小尺寸
        image = image.resize((300, int(300 * image.size[1] / image.size[0])), Image.Resampling.LANCZOS)
        # 修改这一行
        with left_col:
            st.empty()  # 添加空白占位符用于垂直居中
            st.image(image, width=200)
            st.empty()  # 添加空白占位符用于垂直居中
    else:
        left_col.warning("Profile image not found")

    # 使用CSS样式实现文字垂直居中
    right_col.markdown(
        """
        <div style="display: flex; flex-direction: column; justify-content: center; height: 100%;">
            <h4>陕燕姿</h4>
            <p>香港中文大学 市场营销（大数据）硕士<br>
            华南理工大学 广告学（品牌传播） 学士<br>
            12 Chak Cheung St., Ma Liu Shui, HKSAR<br>
            <a href="mailto:yanzishan2020@163.com">yanzishan2020@163.com</a></p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown(
        """
        ### 个人简介
        我是一名将于2025年从香港中文大学市场营销（大数据）专业毕业的研究生，渴望在专业领域中运用所学知识和技能。在求学期间，我在数据分析、数字营销和创意策划方面打下了坚实的基础。

        在硕士课程期间，我完成了多个涉及实际商业场景和应用各种市场营销理论的项目。在这些项目中，我获得了商业分析、Campaign策划、商业谈判和ToB营销方面的实践经验。
        
        我热衷于利用数据驱动洞察并做出明智的决策。我学习能力强，善于团队协作，并具备出色的问题解决能力。期待在充满活力和挑战的环境中贡献自己的技能，并在市场营销领域不断成长。
        """
    )

    st.markdown(
        """
        ### 专业技能
        - 数据分析：Python (Pandas, NumPy), R, SQL
        - 商业分析：市场调研, 竞品分析, 用户画像
        - 营销技能：数字营销, 品牌策划, 活动运营
        - 办公工具：Adobe PR, PS, Microsoft Office
        - 语言能力：中文（母语）, 英语（流利）
        """
    )

    st.markdown("---")
    
    # Interactive component has been moved to the experience page