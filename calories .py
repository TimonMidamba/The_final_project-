import streamlit as st
import datetime
import pandas as pd

# Page configuration
st.set_page_config(page_title="Smart Health Assistant", page_icon="🧠")

st.title("🧠 Smart Health Assistant")
st.write(f"🕒 Current Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Initialize session state variables
if 'food_log' not in st.session_state:
    st.session_state.food_log = []
if 'total_calories' not in st.session_state:
    st.session_state.total_calories = 0

# 🔁 Reset Button
if st.button("🔁 Reset Log"):
    st.session_state.food_log = []
    st.session_state.total_calories = 0
    st.success("✅ Food log and calories reset.")

# 🍽️ Meal Check
st.subheader("🍽️ Meal Check")
food = st.radio("Have you taken a meal?", ["Yes", "No"])
if food == "No":
    st.warning("⚠️ Please take a meal first to proceed!")
    st.stop()
else:
    st.success("✅ Good you have taken a meal.")

# 🏃 Exercise Check
st.subheader("🏃 Exercise Check")
exercise = st.radio("Have you done any exercise today?", ["Yes", "No"])
if exercise == "No":
    st.warning("⚠️ Please do some exercise!")
else:
    st.success("✅ Well done!")

# 🥗 Food Log & Calorie Tracker
st.subheader("🥗 Food Log & Calorie Tracker")
food_type = st.text_input("Enter food type:")
calories = st.number_input("Enter calories for this food:", min_value=0)

if st.button("Add Food"):
    if food_type and calories > 0:
        st.session_state.food_log.append((food_type, calories))
        st.session_state.total_calories += calories
        st.success(f"✅ Added {food_type} with {calories} calories.")
    else:
        st.error("❌ Please enter both food name and calories.")

# Show food log
if st.session_state.food_log:
    st.write("### 📝 Food Items Logged:")
    for i, (food_item, cal) in enumerate(st.session_state.food_log, start=1):
        st.write(f"{i}. {food_item} - {cal} cal")

    # Show total and chart after at least 3 entries
    if len(st.session_state.food_log) >= 3:
        st.write(f"**🔥 Total Calories Today:** {st.session_state.total_calories}")
        if st.session_state.total_calories > 2200:
            st.error("⚠️ You are overeating!")
        else:
            st.success("✅ You are eating well.")

        # 📊 Bar chart
        df = pd.DataFrame(st.session_state.food_log, columns=["Food", "Calories"])
        st.bar_chart(df.set_index("Food"))
    else:
        st.info("ℹ️ Please log at least **3 food items** to see your total calorie intake and chart.")

# 💧 Water Reminder
st.info("💧 Remember to drink at least 2 litres of water daily!")

# 😊 Mood Tracker
st.subheader("😊 Mood Tracker")
mood = st.text_input("How are you feeling today?")
if mood:
    mood_lower = mood.lower()
    if any(word in mood_lower for word in ["sad", "stressed", "depressed", "anxious", "down", "tired", "lonely"]):
        st.warning(f"😟 It's okay to feel {mood}. You're not alone.")
        st.info("💬 Please talk to someone you trust — a friend, a counselor, or a family member.\n\nYou're strong, and better days are coming. 🌈")
    else:
        st.success(f"😊 It's great to hear you're feeling {mood}. Keep going and take care of yourself! 💪")
