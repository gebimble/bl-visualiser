from enum import StrEnum

import polars as pd
import streamlit as st
import plotly.express as px

from loguru import logger

from bl_visualiser.generators.generate_competition_dataset import create_competition_dataset


DropDownFeatures = StrEnum(
    'DropDownFeatures',
    [
        # 'date',
        # 'route',
        'sex',
        # 'age',
        'name'
    ]
)


def create_dataset():
    return create_competition_dataset()


if 'dataset' not in st.session_state.keys():
    st.session_state['dataset'] = create_dataset()


# if 'date' not in st.session_state:
#     st.session_state['date'] = st.session_state['dataset']['date'].unique().sort()
#
# if 'route' not in st.session_state:
#     st.session_state['route'] = st.session_state['dataset']['route'].unique(
#     ).sort()
#
if 'sex' not in st.session_state:
    st.session_state['sex'] = st.session_state['dataset']['sex'].unique(
    ).sort().to_list()
#
# if 'age' not in st.session_state:
#     st.session_state['age'] = st.session_state['dataset']['age'].unique().sort()

if 'name' not in st.session_state:
    st.session_state['name'] = st.session_state['dataset']['name'].unique(
    ).sort().to_list()

# plot_spot = st.empty()


# def filters():
#
#     date_filter = st.session_state['dataset']['date'].isin(
#         st.session_state['date_value']) if date else True
#     route_filter = st.session_state['dataset']['route'].isin(
#         st.session_state['route_value']) if route else True
#     sex_filter = st.session_state['dataset']['sex'].isin(
#         st.session_state['sex_value']) if sex else True
#     age_filter = st.session_state['dataset']['age'].isin(
#         st.session_state['age_value']) if age else True
#     name_filter = st.session_state['dataset']['name'].isin(
#         st.session_state['name_value']) if name else True
#
#     return date_filter & route_filter & sex_filter & age_filter & name_filter


def update_name_from_sex():
    ss = st.session_state

    if ss['name_value']:
        return None

    if ss['sex_value']:
        ss['name'] = ss['dataset'].filter(
            ss['dataset']['sex'].is_in(
                ss['sex_value'])
        )['name'].unique().sort()

        return None

    value = ss['name_value']
    ss['name'] = ss['dataset']['name'].unique().sort()
    ss['name_value'] = value

    return None


def update_sex_from_name():
    ss = st.session_state

    if ss['sex_value']:
        return None

    if ss['name_value']:
        ss['sex'] = ss['dataset'].filter(
            ss['dataset']['name'].is_in(
                ss['name_value'])
        )['sex'].unique().sort()

        return None

    value = ss['sex_value']
    ss['sex'] = ss['dataset']['sex'].unique().sort()
    ss['sex_value'] = value

    return None


# def update_sidebar_content(
#     name: DropDownFeatures = None,
#     value: str = None
# ) -> None:
#     logger.debug(f'{name=}, {value=}')
#     if name is None or not st.session_state[name]:
#         logger.debug('Nothing selected, resetting dropdowns')
#         for dropdown in DropDownFeatures:
#
#             # fmt: off
#             st.session_state[dropdown.name] = st.session_state['dataset'][dropdown.name].unique()
#             # fmt: on
#
#         return None
#
#     logger.debug(f'{name} selected; modifying other dropdowns')
#
#     dropdowns_to_update = [x for x in DropDownFeatures if x.name != name]
#
#     # fmt: off
#     downselect = st.session_state['dataset'].filter(st.session_state['dataset'][name].is_in(st.session_state[value]))
#     # fmt: on
#
#     for dropdown in dropdowns_to_update:
#         if not st.session_state[f'{dropdown.name}_value']:
#             logger.debug(f'Modifying selectable content of {dropdown.name}')
#             st.session_state[dropdown.name] = downselect[dropdown.name].unique(
#             ).to_pandas()
#
#     for dropdown in DropDownFeatures:
#         logger.debug(f'{dropdown.name}: {st.session_state[dropdown.name]}')
#
#     return None


# update_sidebar_content()


# def update_plot():
#
#     groupby_terms = []
#
#     # mask = filters()
#
#     groupby_terms.append('date')
#     groupby_terms.append('route')
#
#     color = 'sex' if any([len(sex) > 1, len(sex) == 0]) else None
#     if color:
#         groupby_terms.append('sex')
#
#     return px.scatter(
#         st.session_state['dataset'].groupby(groupby_terms).mean(),
#         x='route',
#         y='score',
#         color=color,
#         # symbol='date'
#
#     )


# date = st.sidebar.multiselect(
#     label='Select a competition date',
#     key='date_value',
#     options=st.session_state['date'],
# )
# route = st.sidebar.multiselect(
#     label='Select a route',
#     key='route_value',
#     options=st.session_state['route'],
#     kwargs={
#         'name': 'route',
#         'value': 'route_value'
#     }
# )
sex = st.sidebar.multiselect(
    label='Select a sex',
    key='sex_value',
    options=st.session_state['sex'],
    on_change=update_name_from_sex,
)
# age = st.sidebar.multiselect(
#     label='Select an age group',
#     key='age_value',
#     options=st.session_state['age'],
#     kwargs={
#         'name': 'age',
#         'value': 'age_value'
#     }
# )
name = st.sidebar.multiselect(
    label='Select a climber',
    key='name_value',
    options=st.session_state['name'],
    on_change=update_sex_from_name,
    # kwargs={
    #     'name': 'name',
    #     'value': 'name_value'
    # }
)

# update_plot()

# if date:
#     update_sidebar_content(name='date', value='date_value')
#
# if route:
#     update_sidebar_content(name='route', value='route_value')
#
# if sex:
#     update_sidebar_content(name='sex', value='sex_value')
#
# if age:
#     update_sidebar_content(name='age', value='age_value')
#
# if name:
#     update_sidebar_content(name='name', value='name_value')
