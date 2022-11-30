
def test(ws,cellnumber,director_1_Read,director_2_Read,director_3_Read,titleRead,yearRead):        
    cell = 'C' + str(cellnumber)
    ws[cell].value = titleRead
    # YEAR OF RELEASE 
    cellRYear = 'E' + str(cellnumber)
    ws[cellRYear].value = yearRead

    # DIRECTOR(S)
    cellRDirector_1 = 'F' + str(cellnumber)
    ws[cellRDirector_1].value = None                # removing the previous value from the cell
    if director_1_Read != None:
            ws[cellRDirector_1].value = director_1_Read

    cellRDirector_2 = 'F' + str(int(cellnumber) + 1)
    ws[cellRDirector_2].value = None
    if director_2_Read != None:
            ws[cellRDirector_2].value = director_2_Read

    cellRDirector_3 = 'F' + str(int(cellnumber) + 2)
    ws[cellRDirector_3].value = None
    if director_3_Read != None:
            ws[cellRDirector_3].value = director_3_Read