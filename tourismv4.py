import streamlit as st

def open_url(url):
    st.link_button()

def open_places_to_visit():
    st.header("Places to Visit")
    st.subheader("Cities")
    cities_dict = {
        'Cairo': 'https://www.britannica.com/place/Cairo',
        'Luxor': 'https://www.britannica.com/place/Luxor',
        'Aswan': 'https://www.britannica.com/place/Aswan-Egypt',
        'Alexandria': 'https://www.britannica.com/place/Alexandria-Egypt',
        'Sharm El-Sheikh': 'https://www.britannica.com/place/Sharm-el-Sheikh',
        'Dahab': 'https://en.wikipedia.org/wiki/Dahab',
        'Siwa': 'https://www.britannica.com/place/Siwa-Oasis',
        'Taba': 'https://en.wikipedia.org/wiki/Taba,_Egypt',
        'Marsa Alam': 'https://en.wikipedia.org/wiki/Marsa_Alam',
        'Hurghada': 'https://en.wikipedia.org/wiki/Hurghada'
    }

    for city, url in cities_dict.items():
        st.link_button(city, url)
        #open_url(url)

    st.subheader("Categories")
    st.button("History", on_click=open_history)
    st.link_button("Medical", "https://www.egypttoursportal.com/blog/medical-tourism-in-egypt/")
    st.link_button("Chillout", "https://www.tripadvisor.com/Attraction_Review-g294201-d26686959-Reviews-ChillOut_Egypt-Cairo_Cairo_Governorate.html")

def open_history():
    st.header("History")
    st.link_button("Pharaoh", "http://giza.fas.harvard.edu/giza3d/")
    st.button("Religion", on_click=open_religion)

def open_religion():
    st.header("Religion")
    st.link_button("Islamic", "https://www.theislamicquotes.com/islamic-places-to-visit-in-egypt/")
    st.link_button("Christian", "https://www.spiritualtravels.info/spiritual-sites-around-the-world/africa/christian-holy-sites-in-egypt/")
    st.link_button("Pharaoh Religion", "https://en.wikipedia.org/wiki/Ancient_Egyptian_religion")

def main():
    st.title("Welcome to Egypt")

    # Button to open another place
    if st.button("Start"):
        open_another_place()

def open_another_place():
    st.header("Start")

    # Button for Currency Price Transfer
    st.link_button("Currency Price Transfer", "https://www.cbe.org.eg/en/economic-research/statistics/exchange-rates")

    # Button for Places to Visit
    st.button("Places to Visit", on_click=open_places_to_visit)

    # Button for Culture in Egypt
    st.link_button("Culture in Egypt", "https://www.britannica.com/place/Egypt/Daily-life-and-social-customs")

    # Button to Exit the Program
    if st.button("Exit"):
        st.stop()

if __name__ == "__main__":
    main()

