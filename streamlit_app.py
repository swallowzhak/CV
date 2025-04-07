import warnings
import streamlit as st

warnings.simplefilter(action="ignore", category=FutureWarning)

# Must be the first Streamlit command
st.set_page_config(page_title="陕燕姿", layout="wide")

# Import pages from the new directory
from page_content.home import home_page
from page_content.experience import experience_page
from page_content.education import education_page
from page_content.resume import resume_page
from page_content.contact import contact_page

# Import components
from components.footer import display_footer
from components.styles import load_css

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({"title": title, "function": func})

    def run(self):
        # Load custom CSS
        load_css()

        tabs = st.tabs([app["title"] for app in self.apps])
        for i, tab in enumerate(tabs):
            with tab:
                self.apps[i]["function"]()
        
        # Display footer at the bottom of each page
        display_footer()

# Initialize the app
app = MultiApp()

# Add pages to the app
app.add_app("主页", home_page)
app.add_app("教育经历", education_page)
app.add_app("工作经历", experience_page)
app.add_app("简历", resume_page)
app.add_app("联系信息", contact_page)

# Run the app
app.run()
