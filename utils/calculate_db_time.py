from django.db import connection


def calculate_db_response_time():
    """RS: this function is calculating the number of DB calls made during a request-response cycle.
    We are making use of this function in common/views/def statistics(), where we are trying to optimise the
    database queries by means of prefetching the related objects."""

    sqltime = 0.0  # Variable to store execution time
    for query in connection.queries:
        sqltime += float(query["time"])  # Add the time that the query took to the total
    print("Page render: " + str(sqltime) + "sec for " + str(len(connection.queries)) + " queries")

