
import streamlit as st
import folium
from streamlit_folium import st_folium

# App title
st.set_page_config(page_title="Seoul Tourist Attractions Map", page_icon="🌏", layout="wide")
st.title("🌸 Top 10 Tourist Attractions in Seoul (Loved by Foreign Visitors)")
st.markdown("Explore Seoul's most famous landmarks that attract millions of international tourists every year! 🇰🇷")

# Coordinates of Seoul
seoul_center = [37.5665, 126.9780]

# Create map
m = folium.Map(location=seoul_center, zoom_start=12)

# Top 10 attractions (with coordinates and brief info)
attractions = [
    {"name": "Gyeongbokgung Palace", "coords": [37.5796, 126.9770], "desc": "Historic royal palace built in 1395 — the heart of Joseon Dynasty."},
    {"name": "Bukchon Hanok Village", "coords": [37.5826, 126.9830], "desc": "Traditional Korean houses offering a glimpse of old Seoul."},
    {"name": "Insadong", "coords": [37.5740, 126.9858], "desc": "Cultural street full of galleries, tea houses, and craft shops."},
    {"name": "Myeongdong Shopping Street", "coords": [37.5636, 126.9865], "desc": "Seoul’s most vibrant shopping area for fashion and skincare."},
    {"name": "N Seoul Tower (Namsan Tower)", "coords": [37.5512, 126.9882], "desc": "Iconic tower offering panoramic views of the city."},
    {"name": "Dongdaemun Design Plaza (DDP)", "coords": [37.5663, 127.0095], "desc": "Modern architectural landmark famous for design exhibitions."},
    {"name": "Lotte World", "coords": [37.5110, 127.0980], "desc": "One of the world’s largest indoor amusement parks."},
    {"name": "Hongdae", "coords": [37.5572, 126.9245], "desc": "Trendy youth district known for street art and live music."},
    {"name": "Itaewon", "coords": [37.5345, 126.9946], "desc": "Global neighborhood with international food and nightlife."},
    {"name": "Changdeokgung Palace & Secret Garden", "coords": [37.5794, 126.9910], "desc": "UNESCO World Heritage Site famous for its beautiful garden."}
]

# Add markers to map
for spot in attractions:
    folium.Marker(
        location=spot["coords"],
        popup=f"<b>{spot['name']}</b><br>{spot['desc']}",
        tooltip=spot["name"],
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(m)

# Display Folium map in Streamlit
st_data = st_folium(m, width=800, height=600)
