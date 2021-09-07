from src.types import FeedData

mock_data = {
    "1": [{"feed_id": "100",
           "feed_data": FeedData(
               provider_identifier="1000",
               age_0=False,
               age_1=True,
               age_2=False,
               state_0=True,
               state_1=False,
               state_2=False,
               diagnosis_0=True,
               diagnosis_1=False,
               diagnosis_2=False,
               gender_male=True,
               year_2019=True,
               year_2020=False,
               year_2021=False,
               month_1=True,
               month_2=False,
               month_3=False
           )},
          {"feed_id": "200",
           "feed_data": FeedData(
               provider_identifier="2000",
               age_0=True,
               age_1=False,
               age_2=False,
               state_0=False,
               state_1=True,
               state_2=False,
               diagnosis_0=False,
               diagnosis_1=True,
               diagnosis_2=False,
               gender_male=True,
               year_2019=False,
               year_2020=True,
               year_2021=False,
               month_1=False,
               month_2=True,
               month_3=False
           )}
          ],
    "2": [
        {"feed_id": "100",
         "feed_data":
             FeedData(
                 provider_identifier="1000",
                 age_0=False,
                 age_1=False,
                 age_2=True,
                 state_0=False,
                 state_1=False,
                 state_2=True,
                 diagnosis_0=False,
                 diagnosis_1=False,
                 diagnosis_2=True,
                 gender_male=False,
                 year_2019=False,
                 year_2020=True,
                 year_2021=False,
                 month_1=False,
                 month_2=False,
                 month_3=True
             )},
        {"feed_id": "200",
         "feed_data":
             FeedData(
                 provider_identifier="2000",
                 age_0=True,
                 age_1=False,
                 age_2=False,
                 state_0=False,
                 state_1=True,
                 state_2=False,
                 diagnosis_0=False,
                 diagnosis_1=True,
                 diagnosis_2=False,
                 gender_male=True,
                 year_2019=False,
                 year_2020=True,
                 year_2021=False,
                 month_1=False,
                 month_2=True,
                 month_3=False
             )},
    ]
}
