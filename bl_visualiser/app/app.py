import polars as pd
import streamlit as st
import plotly.express as px

from bl_visualiser.generators.generate_competition_dataset import create_competition_dataset


@st.cache_data
def create_dataset():
    return create_competition_dataset()


df = create_dataset()

plot_spot = st.empty()


def update_plot():

    print(routes)
    if routes:
        return px.scatter(
            df.filter(df['route'].is_in(routes)).groupby(
                'route', 'sex', 'score').count(),
            x='sex',
            y='count',
            color='score',
            symbol='route'

        )

    return px.scatter(
        df.groupby('route', 'sex', 'date').mean(),
        x='route',
        y='score',
        color='sex',
        symbol='date'

    )


routes = st.sidebar.multiselect(
    label='Select a route',
    options=df['route'].unique(),
    on_change=update_plot,
)
competition = st.sidebar.multiselect(
    label='Select a competition date',
    options=df['date'].unique(),
    on_change=update_plot,
)


with plot_spot:
    st.plotly_chart(update_plot())
