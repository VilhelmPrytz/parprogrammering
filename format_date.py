def format_date(date):
    return "{}{}{}".format(
        date[6:10],
        date[3:5],
        date[0:2]
    )

print(format_date("11/12/2019"))
print(format_date("12/31/2019"))
print(format_date("01/15/2019"))
