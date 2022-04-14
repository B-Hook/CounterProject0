import streamlit as st


# def increaseCount():
#     global i
#     i += 1
#     st.empty
#     st.write(str(i))


def run():
    st.title('Counter Example')
    if 'count' not in st.session_state:
        st.session_state.count = 0

    increment = st.button('Increment')
    if increment:
        st.session_state.count += 1
        
    st.write('Count = ', st.session_state.count)



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
