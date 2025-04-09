import streamlit as st
import base64
import os

def resume_page():
    pdf_file_path = os.path.join("static", "docs", "CV-陕燕姿_副本.pdf")

    if os.path.exists(pdf_file_path):
        with open(pdf_file_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        # Display the download button
        st.download_button(label="下载简历",
                        data=PDFbyte,
                        file_name="CV_陕燕姿.pdf",
                        mime='application/octet-stream')
    else:
        st.warning("Resume PDF file not found")

    st.title("陕燕姿")

    st.header("联系信息")
    st.markdown("""
    - **Email:** yanzishan2020@163.com
    - **Phone:** (+86) 18834698169
    - **LinkedIn:** [linkedin.com/in/yanzishan](https://www.linkedin.com/in/yanzishan?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app)
    - **Address:** 香港特别行政区 新界 沙田区
    """)

    st.header("个人总结")
    st.markdown("""
    热爱市场营销相关工作，具备专业背景和多段相关实习经验，涉及互联网、教育、家电、家具、数码、地产行业。
数据分析与创意策划能力兼备，擅长快速学习，具备出色的抗压能力、领导力和落地执行能力。
    """)

    st.header("实习经历")
    
    st.markdown("""
    ### 营销策划实习生
    **小红书** | 营销中心 - 家生活&潮数码行业策划 | *2024年3月 - 2024年7月*
    
    - 参与策划小红书家生活/数码行业IP通案，分析IP矩阵并优化内容，完成6个IP通案撰写，成功吸引12个品牌合作意向，实现招商1980万元
    - 参与23场IP营销活动策划并落地15个项目，独立完成10个策划案获海尔、松下等品牌认可，落地5个项目，独立策划活动创收1680万元
    - 统筹15个项目全链路落地，负责执行需求对接、H5设计、文案撰写等环节，与各方协同保障活动效果，实现平均曝光量1亿+及互动量30万+
    """)
    
    st.markdown("""
    ### 社交媒体营销实习生
    **猿辅导** | 斑马百科 - 市场部 | *2023年11月 - 2024年2月*
    
    - 负责斑马百科APP在小红书、抖音的KOC投放，拓展母婴亲子类KOC资源500+，从0到1打通抖音KOC合作链路，季度合作230+博主（超额完成50%目标）
    - 负责投放策略制定及优化全流程，小红书博主软文平均阅读量1.2w（CPV<0.05），抖音博主视频平均播放量12w（CPM<3），带货417单创收6万+
    - 策划「我是百科小老师」UGC活动，激励用户发布孩子讲解知识视频，产生180+用户作品，负责活动物料设计、资源位安排及优秀作品二次传播
    """)
    
    st.markdown("""
    ### 市场活动实习生
    **中海物业** | 市场部 | *2021年9月 - 2021年12月*
    
    - 深度参与举办"方舟生活节"系列品牌活动，结合售楼部实地花店场景策划艺术插花教学活动，负责物料制作对接、活动布场及宣传文案，一人同时对接30+合作方
    - 负责官方公众号运营，构思私域宣传文案并通过话术引导客户阅读，文章平均阅读量1000+，有效提升活动影响力
    - 参与双十二"幸福来敲门"直播活动全流程，负责脚本撰写、流程对接、物料制作及布场等工作，邀请专家诠释"幸福"理念并融入楼盘推荐，直播观看量4万+位居分公司第一
    """)
    
    st.markdown("""
    ### 电视台实习生
    **晋城电视台** | 社会一部 | *2021年6月 - 2021年8月*
    
    - 参与年度晚会"双拥花开太行山"的筹备和录制，负责物料设计对接、颁奖词撰写、后期剪辑
    - 作为小组导演和制片，独立构思并参与医保科普相关短视频剧本编写、录制、剪辑和出镜，视频在抖音平台平均播放量超过3000
    - 独立负责全市党史知识竞赛的赛程设计，构想赛制与规则，确保赛事规则的公平性与赛事类节目看点
    """)
    st.markdown("---")

    st.header("教育经历")
    st.markdown("""
    **市场营销（大数据）理学硕士**
    - 香港中文大学
    - *Graduated: 2025.7*
    - GPA: 3.7/4.0
    """)
    st.markdown("""
    **广告学（品牌传播）文学学士**
    - 华南理工大学
    - *Graduated: 2023.6*
    - GPA: 3.8/4.0
    """)

    st.header("技能")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 专业技能
        - **编程语言:** Python, R, SQL
        - **办公软件:** Microsoft Office
        - **设计工具:** Canva, Adobe Premiere Pro, Adobe Photoshop
        - **专业技能:** 营销策划, 文案撰写, 摄影
        """)
        
    with col2:
        st.markdown("""
        ### 软实力
        - **沟通能力:** 优秀的书面和口头表达能力
        - **团队协作:** 具有丰富的团队协作经验
        - **解决问题:** 强大的分析和批判性思维能力
        - **时间管理:** 高效的任务优先级排序和按期交付能力
        - **适应能力:** 快速学习并在动态环境中快速成长
        """)

    st.header("获奖情况")
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

    st.header("项目经历")
    projects = [
        {
            "title": "七月浮游艺术创意文化工作室",
            "description": "负责工作室商业策划书撰写，获国创项目良好结题并受邀参与全国创新创业年会；策划【毕业季】采访和【心动】主题征集活动，吸引90+参与者，引流110+新粉丝；运营3个粉丝社群，制定SOP维持日活，实现裂变增长至460人。",
            "skills": ["商业策划", "活动策划", "社群运营", "内容运营"],
            "outcome": "获国创项目良好结题，成功运营460人社群"
        },
        {
            "title": "爱华仕一帆风顺系列品牌传播策划",
            "description": "为爱华仕\"一帆风顺\"系列行李箱策划营销活动，以『形影箱随，足迹纷飞』为主题构建整合品牌传播策略。策划行李收纳赛、涂鸦大师行李箱定制等创意营销活动，结合商旅、旅游季、毕业季场景撰写TVC脚本。",
            "skills": ["品牌策划", "创意营销", "TVC脚本撰写", "整合传播"],
            "outcome": "获得第13届全国大学生广告艺术大赛国家级优秀奖、广东省三等奖"
        }
    ]
    
    for i, project in enumerate(projects):
        with st.expander(f"{project['title']}", expanded=i==0):
            st.markdown(f"**项目描述：** {project['description']}")
            st.markdown(f"**使用技能：** {', '.join(project['skills'])}")
            st.markdown(f"**项目成果：** {project['outcome']}")
    

    
    st.markdown("---")

    st.header("语言")
    st.markdown("""
    - **英语:** 流利
    - **粤语:** 中等
    """)

    st.header("兴趣爱好")
    st.markdown("""
    - 主持
    - 阅读
    - 旅行
    - 羽毛球
    """)

    st.markdown("---")