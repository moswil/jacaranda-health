import pandas as pd

from .messages_data import messages_df
from .subjects_data import df_ticket_sbj_phone

merged_df = pd.merge(df_ticket_sbj_phone, messages_df, on=['ticket_id'])
