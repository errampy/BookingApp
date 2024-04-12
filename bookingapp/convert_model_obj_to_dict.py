from django.forms.models import model_to_dict

def query_set_obj_to_dict(qs_obj,excluded_column=None):
    '''
    This function is resposible to convert query obj to into dict .

    paremeter:
    qs_obj : model object
    excluded_column(list) : thsi parameter type should be list instide the list item must be the model column name that need to exclud.
                            default will be None that will this will not exclude any column name .
    '''
    result_list=[]
    exclude_fields = excluded_column
    if excluded_column is not None:
        for obj in qs_obj:
            record = model_to_dict(obj, exclude=exclude_fields)
            result_list.append(record)
        return result_list
    else:
        for obj in qs_obj:
            record = model_to_dict(obj)
            result_list.append(record)
        return result_list


def get_obj_to_dict(get_obj,excluded_column=None):
    '''
    This function is resposible to convert query obj to into dict .

    paremeter:
    get_obj : model object 
    excluded_column(list) : thsi parameter type should be list instide the list item must be the model column name that need to exclud.
                            default will be None that will this will not exclude any column name .
    '''
    exclude_fields = excluded_column
    if excluded_column is not None:
        result = model_to_dict(get_obj, exclude=exclude_fields)
        return result
    else:
        result = model_to_dict(get_obj)
        return result
    
