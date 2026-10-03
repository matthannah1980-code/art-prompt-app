from datetime import datetime
import streamlit as st

st.set_page_config(
    page_title="Daily Art Prompt Generator", page_icon="🎨", layout="centered"
)

# Curated list of prompts with reference image examples
PROMPTS = [
    {
        "subject": "A vintage fountain pen with cap off",
        "category": "Objects",
        "difficulty": "Moderate",
        "tip": (
            "Focus on metallic highlights, threaded barrel details, and ink"
            " reflection."
        ),
        "image_url": (
            "https://images.unsplash.com/photo-1583485088034-697b5bc54ccd?w=800"
        ),
    },
    {
        "subject": "A sleeping cat curled in a tight circle",
        "category": "Animals & Life",
        "difficulty": "Moderate",
        "tip": (
            "Pay close attention to overlapping forms and soft fur contours"
            " rather than individual hairs."
        ),
        "image_url": (
            "https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?w=800"
        ),
    },
    {
        "subject": "A single textured monstera leaf",
        "category": "Botanicals",
        "difficulty": "Simple",
        "tip": (
            "Capture the unique fenestrations (splits) and the subtle curve of"
            " the main vein."
        ),
        "image_url": (
            "https://images.unsplash.com/photo-1614594975525-e45190c55d0b?w=800"
        ),
    },
    {
        "subject": "A rustic brass lantern",
        "category": "Objects",
        "difficulty": "Detailed",
        "tip": (
            "Balance the hard geometric cage lines with soft glass refraction"
            " effects."
        ),
        "image_url": (
            "https://images.unsplash.com/photo-1513519245088-0e12902e5a38?w=800"
        ),
    },
    {
        "subject": "A heavy ceramic coffee mug with a chipped rim",
        "category": "Still Life",
        "difficulty": "Simple",
        "tip": (
            "Use uneven lighting to emphasize the weight of the clay and glaze"
            " thickness."
        ),
        "image_url": (
            "https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?w=800"
        ),
    },
]

# Select prompt based on day of the year for a consistent daily experience
day_of_year = datetime.now().timetuple().tm_yday
current_prompt = PROMPTS[day_of_year % len(PROMPTS)]

st.title("🎨 Daily Studio Art Prompt")
st.write(
    "A daily exercise designed to challenge your observational skills without"
    " overwhelming your schedule."
)

st.markdown("---")

# Display Today's Prompt Card
st.subheader(f"📅 Today's Subject: {current_prompt['subject']}")
col1, col2 = st.columns(2)
with col1:
  st.markdown(f"**Category:** {current_prompt['category']}")
with col2:
  st.markdown(f"**Complexity:** {current_prompt['difficulty']}")

st.info(f"💡 **Artist Focus Tip:** {current_prompt['tip']}")

# Display visual example reference image
st.markdown("### Visual Reference Example")
st.image(
    current_prompt["image_url"],
    caption=f"Reference Example: {current_prompt['subject']}",
    use_container_width=True,
)

st.markdown("---")

# User Sketch Tracker / Notes Section
st.subheader("Your Studio Session")
notes = st.text_area(
    "Jot down your color palette notes, medium choices, or lighting"
    " observations:"
)

if st.button("Mark Today's Prompt Complete", type="primary"):
  st.success("Great work! Session logged for today.")

# Optional image uploader to store your finished piece
uploaded_sketch = st.file_uploader(
    "Upload a photo of your finished sketch or painting",
    type=["png", "jpg", "jpeg"],
)
if uploaded_sketch:
  st.image(uploaded_sketch, caption="Today's Study", use_container_width=True)