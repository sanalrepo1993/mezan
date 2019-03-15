def index():
    table_coloums = """
        [
        {'data': 'masjid_name', 'searchable': true},
        {'data': 'masjid_contact_no'},
        {'data': 'masjid_email'},
        //{'data': 'patient_martial_status'},
        //{'data': 'patient_blood_group'},
        //{'data': 'patient_phone'},
        //{'data': 'patient_email'},
        //{'data': 'patient_dob'},
        //{'data': 'patient_address'},
        //{'data': 'year'},
        //{'data': 'genres', 'name': 'genres.name', 'sortable': false},
        ]
    """
    table_colums_width = """
    [
        { "width": "50%", "targets": 0 },
        { "width": "25%", "targets": 1 },
        { "width": "25%", "targets": 2 },
        //{ "width": "5%", "targets": 3 },
        //{ "width": "2%", "targets": 4 },
        //{ "width": "20%", "targets": 5 },
        //{ "width": "20%", "targets": 6 },
        //{ "width": "10%", "targets": 7 },
        //{ "width": "20%", "targets": 8 },
    ]

    """
    table_heads = [ 
                        "Mazjid",
                        "Phone No",
                        "Email",
                        #"Blood Group",
                        #"Phone",
                        #"Email",
                        #"DOB",
                        #"Address",
                        ]

    '''
    tabnames = [
        { 'href' : '#home' , 'active':True , 'class' : '' , 'id' : '' , 'data' : 'Data'},
    ]

    tabs = [

    ]
    '''
    
    context = {
        "widget_title" : "Patients Data",
        "table_title" : "Patients",
        "widget_des" : "Records",
        "ajax" : "'/masjid/api/masjid_list/?format=datatables'",
        "add" : True,
        "add_url":"patient/add",
        "edit" : True,
        "edit_url":"patient/edit",
        "report" : True,
        "report_url":"localhost/report",
        "delete" : True,
        "delete_url":"patient/delete",
        "details_url":"patient/viewdata",
        "table_heads": table_heads,
        "columns": table_coloums,
        "column_width":table_colums_width,

    }
    return context