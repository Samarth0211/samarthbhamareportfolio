import streamlit as st

st.markdown(
    """
    <style>
    body {
        background-color: #232323;
        color: white;
        font-family: 'Arial', sans-serif;
    }
    h1, h2, h3 {
        font-weight: bold;
    }
    .button {
        background-color: red;
        color: white;
        font-weight: bold;
        padding: 10px 20px;
        border-radius: 4px;
    }
    .button:hover {
        background-color: #FF5733;
    }
    .content {
        margin: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Update button styling
button_style = 'class="button"'


# st.title('Samarth Bhamare Portfolio')
# st.markdown("Passionate Data Science enthusiast with a solid background in computer science. Proficient in data analytics and skilled in Python. I've actively engaged in diverse projects encompassing Regression, Classification and more, showcasing a well-rounded understanding of data analysis techniques.")

col20, col21 = st.columns([1, 4])  # Split the layout into two columns

# In the first column (col1), you can add the title and markdown
with col21:
    st.title('Samarth Bhamare Portfolio')
    st.markdown("Passionate Data Science enthusiast with a solid background in computer science. Proficient in data analytics and skilled in Python. I've actively engaged in diverse projects encompassing Regression, Classification and more, showcasing a well-rounded understanding of data analysis techniques.")

# In the second column (col2), you can add your image
with col20:
    st.image('myimage.png', use_column_width=True)


# Custom CSS styling for the buttons
button_style = (
    'width: 200px; '
    'background-color: red; '
    'color: white; '
    'padding: 10px 1px; '
    'text-align: center; '
    'text-decoration: none; '
    'display: inline-block; '
    'font-size: 16px; '
    'font-weight: bold; '  # Added bold text
    'margin: 0 1px; '
    'cursor: pointer; '
    'border-radius: 4px;'
)
d_button_style = (
    'width: 200px; '
    'background-color: green; '
    'color: white; '
    'padding: 10px; '
    'text-align: center; '
    'text-decoration: none; '
    'display: inline-block; '
    'font-size: 16px; '
    'font-weight: bold; '  # Added bold text
    'margin: 0 1px; '
    'cursor: pointer; '
    'border-radius: 4px;'
)
p_button_style = (
    'width: 170px; '
    'background-color: green; '
    'color: white; '
    'padding: 10px; '
    'text-align: center; '
    'text-decoration: none; '
    'display: inline-block; '
    'font-size: 16px; '
    'font-weight: bold; '  # Added bold text
    'margin: 0 1px; '
    'cursor: pointer; '
    'border-radius: 4px;'
)
custom_widget = (
        'display: grid;'
        'border: 1px solid black;'
        'padding: 12px;'
        'border-radius: 5%;'
        'color: #003366;'
        'margin-bottom: 5px;'
        'min-height: 251.56px;'
        'align-items: center;'
)

tabs = ["Machine Learning Projects", "PowerBI Projects"]
selected_tab = st.selectbox("Select Tab:", tabs)


if selected_tab == "Machine Learning Projects":
    st.title('Machine Learning Projects')
    # Use HTML to create styled link buttons
    st.header('1. Movie Recommender System')
    st.image('movie recommender.png', use_column_width="auto")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<a style="{}" href="https://movie-recommeder-system.streamlit.app/" target="_blank">Live Project</a>'.format(button_style), unsafe_allow_html=True)
    with col2:
        st.markdown('<a style="{}" href="https://github.com/Samarth0211/movie-recommeder" target="_blank">GitHub Link</a>'.format(button_style), unsafe_allow_html=True)
    with col3:
        st.markdown('<a style="{}" href="https://github.com/Samarth0211/movie-recommeder/archive/refs/heads/main.zip" target="_blank">Download Code</a>'.format(d_button_style), unsafe_allow_html=True)

    st.header('2. IPL Winner Predictor')
    st.image('ipl.png', use_column_width="auto")
    col4, col5, col6 = st.columns(3)
    with col4:
        st.markdown('<a style="{}" href="https://iplwinnerpredictor.streamlit.app/" target="_blank">Live Project</a>'.format(button_style), unsafe_allow_html=True)
    with col5:
        st.markdown('<a style="{}" href="https://github.com/Samarth0211/IPL_Winner_Predictor" target="_blank">GitHub Link</a>'.format(button_style), unsafe_allow_html=True)
    with col6:
        st.markdown('<a style="{}" href="https://github.com/Samarth0211/IPL_Winner_Predictor/archive/refs/heads/main.zip" target="_blank">Download Code</a>'.format(d_button_style), unsafe_allow_html=True)

    st.header('3. WhatsApp Chat Analyser')
    st.image('whatsapp.png', use_column_width="auto")
    col7, col8, col9 = st.columns(3)
    with col7:
        st.markdown('<a style="{}" href="https://analyze-whatsapp-chat.streamlit.app/" target="_blank">Live Project</a>'.format(button_style), unsafe_allow_html=True)
    with col8:
        st.markdown('<a style="{}" href="https://github.com/Samarth0211/whatsapp-chat-analyzer" target="_blank">GitHub Link</a>'.format(button_style), unsafe_allow_html=True)
    with col9:
        st.markdown('<a style="{}" href="https://github.com/Samarth0211/whatsapp-chat-analyzer/archive/refs/heads/main.zip" target="_blank">Download Code</a>'.format(d_button_style), unsafe_allow_html=True)

    st.header('4. Email Spam Classifier')
    st.image('spam email.png', use_column_width="auto")
    col10, col11, col12 = st.columns(3)
    with col10:
        st.markdown('<a style="{}" href="https://spamemailclassify.streamlit.app/" target="_blank">Live Project</a>'.format(button_style), unsafe_allow_html=True)
    with col11:
        st.markdown('<a style="{}" href="https://github.com/Samarth0211/email-spam-classify" target="_blank">GitHub Link</a>'.format(button_style), unsafe_allow_html=True)
    with col12:
        st.markdown('<a style="{}" href="https://github.com/Samarth0211/email-spam-classify/archive/refs/heads/main.zip" target="_blank">Download Code</a>'.format(d_button_style), unsafe_allow_html=True)

    st.header('5. Car Price Predictor')
    st.image('car price.png', use_column_width="auto")
    col13, col14, col15 = st.columns(3)
    with col13:
        st.markdown('<a style="{}" href="https://car-price-prediction2.streamlit.app/" target="_blank">Live Project</a>'.format(button_style), unsafe_allow_html=True)
    with col14:
        st.markdown('<a style="{}" href="https://github.com/Samarth0211/car-price-prediction/" target="_blank">GitHub Link</a>'.format(button_style), unsafe_allow_html=True)
    with col15:
        st.markdown('<a style="{}" href="https://github.com/Samarth0211/car-price-prediction/archive/refs/heads/main.zip" target="_blank">Download Code</a>'.format(d_button_style), unsafe_allow_html=True)

    st.header('6. Laptop Price Predictor')
    st.image('laptop.png', use_column_width="auto")
    col16, col17, col18 = st.columns(3)
    with col16:
        st.markdown('<a style="{}" href="https://predict-laptop-price2.streamlit.app/" target="_blank">Live Project</a>'.format(button_style), unsafe_allow_html=True)
    with col17:
        st.markdown('<a style="{}" href="https://github.com/Samarth0211/laptop-price-predictor/" target="_blank">GitHub Link</a>'.format(button_style), unsafe_allow_html=True)
    with col18:
        st.markdown('<a style="{}" href="https://github.com/Samarth0211/laptop-price-predictor/archive/refs/heads/main.zip" target="_blank">Download Code</a>'.format(d_button_style), unsafe_allow_html=True)


if selected_tab == "PowerBI Projects":
    st.title('PowerBI Projects')
    st.markdown('---')
    col19,col20 = st.columns(2)
    with col19:
        st.header('1. Netflix Analysis Dashboard')
        st.image('PowerBI/Netflix Dashboard.jpg', use_column_width="auto")
        st.markdown(
            """
            <div style="display: flex; justify-content: center; align-items: center;">
                <a style="{}" href="https://github.com/Samarth0211/PowerBI-NetflixDashbaord/archive/refs/heads/main.zip" target="_blank">Download Project</a>
            </div>
            """.format(p_button_style),
            unsafe_allow_html=True
        )
    with col20:
        st.header('2. IPL Analysis Dashboard')
        st.image('PowerBI/ipl_dashboard.jpg', use_column_width="auto")
        st.markdown(
            """
            <div style="display: flex; justify-content: center; align-items: center;">
                <a style="{}" href="https://github.com/Samarth0211/PowerBI-IPLDashboard/archive/refs/heads/main.zip" target="_blank">Download Project</a>
            </div>
            """.format(p_button_style),
            unsafe_allow_html=True
        )
    st.markdown('---')
    col21, col22 = st.columns(2)
    with col21:
        st.header('3. Road Accident Analysis Dashboard')
        st.image('PowerBI/Road Accident Dashboard.jpg', use_column_width="auto")
        st.markdown(
            """
            <div style="display: flex; justify-content: center; align-items: center;">
                <a style="{}" href="https://github.com/Samarth0211/PowerBI-RoadAccident/archive/refs/heads/main.zip" target="_blank">Download Project</a>
            </div>
            """.format(p_button_style),
            unsafe_allow_html=True
        )
    with col22:
        st.header('4. Diwali Sales Analysis Dashboard')
        st.image('PowerBI/diwali sales dashboard.jpg', use_column_width="auto")
        st.markdown(
            """
            <div style="display: flex; justify-content: center; align-items: center;">
                <a style="{}" href="https://github.com/Samarth0211/PowerBI-DiwaliSalesAnalysis/archive/refs/heads/main.zip" target="_blank">Download Project</a>
            </div>
            """.format(p_button_style),
            unsafe_allow_html=True
        )

st.markdown('---')

if st.button("Contact Me", use_container_width=True, type='primary'):
    st.markdown(
        """
        <style>
        .text-with-background {
            background-color: rgba(0, 0, 0, 0.8); /* Transparent black */
            padding: 10px;
            border-radius: 5px;
            color: white; /* Text color */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Your contact details with transparent black background
    st.markdown('<div class="text-with-background">📞 Phone: +91-9075002770</div>', unsafe_allow_html=True)
    st.markdown('<div class="text-with-background">✉️ Email: samarthbhamareofficial@gamil.com</div>', unsafe_allow_html=True)

    # Link to your LinkedIn profile with transparent black background
    linkedin_url = "https://www.linkedin.com/in/your-profile/"
    st.markdown(f'<div class="text-with-background">🔗 LinkedIn: <a href="{linkedin_url}">{linkedin_url}</a></div>', unsafe_allow_html=True)

