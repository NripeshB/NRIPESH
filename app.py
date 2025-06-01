import streamlit as st

# Set the page configuration (optional)
st.set_page_config(page_title="Happy Birthday Nripesh", layout="centered")

# Main title and subtitle
st.title("Happy Birthday Nripesh")
st.subheader("🎉🎉✨✨")

# One Piece quotes to complement the celebration
quotes = ["", "", "",
    "\"If you don't take risks, you can't create a future!\" – Monkey D. Luffy",
    "\"Yohohoho, life is a grand adventure! Let's set sail for new horizons!\" – Brook",
    "\"When do you think people die? When they are shot with a bullet? No! When they eat a soup made from a poisonous mushroom? No! People die when they are forgotten.\" – Dr. Hiriluk",
    "\"DSA ou ni, ore wa naru! – Nripesh Bhusal"
]

# Display the quotes
for quote in quotes:
    st.write(quote)

#sample 
# Add some celebratory flair
st.balloons()
