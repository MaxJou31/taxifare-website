
import streamlit as st
import datetime
import requests




'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''
d = st.date_input(
    "When's",
    datetime.date(2014, 7, 6))
st.write('Your date  is:', d)

t = st.time_input('Time?', datetime.time(19, 18))

st.write('Time chosen', t)




number0 = st.number_input('Insert a pickup longitude',-30)

st.write('The current pickup longitude is ', number0)


number1 = st.number_input('Insert a pickup latitude',40)

st.write('The current pickup latitude is ', number1)

number2 = st.number_input('Insert a dropoff longitude',-73)

st.write('The current dropoff longitude is ', number2)

number3 = st.number_input('Insert a dropoff latitude',40)

st.write('The current dropoff latitude is ', number3)

number4 = st.number_input('Insert a passenger count',1)

st.write('The current passenger count is ', number4)






'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''












url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...'''

params = {"pickup_datetime": f"{d} {t}",
          "pickup_longitude":number0,
          "pickup_latitude":number1,
          "dropoff_longitude":number2,
          "dropoff_latitude":number3,
          "passenger_count":number4
}

'''3. Let's call our API using the `requests` package...'''



'''
4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
if st.button('click me to see pred'):
    # print is visible in the server output, not in the page
    print('button clicked!')
    st.write('I was clicked 🎉')
    st.write('Loading')
    r = requests.get(url, params=params)
    st.write(params)
    PRED = r.json()
    st.write('Prediction:', PRED)

else:
    st.write('I was not clicked 😞')
