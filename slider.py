st.text_input('Your Name', key = 'name')
age = st.slider('Your Age', min_value = 18, max_value=30)
work_experience = st.slider('Work Experience', min_value = 2, max_value = 15)

name = st.session_state.name

person = pd.DataFrame({
        'Name': name,
        'Age': age,
        'Work Experience': work_experience
    }, index = [0])

if st.checkbox('Show Details'):
    st.table(person)