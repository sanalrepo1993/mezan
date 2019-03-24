def index():
    table_coloums = """
        [
        {'data': 'house_name', 'searchable': true},
        {'data': 'house_address'},
        {'data': 'house_memebrship'},
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
        { "width": "30%", "targets": 0 },
        { "width": "60%", "targets": 1 },
        { "width": "10%", "targets": 2 },
        //{ "width": "5%", "targets": 3 },
        //{ "width": "2%", "targets": 4 },
        //{ "width": "20%", "targets": 5 },
        //{ "width": "20%", "targets": 6 },
        //{ "width": "10%", "targets": 7 },
        //{ "width": "20%", "targets": 8 },
    ]

    """
    table_heads = [ 
                        "House Name",
                        "Address",
                        "Membership",
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
        "ajax" : "'/members/api/family_list/?getId=&format=datatables'",
        "add_url":"./add/family",
        "edit_url":"./edit",
        "report_url":"./report",
        "delete_url":"./delete",
        "details_url":"./details",
        "table_heads": table_heads,
        "columns": table_coloums,
        "column_width":table_colums_width,
    }
    return context