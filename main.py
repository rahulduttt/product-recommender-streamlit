import streamlit as st

from recommeders.knn_tester import get_knn_recommendation
from utils.loader import load_customer_ids

# Data handling dependencies

# Data Loading
# title_list = load_product_titles('resources/dataset/amazon_reviews_us_Digital_Software_v1_00.tsv')
customer_list = load_customer_ids('resources/dataset/amazon_reviews_us_Digital_Software_v1_00.tsv')


def main():
    page_options = ["Recommender System", "Solution Overview"]

    page_selection = st.sidebar.selectbox("Choose Option", page_options)

    if page_selection == "Recommender System":
        # Header contents
        st.write('# Product Recommender Engine')
        st.write('### EXPLORE CS412 Unsupervised Predictions')
        st.image('resources/images/amazon-recommends.png', use_column_width=True)

        st.write('### Recommendation For Customers')
        selected_customer = st.selectbox('Customer ID', customer_list[14930:15200])

        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('K Nearest Neighbours',
                        'Singular Value Decomposition'))

        if sys == 'K Nearest Neighbours':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        # st.title("We think you'll like:")
                        top_recommendations = get_knn_recommendation(customer_id=selected_customer, top_n=10)
                    st.title("We think you'll like:")
                    # for i, j in enumerate(top_recommendations):
                    #     st.subheader(str(i + 1) + '. ' + j)
                    # for rec in top_recommendations:
                    #     st.subheader(rec)
                except:

                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


if __name__ == '__main__':
    main()