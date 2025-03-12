def user_contributions_query(username):
    query = '''
    query {{
        user(login: "{0}") {{
            contributionsCollection {{
                contributionCalendar {{
                    weeks {{
                        contributionDays {{
                            date
                        }}
                    }}
                }}
            }}
        }}
    }}
    '''.format(username)
    return query