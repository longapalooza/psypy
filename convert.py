# import sqlite 3 database module as lite
import sqlite3 as lite
# import os path method
import os.path

# define unit function to perform unit conversion
# val must be float or int type
# in_unit must be str type
# out_unit must be str type
# val will be convert from in_unit units to out_unit units
def unit(val, in_unit, out_unit, dbname='unit.db'):
    # check if database exits
    if not os.path.isfile(dbname):
        print('Unit database does not exist.')
        return
    # change val to a float
    val=float(val)
    # change in_unit to a str
    in_unit=str(in_unit)
    # change out_unit to a str
    out_unit=str(out_unit)
    # define empty con variable for use with database
    con=None
    # connect to unit database
    con=lite.connect(dbname)
    # get cursor object
    cur=con.cursor()
    # execute sqlite SELECT statement for in_unit
    cur.execute('SELECT * FROM units WHERE abbreviation="'+in_unit+'"')
    # get data from in_unit row
    in_row=cur.fetchone()
    # execute sqlite SELECT statement for out_unit
    cur.execute('SELECT * FROM units WHERE abbreviation="'+out_unit+'"')
    # get data from out_unit row
    out_row=cur.fetchone()
    # check if in_unit is in database
    if in_row==None:
        # print error message if in_unit is not in database
        print('Input unit is not in database.')
        # end function
        return
    # check if out_unit is in database
    elif out_row==None:
        # print eorror message if out_unit is not in database
        print('Output unit is not in database.')
        # end function
        return
    # if in_unit and out_unit are in database
    else:
        # check if in_unit and out_unit types are the same
        if in_row[3]==out_row[3]:
            # define in_unit scale factor
            in_scale=in_row[4]
            # define in_unit reference value
            in_ref=in_row[5]
            # define out_unit scale factor
            out_scale=out_row[4]
            # define out_unit reference value
            out_ref=out_row[5]
            # convert val in in_unit units to base units of in_unit type
            val=(val+in_ref)/in_scale
            # convert val in base units of in_unit type to out_unit units
            val=val*out_scale-out_ref
            # return val
            return val
        # if in_unit and out_unit types are different
        else:
            # print error message
            print('Input unit ('+in_unit+') is not of the same type as the out'
                'put units ('+out_unit+'). Input type is '+in_row[3]+' and o'
                'utput type is '+out_row[3]+'.')
            # end function
            return