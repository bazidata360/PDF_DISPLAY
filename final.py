import streamlit as st
import base64
from PIL import Image
import requests
# Create a session state to track login status
if 'login_status' not in st.session_state:
    st.session_state.login_status = False

# Check if the user is already logged in
if st.session_state.login_status:
    st.title("Welcome to the Secure Area")
    
    def main():
        st.title('')
        

    def show_pdf(file_path):
        with open(file_path,"rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="300" height="800" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)
    
    def display_NYSE_HSBC_2021():
        st.title("NYSE_HSBC_2021")
        user_link = "https://www.annualreports.com/HostedData/AnnualReportArchive/h/NYSE_HSBC_2021.pdf"  # Replace with the URL of your PDF
        if user_link:
            st.markdown(f"[{user_link}]({user_link})")
    # Embed the PDF viewer using an iframe
            st.write(f'<embed src="{user_link}" width="400%" height="800"></embed>', unsafe_allow_html=True)
    def display_LSE_BARC_2022():
        st.title("LSE_BARC_2022")
        user_link = "https://www.annualreports.com/HostedData/AnnualReports/PDF/LSE_BARC_2022.pdf"  # Replace with the URL of your PDF

        if user_link:
            st.markdown(f"[{user_link}]({user_link})")
    # Embed the PDF viewer using an iframe
            st.write("PDF Viewer:")
            st.write(f'<embed src="{user_link}" width="400%" height="800"></embed>', unsafe_allow_html=True)

    def display_NYSE_RBS_2020():
        st.title("NYSE_RBS_2020")
        user_link = "https://www.annualreports.com/HostedData/AnnualReportArchive/r/NYSE_RBS_2020.pdf"  # Replace with the URL of your PDF

        if user_link:
            st.markdown(f"[{user_link}]({user_link})")
    # Embed the PDF viewer using an iframe
            st.write("PDF Viewer:")
            st.write(f'<embed src="{user_link}" width="400%" height="800"></embed>', unsafe_allow_html=True)
        
    topic = st.sidebar.selectbox("Menu:", ["Home", "About"])

    if topic=='Home':
        feature_image1 = Image.open(r'C:\Users\marba\OneDrive\Desktop\New folder (2)\streamlit_pdf_display\2022.PNG')
        with st.container():
            image_col, text_col = st.columns((1,3))
            with image_col:
                st.image(feature_image1,caption='Image by Pixabay')
            with text_col:
                st.markdown(""" <style> .font {
                font-size:22px ; font-family: 'Black'; color: #FFFFF;} 
                </style> """, unsafe_allow_html=True)
                st.markdown('<p class="font">Barclays PLC Annual Report 2022</p>', unsafe_allow_html=True)    
                st.markdown("Our Purpose...We deploy finance responsibly to support people and businesses, acting with empathy and integrity, championing innovation and sustainability, for the common good and the long term)")

        col1, col2,col3= st.columns(3)
        with col1:
            if st.button('Read PDF Tutorial',key='1'):
                st.container()
                display_LSE_BARC_2022()
        with col2:
            st.button('Close PDF Tutorial',key='2')                   
        with col3:
            with open("LSE_BARC_2022.pdf", "rb") as pdf_file:
                PDFbyte = pdf_file.read()
            st.download_button(label="Download PDF Tutorial", key='3',data=PDFbyte,file_name="LSE_BARC_2022",mime='application/octet-stream')

        feature_image2 = Image.open(r'C:\Users\marba\OneDrive\Desktop\New folder (2)\streamlit_pdf_display\2021.PNG')
        with st.container():
            image_col, text_col = st.columns((1,3))
            with image_col:
                st.image(feature_image2,caption='Image by Pixabay')
            with text_col:
                st.markdown(""" <style> .font {
                font-size:22px ; font-family: 'Black'; color: #FFFFF;} 
                </style> """, unsafe_allow_html=True)
                st.markdown('<p class="font">HSBC Holdings plc Annual Report and Accounts 2021</p>', unsafe_allow_html=True)    
                st.markdown("Our ambition is to be the preferred international financial partner for our clients. Our purpose, ambition and values reflect our strategy and support our focus on execution.)")

        col4,col2,col3=st.columns(3)
        with col4:  
            if st.button('Read PDF Tutorial',key='4'):            
                display_NYSE_HSBC_2021()
        with col2:
            st.button('Close PDF Tutorial',key='5')                   
        with col3:
            with open("NYSE_HSBC_2021.pdf", "rb") as pdf_file:
                PDFbyte = pdf_file.read()
            st.download_button(label="Download PDF Tutorial", key='6',data=PDFbyte,file_name="NYSE_HSBC_2021",mime='application/octet-stream')
        
        
        feature_image3 = Image.open(r'C:\Users\marba\OneDrive\Desktop\New folder (2)\streamlit_pdf_display\2020.PNG')
        with st.container():
            image_col, text_col = st.columns((1,3))
            with image_col:
                st.image(feature_image3,caption='Image by Pixabay')
            with text_col:
                st.markdown(""" <style> .font {
                font-size:22px ; font-family: 'Black'; color: #FFFFF;} 
                </style> """, unsafe_allow_html=True)
                st.markdown('<p class="font">NatWest Group plc Annual Report and Accounts 2020</p>', unsafe_allow_html=True)    
                st.markdown("Our 2020 reporting suite brings together NatWest Group’s financial, non-financial and risk performance for the year. The reports are designed primarily to meet the expectations of our investors and debt holders (including green, social and sustainability (GSS) bonds)")

        col1, col2,col3= st.columns(3)
        with col1:  
            if st.button('Read PDF Tutorial',key='7'):            
                display_NYSE_RBS_2020()
        with col2:
            st.button('Close PDF Tutorial',key='8')                   
        with col3:
            with open("NYSE_RBS_2020.pdf", "rb") as pdf_file:
                PDFbyte = pdf_file.read()
            st.download_button(label="Download PDF Tutorial", key='9',data=PDFbyte,file_name="NYSE_RBS_2020",mime='application/octet-stream')   
    
    if __name__ == '__main__':
        main()

    # Add your functions and content for the secure area here
    # For example, you can add buttons to trigger various actions.
   
else:
    st.title("Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        # Check login credentials (you can replace this with your logic)
        if email == "your_email" and password == "your_password":
            st.session_state.login_status = True
        else:
            st.write("Login failed. Please try again.")

# Optionally, you can add a "Sign Up" link or other content here.
