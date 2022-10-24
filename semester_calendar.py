import calendar

def semester_calendar(output_type, year, first_month, last_month):
    """This function create a calendar of inputed year, that starts \n from first_month and continues to last month
    >>> semester_calendar("html", 2021, 10, 10)
    <table border="0" cellpadding="0" cellspacing="0" class="month">
    <tr><th colspan="7" class="month">October 2021</th></tr>
    <tr><th class="mon">Mon</th><th class="tue">Tue</th><th class="wed">Wed</th><th class="thu">Thu</th><th class="fri">Fri</th><th class="sat">Sat</th><th class="sun">Sun</th></tr>
    <tr><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="fri">1</td><td class="sat">2</td><td class="sun">3</td></tr>
    <tr><td class="mon">4</td><td class="tue">5</td><td class="wed">6</td><td class="thu">7</td><td class="fri">8</td><td class="sat">9</td><td class="sun">10</td></tr>
    <tr><td class="mon">11</td><td class="tue">12</td><td class="wed">13</td><td class="thu">14</td><td class="fri">15</td><td class="sat">16</td><td class="sun">17</td></tr>
    <tr><td class="mon">18</td><td class="tue">19</td><td class="wed">20</td><td class="thu">21</td><td class="fri">22</td><td class="sat">23</td><td class="sun">24</td></tr>
    <tr><td class="mon">25</td><td class="tue">26</td><td class="wed">27</td><td class="thu">28</td><td class="fri">29</td><td class="sat">30</td><td class="sun">31</td></tr>
    </table>
    <BLANKLINE>

    >>> semester_calendar("txt", 2021, 10, 10)
        October 2021
    Mo Tu We Th Fr Sa Su
                 1  2  3
     4  5  6  7  8  9 10
    11 12 13 14 15 16 17
    18 19 20 21 22 23 24
    25 26 27 28 29 30 31
    <BLANKLINE>

    >>> semester_calendar(12, 2021, 10, 10)
    None
    >>> semester_calendar("txt", "hello", 10, 10)
    None
    >>> semester_calendar("txt", 2021, "Howru", 10)
    None
    >>> semester_calendar("txt", 2021, 10, "culater")
    None
    """
    if not isinstance(output_type, str):
        print ("None")
        return
    if not isinstance(year, int):
        print ("None")
        return
    if not isinstance(first_month, int):
        print ("None")
        return
    if not isinstance(last_month, int):
        print ("None")
        return
    if output_type == "txt":
        for i in range (last_month - first_month + 1):
            print(calendar.month(year, first_month+i, w=0, l=0))
        return
    html_calendar = calendar.HTMLCalendar()
    for j in range (last_month - first_month + 1):
        print(html_calendar.formatmonth(year, first_month + j))
    return

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())