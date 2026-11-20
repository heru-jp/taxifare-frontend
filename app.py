import streamlit as st
import requests

st.title("🚕🍆 Taxifare Front")
st.markdown("Enter the specific data for your taxi ride below.")


pickup_datetime = st.date_input("Select a date", format="YYYY-MM-DD")

if pickup_datetime is not None:
    date_str = pickup_datetime.strftime("%Y-%m-%d")



pickup_longitude = st.number_input(
    "pickup_longitude", min_value=0.0, value=39.1, step=0.1
)
pickup_latitude = st.number_input(
    "pickup_latitude", min_value=0.0, value=18.7, step=0.1
)
dropoff_longitude = st.number_input(
    "dropoff_longitude", min_value=0.0, value=181.0, step=1.0
)
dropoff_latitude = st.number_input(
    "dropoff_latitude", min_value=0.0, value=3750.0, step=10.0
)
passenger_count = st.number_input(
    "passenger_count", min_value=0, value=3750, step=10
)

url = st.secrets['API_URL']

if st.button("Predict Fare"):
  params = {
      "pickup_datetime": date_str,
      "pickup_longitude": pickup_longitude,
      "pickup_latitude": pickup_latitude,
      "dropoff_longitude": dropoff_longitude,
      "dropoff_latitude": dropoff_latitude,
      "passenger_count": passenger_count,
  }
  try:
    response = requests.get(url, params=params)
    response.raise_for_status()
    prediction = response.json()
    st.success(f"Predicted Taxifare: **{prediction}**")
  except requests.exceptions.RequestException as e:
    st.error(f"Error calling the API: {e}")
