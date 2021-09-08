import os
from typing import Tuple

from .utils import read_excel_data


def get_phone_number_and_subject(sbj: str) -> Tuple[str, str]:
    phone_number = ''
    subject = ''
    if '[' in sbj and ']' in sbj:
        phone_number = sbj.split(' ')[1][:-1]
        subject = ' '.join(sbj.split(' ')[2:])
    else:
        phone_number = None
        subject = sbj
    return phone_number, subject


current_path = os.path.dirname(os.path.abspath(__file__))
resources_path = os.path.join(current_path, 'resources')

df_subjects = read_excel_data(os.path.join(resources_path,
                                           'Software_Developer_Interview_Assignment.xlsx'), sheet_name='Subjects')


df_subjects['phone_number'] = df_subjects.apply(
    lambda row: get_phone_number_and_subject(row['subject'])[0], axis=1)

df_subjects['sbj'] = df_subjects.apply(
    lambda row: get_phone_number_and_subject(row['subject'])[1], axis=1)

df_ticket_sbj_phone = df_subjects[['ticket_id', 'phone_number', 'sbj']]
