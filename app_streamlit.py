import os
import pickle
import streamlit as st


current_path = os.path.dirname(os.path.realpath(__file__))
pickle_in = open(f"{current_path}/model.pkl", "rb")
rf = pickle.load(pickle_in)


def predict_note(variance, skewness, curtosis, entropy):
    prediction = rf.predict([[variance, skewness, curtosis, entropy]])
    return "This is my prediction" + str(prediction)


def predict_file():
    # df_test = pd.read_csv(request.files.get("test"))
    # file_prediction = rf.predict(df_test)
    return "Predcted values of test file is" + str(list("file_prediction"))


def main():
    st.title("Bank Authenticator")
    html_temp = """
    <div style="background-color: tomato; padding: 10px;">
        <h2 style="color: white; text-align: center;">
            Streamlit Bank Authenticator
        </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    variance = st.text_input("Variance", "Type Here")
    skewness = st.text_input("Skewness", "Type Here")
    curtosis = st.text_input("Curtosis", "Type Here")
    entropy = st.text_input("Entropy", "Type Here")

    result = ""
    if st.button("Predict"):
        result = predict_note(variance, skewness, curtosis, entropy)
    st.success("The output is {}".format(result))

    if st.button("About"):
        st.text("Lets Learn")
        st.text("Build with streamlit")


if __name__ == "__main__":
    main()
