import streamlit as st
import random

# Title
st.title("🎮 Rock-Paper-Scissors Game")

# Initialize session state
if "user_score" not in st.session_state:
    st.session_state.user_score = 0
if "computer_score" not in st.session_state:
    st.session_state.computer_score = 0
if "round" not in st.session_state:
    st.session_state.round = 1

# Choices
choices = ["rock", "paper", "scissors"]
user_choice = st.radio("Choose your move:", choices, horizontal=True)

if st.button("Play Round"):
    computer_choice = random.choice(choices)
    st.write(f"🧠 Computer chose: **{computer_choice}**")

    if user_choice == computer_choice:
        st.info("🤝 It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        st.success("✅ You win this round!")
        st.session_state.user_score += 1
    else:
        st.error("❌ You lose this round!")
        st.session_state.computer_score += 1

    st.session_state.round += 1

# Scoreboard
st.markdown("---")
st.subheader("🏆 Scoreboard")
st.write(f"**You:** {st.session_state.user_score}")
st.write(f"**Computer:** {st.session_state.computer_score}")

# Reset Button
if st.button("🔄 Restart Game"):
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.session_state.round = 1
    st.success("Game has been reset!")

