import streamlit as st
import datetime

# Define your relationship start date
start_date = datetime.date(2022, 6, 22)  # Wednesday, June 22, 2022

# Get the current date
current_date = datetime.date.today()

# Calculate the duration in days, weeks, months, and years
duration_days = (current_date - start_date).days
duration_weeks = duration_days // 7
duration_months = (current_date.year - start_date.year) * 12 + (current_date.month - start_date.month)
duration_years = duration_months // 12

# Define your anniversary date for the next year
next_anniversary = start_date.replace(year=current_date.year + 1)

# Calculate the time remaining until your next anniversary
time_remaining = (next_anniversary - current_date).days

# Set the title for your app
st.title(":red[Honeylene and Brandon's Anniversary Tracker]")
st.write("----------------------------------------------")

# Create a layout using columns
col1, col2 = st.columns(2)

# In the left column, display the heart with anniversary text
with col1:
    st.markdown(
        """
        <style>
        @keyframes heartbeat {
            0% {
                transform: scale(1);
            }
            50% {
                transform: scale(1.1);
            }
            100% {
                transform: scale(1);
            }
        }
        .heartbeat {
            animation: heartbeat 2s infinite;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }
        .heart {
            fill: red; /* Set the heart color to red */
        }
        .heart-text {
            fill: white; /* Set the text color to white */
            font-size: 18px;
        }
        </style>
        <div class="heartbeat">
            <svg xmlns="http://www.w3.org/2000/svg" width="200" height="200" viewBox="0 0 24 24">
                <!-- Define the heart shape with a red fill -->
                <path class="heart" d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
            </svg>
            <!-- Embed your anniversary information as a separate text element -->
            <text x="50%" y="65%" text-anchor="middle" dominant-baseline="middle" class="heart-text">Anniversary: June 22</text>
        </div>
        """,
        unsafe_allow_html=True,
    )

# In the right column, display the relationship information in a formatted way
with col2:
    st.markdown(":blue[We've been dating for:]")
    st.write(f"- {duration_days} days")
    st.write(f"- {duration_weeks} weeks")
    st.write(f"- {duration_months} months")
    st.write(f"- {duration_years} years")
    st.write("----------------------------------------------")
    st.markdown(":blue[Time remaining until our next anniversary:]")
    st.write(f"- {time_remaining} days")
