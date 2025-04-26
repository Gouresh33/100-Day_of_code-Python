# def format_name(f_name, l_name):
#     print(f_name.title())
#     print(l_name.title())
#
# format_name("Gouresh", "PARAB")
from AppData.Local.Programs.Python.Python313.Lib.test.test_future_stmt.import_nested_scope_twice import result


def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


print(is_leap_year(2025))

# def is_leap_year(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False