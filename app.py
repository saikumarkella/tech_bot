## importing the modules

import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
import chatmodel as cm


## pae configuration
st.set_page_config(page_title="TechBot")

st.title("Tech-Bot")

### starting the session
if 'generated' not in st.session_state:
    st.session_state['generated'] = ["Hi i am techie bot, How can i help you ?"]
    
if 'past' not in st.session_state:
    st.session_state['past'] = ['Hi!']
    
    
## designing the layout
input_container = st.container()
colored_header(label='', description='', color_name='blue-30')
response_container = st.container()


# User input
## Function for taking user provided prompt as input
def get_text():
    input_text = st.chat_input(key="input")
    return input_text

## Applying the user input box
with input_container:
    user_input = get_text()
    # print(user_input)

## Conditional display of AI generated responses as a function of user provided prompts
with response_container:
    if user_input:
        response = cm.get_response(user_input)
        st.session_state.past.append(user_input)
        st.session_state.generated.append(response)
  
    if st.session_state['generated']:
        for i in range(1,len(st.session_state['generated'])):
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
            message(st.session_state['generated'][i], key=str(i))
