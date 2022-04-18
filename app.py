import streamlit as st


# def increaseCount():
#     global i
#     i += 1
#     st.empty
#     st.write(str(i))

@st.cache(allow_output_mutation=True)
def Chat():
    return []

#def update_first():
#    st.session_state.second = st.session_state.first

def run():
    st.title('Counter - Braiden Hook')

    chat=Chat()
    name = st.sidebar.text_input("Name")
    message = st.sidebar.text_area("Message")

    if 'count' not in st.session_state:
        st.session_state.count = 0

    increment = st.button('Increment')
    if increment:
        st.session_state.count += 1
        
    st.write('Count = ', st.session_state.count)
    
    if st.sidebar.button("Post chat message"):
        chat.append((name,message))

    try:
        names, messages = zip(*chat)
        chat1 = dict(Name = names, Message =  messages)
        st.table(chat1)
    except ValueError:
        st.title("Enter your name and message into the sidebar, and post!")
    #st.text_input(label='Textbox 1', key='first', on_change=update_first)




if __name__=='__main__':
    run()
    #number = st.write("0")



    # placeholder = st.empty()
    # clicked = st.button("Add to count")
    # if clicked:
    #     i += 1
    #     placeholder.text(str(i))

    # placeholder = st.empty()
    # if st.button("Add to count"):
    #     i += 1
    #     placeholder.text(str(i))





# app = st(__name__)
#
# i = -1
#
# @app.route("/")
# def hello():
#     global i
#     i += 1
#     return str(i)
#
# if __name__=='__main__':
#     app.run(debug=True)
