def user_contributions_query(username):
    query = '''
    query {{
        user(login: "{0}") {{
            contributionsCollection {{
                contributionCalendar {{
                    weeks {{
                        contributionDays {{
                            date, contributionCount
                        }}
                    }}
                }}
            }}
        }}
    }}
    '''.format(username)
    return query