#Power BI Rolling Calendar
#Hello, below are the steps to create a rolling calendar in PowerBI:
#1. In the PowerQuery Editor create a Blank Query (Get Data > Blank Query or New Source > Blank Query)
#2. In the formula bar, generate a starting date by entering a "literal"
    # =date(YYYY,MM,DD) 
#3 Once you have entered and cofirmed the starting date enter this formula
    # =List.Dates (Sourece, Number.From(DateTime.LocalNow()) - Number.From(Source), #duration(1,0,0,0))
#4 Covert the resulting list into a Table (List Tools > To Table) and format the column as a Date
#End

#Note If you see something other than "Source" in Step #3, use that version instead (common for non-US users)